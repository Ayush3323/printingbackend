from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the name")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the name")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='subcategories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=50, unique=True, help_text="Stock Keeping Unit")
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=500, blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Inventory & Logistics
    stock_quantity = models.IntegerField(default=0, help_text="Available stock")
    is_infinite_stock = models.BooleanField(default=True, help_text="For POD items")
    weight_kg = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    
    # SEO
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PrintSpecs(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='print_specs')
    width_mm = models.FloatField(help_text="Final trim width in mm")
    height_mm = models.FloatField(help_text="Final trim height in mm")
    bleed_margin_mm = models.FloatField(default=3.0, help_text="Bleed area to add on each side")
    safe_zone_mm = models.FloatField(default=3.0, help_text="Safe zone margin from trim line")
    
    # Technical Specs
    format_template_url = models.URLField(blank=True, help_text="Link to AI/PSD template")
    allowed_file_types = models.CharField(max_length=255, default='pdf,jpg,png,svg')
    min_resolution_dpi = models.IntegerField(default=300)

    def __str__(self):
        return f"Specs for {self.product.name}"

class ProductAttribute(models.Model):
    """
    Defines configurable options (e.g., Size, Paper Type, Finish)
    """
    TYPE_CHOICES = (
        ('text', 'Text Label'),
        ('color', 'Color Swatch'),
        ('image', 'Image Selection'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, blank=True)
    attribute_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')
    is_required = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.product.name} - {self.name}"

class AttributeValue(models.Model):
    """
    Specific choices for an attribute (e.g., Matte, Glossy)
    """
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100)
    display_value = models.CharField(max_length=100, blank=True)
    price_adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_default = models.BooleanField(default=False)
    swatch_color = models.CharField(max_length=20, blank=True, help_text="Hex code for color swatch")
    swatch_image = models.ImageField(upload_to='attribute_swatches/', null=True, blank=True)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"
