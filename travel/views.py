from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def service_view(request):
    return render(request, 'service.html')


def package_view(request):
    return render(request, 'package.html')


def blog_view(request):
    return render(request, 'blog.html')


def single_view(request):
    return render(request, 'single.html')


def destination_view(request):
    return render(request, 'destination.html')


def guide_view(request):
    return render(request, 'guide.html')


def testimonial_view(request):
    return render(request, 'testimonial.html')


def contact_view(request):
    return render(request, 'contact.html')
