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
)

class Command(BaseCommand):
    help = 'Seed About page content for DravTech website'

    def handle(self, *args, **options):
        self.stdout.write("📝 Seeding About page content...")
        
        # Clear existing data
        AboutPage.objects.filter(is_active=True).update(is_active=False)
        TimelineEntry.objects.all().delete()
        CompanyValue.objects.all().delete()
        HowWeWorkStep.objects.all().delete()
        Project.objects.all().delete()
        Testimonial.objects.all().delete()
        SiteStat.objects.all().delete()
        
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
                'image': 'projects/fintech-app.jpg',
            },
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'summary': 'Full-featured online marketplace with AI-powered recommendations.',
                'description': 'Full-featured online marketplace with AI-powered recommendations and seamless payment integration.',
                'link': '#',
                'is_featured': True,
                'display_order': 2,
                'image': 'projects/ecommerce.jpg',
            },
            {
                'title': 'Healthcare Portal',
                'slug': 'healthcare-portal',
                'summary': 'Comprehensive patient management system with telemedicine capabilities.',
                'description': 'Comprehensive patient management system with telemedicine capabilities and real-time monitoring.',
                'link': '#',
                'display_order': 3,
                'image': 'projects/healthcare.jpg',
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
        
        # Site Stats
        stats_data = [
            {
                'value': '150+',
                'label': 'Projects Completed',
                'display_order': 1,
            },
            {
                'value': '50+',
                'label': 'Happy Clients',
                'display_order': 2,
            },
            {
                'value': '10+',
                'label': 'Years Experience',
                'display_order': 3,
            },
            {
                'value': '15+',
                'label': 'Team Members',
                'display_order': 4,
            },
        ]
        
        for stat_data in stats_data:
            SiteStat.objects.create(**stat_data)
        
        self.stdout.write(self.style.SUCCESS("✅ About page content seeded successfully!"))
        self.stdout.write(f"   - About Page: 1 entry")
        self.stdout.write(f"   - Timeline Entries: {len(timeline_data)}")
        self.stdout.write(f"   - Company Values: {len(values_data)}")
        self.stdout.write(f"   - How We Work Steps: {len(steps_data)}")
        self.stdout.write(f"   - Projects: {len(projects_data)}")
        self.stdout.write(f"   - Testimonials: {len(testimonials_data)}")
        self.stdout.write(f"   - Site Stats: {len(stats_data)}")
