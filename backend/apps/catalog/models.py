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
    
    # Pricing
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Discounts
    DISCOUNT_TYPE_CHOICES = (
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
    )
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES, blank=True, null=True)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Percentage or fixed amount")
    discount_start_date = models.DateTimeField(null=True, blank=True)
    discount_end_date = models.DateTimeField(null=True, blank=True)
    is_on_sale = models.BooleanField(default=False)
    
    # Media (S3 URLs)
    primary_image = models.URLField(max_length=500, blank=True, null=True, help_text="S3 URL for primary image")
    
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

    @property
    def final_price(self):
        """Calculate final price after discount"""
        if not self.is_on_sale or not self.discount_value:
            return self.base_price
        
        from django.utils import timezone
        now = timezone.now()
        
        # Check if discount is active
        if self.discount_start_date and now < self.discount_start_date:
            return self.base_price
        if self.discount_end_date and now > self.discount_end_date:
            return self.base_price
        
        # Apply discount
        if self.discount_type == 'percentage':
            discount_amount = self.base_price * (self.discount_value / 100)
            return max(self.base_price - discount_amount, 0)
        else:  # fixed
            return max(self.base_price - self.discount_value, 0)

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

class ProductImage(models.Model):
    """
    Multiple images for a product (gallery) - S3 URLs
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.URLField(max_length=500, help_text="S3 URL for product image")
    alt_text = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', 'created_at']

    def __str__(self):
        return f"{self.product.name} - Image {self.display_order}"

class ProductReview(models.Model):
    """
    Customer reviews for products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='product_reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="1-5 stars")
    title = models.CharField(max_length=200, blank=True)
    comment = models.TextField()
    is_verified_purchase = models.BooleanField(default=False)
    helpful_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('product', 'user')  # One review per user per product

    def __str__(self):
        return f"{self.user.email} - {self.product.name} ({self.rating}★)"

