Architecture (final)

Client → https://printing-website-beta.vercel.app
 → https://api.printdoot.com
 → Nginx → Gunicorn (socket) → Django → PostgreSQL

No IP. No :8000. Only domain over HTTPS.

Important Paths (never forget)

Project root (backend):

/home/printdoot/printingbackend/backend


Django .env:

/home/printdoot/printingbackend/backend/.env


Gunicorn service:

/etc/systemd/system/gunicorn-printingbackend.service


Nginx site config:

/etc/nginx/sites-available/printingbackend
/etc/nginx/sites-enabled/printingbackend


Gunicorn socket:

/run/gunicorn/printingbackend.sock


Postgres DB:

DB: printdootdb
User: printdootuser

1) Update CORS / Hosts (most common task)

Open env:

nano /home/printdoot/printingbackend/backend/.env


Ensure these lines exist:

ALLOWED_HOSTS=api.printdoot.com

CORS_ALLOWED_ORIGINS=https://printing-website-beta.vercel.app


Save.

Restart backend:

systemctl restart gunicorn-printingbackend

2) Check everything is running (health check)

Gunicorn:

systemctl status gunicorn-printingbackend


Nginx:

systemctl status nginx


Test from VPS:

curl -I https://api.printdoot.com/api/v1/


You must get 200, 301, or 404. Anything else = problem.

3) When you pull new backend code from Git
su - printdoot
cd /home/printdoot/printingbackend/backend
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
deactivate


Restart:

systemctl restart gunicorn-printingbackend

4) When database dump needs to be restored

Upload from local:

scp C:\path\file.sql root@72.62.197.43:/tmp/dump.sql


Restore:

sudo -u postgres psql
DROP DATABASE printdootdb;
CREATE DATABASE printdootdb OWNER printdootuser;
\q

sudo -u postgres psql printdootdb < /tmp/dump.sql


Fix privileges (important):

sudo -u postgres psql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO printdootuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO printdootuser;
\q

5) When SSL renews or breaks

Check cert:

certbot certificates


Renew manually:

certbot renew
systemctl restart nginx

6) If site shows 502 Bad Gateway

Means Gunicorn/socket problem.

Fix:

mkdir -p /run/gunicorn
chown printdoot:www-data /run/gunicorn
systemctl restart gunicorn-printingbackend
systemctl restart nginx

7) If CORS error happens from Vercel

Only edit:

/home/printdoot/printingbackend/backend/.env


Add new frontend URL in:

CORS_ALLOWED_ORIGINS=


Restart gunicorn.

8) Never do these again

❌ Never use IP in frontend
❌ Never use :8000 in production
❌ Never edit nginx to point to 127.0.0.1:8000 (use socket)
❌ Never touch DNS again

9) One-line service restart (after any change)
systemctl restart gunicorn-printingbackend nginx

10) Quick sanity test from browser

Open:

https://api.printdoot.com/api/v1/


If it loads → backend healthy.

This is permanent operational manual for this VPS.