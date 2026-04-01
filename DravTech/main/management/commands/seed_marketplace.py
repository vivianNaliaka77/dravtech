from django.core.management.base import BaseCommand
from marketplace.models import Product as MarketplaceProduct
from main.models import Product, PricingPlan, Category

class Command(BaseCommand):
    help = 'Seed basic marketplace products'

    def handle(self, *args, **options):
        self.stdout.write("🛍️ Seeding marketplace products...")
        
        # Clear existing products and categories
        MarketplaceProduct.objects.all().delete()
        Category.objects.all().delete()
        
        # Create categories
        digital_cat = Category.objects.create(name='Digital Products', slug='digital-products')
        merch_cat = Category.objects.create(name='Merchandise', slug='merchandise') 
        artwork_cat = Category.objects.create(name='Artwork', slug='artwork')
        
        # Create products
        products_data = [
            {
                'title': 'Web Development Toolkit',
                'slug': 'web-dev-toolkit',
                'description': 'Complete toolkit for modern web development with templates, components, and guides.',
                'product_type': 'digital',
                'category': digital_cat,
                'price': 15000,
                'is_featured': True,
                'is_active': True,
            },
            {
                'title': 'UI Design System',
                'slug': 'ui-design-system',
                'description': 'Comprehensive UI design system with components, patterns, and style guides.',
                'product_type': 'digital',
                'category': digital_cat,
                'price': 12000,
                'is_featured': True,
                'is_active': True,
            },
            {
                'title': 'DravTech Branded Hoodie',
                'slug': 'dravtech-hoodie',
                'description': 'Premium quality hoodie with DravTech branding. Comfortable and stylish.',
                'product_type': 'merch',
                'category': merch_cat,
                'price': 3500,
                'is_active': True,
            },
            {
                'title': 'Digital Landscape Collection',
                'slug': 'digital-landscape',
                'description': 'Stunning digital landscape artwork collection in high resolution.',
                'product_type': 'artwork',
                'category': artwork_cat,
                'price': 5000,
                'is_featured': True,
                'is_active': True,
            },
        ]
        
        for product_data in products_data:
            product = MarketplaceProduct.objects.create(**product_data)
            
            # Create pricing plans for digital products
            if product.product_type == 'digital':
                PricingPlan.objects.create(
                    product=product,
                    name='Basic',
                    price=product.price,
                    features=['Basic support', '1 year updates', 'Documentation'],
                    is_popular=False,
                )
                PricingPlan.objects.create(
                    product=product,
                    name='Professional',
                    price=int(product.price * 1.5),
                    features=['Priority support', 'Lifetime updates', 'Documentation', 'Source code'],
                    is_popular=True,
                )
        
        self.stdout.write(self.style.SUCCESS("✅ Marketplace products seeded successfully!"))
        self.stdout.write(f"   - Categories: 3")
        self.stdout.write(f"   - Products: {len(products_data)}")
        self.stdout.write(f"   - Pricing Plans: 4")
