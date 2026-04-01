from django.core.management.base import BaseCommand
from django.utils import timezone
from main.models import (
    AboutPage,
    TimelineEntry,
    CompanyValue,
    HowWeWorkStep,
    Project,
    Testimonial,
    SiteStat,
    TeamMember,
    PricingPlan,
    Product,
    Category,
)
from services.models import Service, ServiceCategory, CaseStudy
from marketplace.models import Product as MarketplaceProduct
import random

class Command(BaseCommand):
    help = 'Seed comprehensive data for DravTech website'

    def handle(self, *args, **options):
        self.stdout.write("🌱 Starting DravTech data seeding...")
        
        # 1. About Page Content (excluding team)
        self.create_about_page_content()
        
        # 2. Services and Categories
        self.create_services_data()
        
        # 3. Marketplace Products
        self.create_marketplace_products()
        
        # 4. Site Stats
        self.create_site_stats()
        
        self.stdout.write(self.style.SUCCESS("✅ DravTech data seeding completed!"))

    def create_about_page_content(self):
        """Create About page content excluding team sections"""
        self.stdout.write("📝 Creating About page content...")
        
        # Create About Page
        about_page = AboutPage.objects.create(
            is_active=True,
            hero_headline="Transforming Ideas Into Digital Reality",
            hero_subtitle="We are a team of passionate innovators dedicated to crafting exceptional digital experiences that drive business growth and inspire users.",
            hero_cta_label="Learn More",
            hero_cta_url="/services/",
            mission_title="Our Mission",
            mission_body="To empower businesses with cutting-edge digital solutions that bridge the gap between imagination and reality, creating meaningful connections between brands and their audiences.",
            vision_title="Our Vision", 
            vision_body="To be the leading digital innovation partner in Africa, recognized for our creativity, technical excellence, and unwavering commitment to client success.",
            how_we_work_title="How We Work",
            how_we_work_intro="Our proven process ensures successful project delivery through collaboration, innovation, and attention to detail.",
            final_cta_headline="Ready to Transform Your Digital Presence?",
            final_cta_subtext="Let's collaborate to bring your vision to life with our innovative solutions and expert team.",
            final_cta_label="Start Your Journey",
            final_cta_url="/contact/",
        )
        
        # Timeline Entries
        timeline_data = [
            {
                'year_label': '2020',
                'title': 'DravTech Founded',
                'description': 'Started with a vision to revolutionize digital experiences in Kenya',
                'display_order': 1,
            },
            {
                'year_label': '2021', 
                'title': 'First Major Client',
                'description': 'Partnered with leading fintech company for complete digital transformation',
                'display_order': 2,
            },
            {
                'year_label': '2022',
                'title': 'Team Expansion',
                'description': 'Grew our team to 15+ talented professionals across multiple disciplines',
                'display_order': 3,
            },
            {
                'year_label': '2023',
                'title': 'Innovation Award',
                'description': 'Recognized as "Most Innovative Digital Agency" at Kenya Tech Awards',
                'display_order': 4,
            },
            {
                'year_label': '2024',
                'title': 'Regional Expansion',
                'description': 'Expanded operations to serve clients across East Africa',
                'display_order': 5,
            },
        ]
        
        for entry_data in timeline_data:
            TimelineEntry.objects.create(**entry_data)
        
        # Company Values
        values_data = [
            {
                'title': 'Innovation First',
                'description': 'We embrace cutting-edge technologies and creative approaches to solve complex challenges and deliver exceptional results.',
                'display_order': 1,
            },
            {
                'title': 'Client Success',
                'description': 'Your success is our success. We are committed to delivering solutions that exceed expectations and drive measurable growth.',
                'display_order': 2,
            },
            {
                'title': 'Quality Excellence',
                'description': 'We maintain the highest standards of quality in everything we create, ensuring robust, scalable, and beautiful solutions.',
                'display_order': 3,
            },
            {
                'title': 'Collaborative Spirit',
                'description': 'We believe in the power of collaboration, working closely with clients to transform their vision into reality.',
                'display_order': 4,
            },
            {
                'title': 'Continuous Learning',
                'description': 'We stay ahead of industry trends through continuous learning, research, and adaptation to new technologies.',
                'display_order': 5,
            },
            {
                'title': 'Integrity & Trust',
                'description': 'We build lasting relationships based on transparency, honesty, and delivering on our promises.',
                'display_order': 6,
            },
        ]
        
        for value_data in values_data:
            CompanyValue.objects.create(**value_data)
        
        # How We Work Steps
        steps_data = [
            {
                'step_number': 1,
                'title': 'Discovery & Strategy',
                'description': 'We dive deep into understanding your business, goals, and target audience to develop a comprehensive digital strategy.',
            },
            {
                'step_number': 2,
                'title': 'Design & Prototyping',
                'description': 'Our creative team crafts stunning designs and interactive prototypes that bring your vision to life.',
            },
            {
                'step_number': 3,
                'title': 'Development & Implementation',
                'description': 'We transform designs into robust, scalable solutions using the latest technologies and best practices.',
            },
            {
                'step_number': 4,
                'title': 'Testing & Quality Assurance',
                'description': 'Rigorous testing ensures your solution is bug-free, secure, and performs optimally across all platforms.',
            },
            {
                'step_number': 5,
                'title': 'Launch & Support',
                'description': 'We handle seamless deployment and provide ongoing support to ensure your continued success.',
            },
        ]
        
        for step_data in steps_data:
            HowWeWorkStep.objects.create(**step_data)
        
        # Sample Projects
        projects_data = [
            {
                'title': 'FinTech Mobile App',
                'slug': 'fintech-mobile-app',
                'summary': 'Revolutionary mobile banking application serving 50,000+ users.',
                'description': 'Revolutionary mobile banking application serving 50,000+ users with advanced security features and seamless user experience.',
                'link': '#',
                'is_featured': True,
                'display_order': 1,
            },
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'summary': 'Full-featured online marketplace with AI-powered recommendations.',
                'description': 'Full-featured online marketplace with AI-powered recommendations and seamless payment integration.',
                'link': '#',
                'is_featured': True,
                'display_order': 2,
            },
            {
                'title': 'Healthcare Portal',
                'slug': 'healthcare-portal',
                'summary': 'Comprehensive patient management system with telemedicine capabilities.',
                'description': 'Comprehensive patient management system with telemedicine capabilities and real-time monitoring.',
                'link': '#',
                'display_order': 3,
            },
        ]
        
        for project_data in projects_data:
            Project.objects.create(**project_data)
        
        # Testimonials
        testimonials_data = [
            {
                'quote': 'DravTech transformed our digital presence completely. Their innovative approach and technical expertise helped us reach new markets.',
                'author_name': 'Sarah Johnson',
                'organization': 'TechStart Kenya',
                'role': 'CEO',
                'display_order': 1,
            },
            {
                'quote': 'Working with DravTech was a game-changer for our fintech platform. They delivered beyond our expectations and on time.',
                'author_name': 'Michael Chen',
                'organization': 'AfriPay Solutions',
                'role': 'CTO',
                'display_order': 2,
            },
            {
                'quote': 'The healthcare portal they built for us has revolutionized how we serve our patients. Exceptional work!',
                'author_name': 'Grace Wanjiru',
                'organization': 'MediCare Plus',
                'role': 'Operations Director',
                'display_order': 3,
            },
        ]
        
        for testimonial_data in testimonials_data:
            Testimonial.objects.create(**testimonial_data)

    def create_services_data(self):
        """Create services and categories"""
        self.stdout.write("🔧 Creating services data...")
        
        # Service Categories
        categories_data = [
            {
                'name': 'Web Development',
                'short_description': 'Custom web applications and websites',
                'description': 'Building responsive, fast, and secure web applications using cutting-edge technologies.',
                'icon': 'bi-globe',
                'display_order': 1,
            },
            {
                'name': 'Mobile Development',
                'short_description': 'iOS and Android applications',
                'description': 'Creating native and cross-platform mobile applications that deliver exceptional user experiences.',
                'icon': 'bi-phone',
                'display_order': 2,
            },
            {
                'name': 'UI/UX Design',
                'short_description': 'User interface and experience design',
                'description': 'Designing intuitive, beautiful, and user-centered interfaces that engage and convert.',
                'icon': 'bi-palette',
                'display_order': 3,
            },
            {
                'name': 'Digital Marketing',
                'short_description': 'Online marketing and growth strategies',
                'description': 'Data-driven digital marketing strategies that help you reach and engage your target audience.',
                'icon': 'bi-megaphone',
                'display_order': 4,
            },
        ]
        
        for cat_data in categories_data:
            ServiceCategory.objects.create(**cat_data)
        
        # Services
        web_dev_cat = ServiceCategory.objects.get(name='Web Development')
        mobile_cat = ServiceCategory.objects.get(name='Mobile Development')
        design_cat = ServiceCategory.objects.get(name='UI/UX Design')
        marketing_cat = ServiceCategory.objects.get(name='Digital Marketing')
        
        services_data = [
            {
                'title': 'Custom Web Applications',
                'short_description': 'Tailored web solutions for your business',
                'description': 'We build custom web applications that solve specific business challenges and drive growth.',
                'category': web_dev_cat,
                'price': 150000,
                'image': 'services/custom-web.jpg',
                'featured': True,
                'display_order': 1,
            },
            {
                'title': 'E-Commerce Solutions',
                'short_description': 'Complete online store development',
                'description': 'End-to-end e-commerce solutions with payment integration, inventory management, and analytics.',
                'category': web_dev_cat,
                'price': 200000,
                'image': 'services/ecommerce.jpg',
                'featured': True,
                'display_order': 2,
            },
            {
                'title': 'Mobile App Development',
                'short_description': 'iOS and Android native apps',
                'description': 'Native mobile applications that deliver superior performance and user experience.',
                'category': mobile_cat,
                'price': 300000,
                'image': 'services/mobile-app.jpg',
                'featured': True,
                'display_order': 3,
            },
            {
                'title': 'UI/UX Design',
                'short_description': 'User-centered design solutions',
                'description': 'Comprehensive UI/UX design services from research to final implementation.',
                'category': design_cat,
                'price': 100000,
                'image': 'services/ui-ux.jpg',
                'display_order': 4,
            },
            {
                'title': 'SEO Optimization',
                'short_description': 'Search engine optimization services',
                'description': 'Improve your search rankings and drive organic traffic with our SEO expertise.',
                'category': marketing_cat,
                'price': 75000,
                'image': 'services/seo.jpg',
                'display_order': 5,
            },
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)
        
        # Case Studies
        web_service = Service.objects.get(title='Custom Web Applications')
        mobile_service = Service.objects.get(title='Mobile App Development')
        
        case_studies_data = [
            {
                'title': 'Banking Platform Redesign',
                'client': 'Equity Bank Kenya',
                'description': 'Complete redesign of legacy banking platform with modern UI/UX and enhanced security features.',
                'challenge': 'Outdated interface, poor user experience, security vulnerabilities',
                'solution': 'Modern responsive design, enhanced security protocols, real-time updates',
                'results': '300% increase in user engagement, 95% reduction in security incidents',
                'service': web_service,
                'image': 'case-studies/banking.jpg',
                'featured': True,
                'display_order': 1,
            },
            {
                'title': 'Ride-Hailing Mobile App',
                'client': 'QuickRide Kenya',
                'description': 'End-to-end ride-hailing application with real-time tracking and payment integration.',
                'challenge': 'Need for reliable transportation solution with seamless payments',
                'solution': 'Native mobile apps with GPS tracking, multiple payment options, driver management',
                'results': '50,000+ downloads, 4.8-star rating, operations in 5 cities',
                'service': mobile_service,
                'image': 'case-studies/rideshare.jpg',
                'featured': True,
                'display_order': 2,
            },
        ]
        
        for case_data in case_studies_data:
            CaseStudy.objects.create(**case_data)

    def create_marketplace_products(self):
        """Create marketplace products"""
        self.stdout.write("🛍️ Creating marketplace products...")
        
        # Create categories
        digital_cat = Category.objects.create(name='Digital Products', slug='digital-products')
        merch_cat = Category.objects.create(name='Merchandise', slug='merchandise') 
        artwork_cat = Category.objects.create(name='Artwork', slug='artwork')
        
        # Digital Products
        digital_products = [
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
                'title': 'Mobile App Templates',
                'slug': 'mobile-app-templates',
                'description': 'Collection of premium mobile app templates for iOS and Android.',
                'product_type': 'digital',
                'category': digital_cat,
                'price': 18000,
                'is_active': True,
            },
        ]
        
        # Merchandise
        merch_products = [
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
                'title': 'Tech Enthusiast T-Shirt',
                'slug': 'tech-tshirt',
                'description': 'Comfortable cotton t-shirt perfect for tech enthusiasts.',
                'product_type': 'merch',
                'category': merch_cat,
                'price': 1500,
                'is_active': True,
            },
        ]
        
        # Artwork
        artwork_products = [
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
            {
                'title': 'Abstract Tech Art',
                'slug': 'abstract-tech-art',
                'description': 'Modern abstract artwork inspired by technology and innovation.',
                'product_type': 'artwork',
                'category': artwork_cat,
                'price': 3000,
                'is_active': True,
            },
        ]
        
        all_products = digital_products + merch_products + artwork_products
        
        for product_data in all_products:
            MarketplaceProduct.objects.create(**product_data)
        
        # Create pricing plans for digital products
        for product in MarketplaceProduct.objects.filter(product_type='digital'):
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
                price=product.price * 1.5,
                features=['Priority support', 'Lifetime updates', 'Documentation', 'Source code'],
                is_popular=True,
            )

    def create_site_stats(self):
        """Create site statistics"""
        self.stdout.write("📊 Creating site statistics...")
        
        stats_data = [
            {
                'stat_number': '150+',
                'stat_label': 'Projects Completed',
                'display_order': 1,
            },
            {
                'stat_number': '50+',
                'stat_label': 'Happy Clients',
                'display_order': 2,
            },
            {
                'stat_number': '10+',
                'stat_label': 'Years Experience',
                'display_order': 3,
            },
            {
                'stat_number': '15+',
                'stat_label': 'Team Members',
                'display_order': 4,
            },
        ]
        
        for stat_data in stats_data:
            SiteStat.objects.create(**stat_data)
