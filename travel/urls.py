from django.urls import path
from .views import home_view, about_view, service_view, package_view, blog_view, single_view, destination_view, \
	guide_view, testimonial_view, contact_view

urlpatterns = [
	path('', home_view, name='home'),
	path('about/', about_view, name='about'),
	path('service/', service_view, name='service'),
	path('packege/', package_view, name='package'),
	path('blog/', blog_view, name='blog'),
	path('single/', single_view, name='single'),
	path('destination/', destination_view, name='destination'),
	path('guide/', guide_view, name='guide'),
	path('testimonial/', testimonial_view, name='testimonial'),
	path('contact/', contact_view, name='contact')
]
