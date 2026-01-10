# Standard Deployment Commands
ssh root@72.62.197.43
cd /root/deploy/printingbackend
git pull origin main
cd backend
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart gunicorn-printingbackend

# Database Import Commands
# 1. Backup existing database
sudo -u postgres pg_dump vistaprint_db > /root/deploy/printingbackend/backups/backup_$(date +%Y%m%d_%H%M%S).sql

# 2. Import SQL dump
sudo -u postgres psql vistaprint_db < /root/deploy/printingbackend/local_data_utf8.sql

# 3. Run migrations after import
cd /root/deploy/printingbackend/backend
source venv/bin/activate
python manage.py migrate
sudo systemctl restart gunicorn-printingbackend
