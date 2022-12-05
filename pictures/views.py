from django.shortcuts import render
from django.http  import HttpResponse
from .models import Categories, Images, Locations

# Create your views here.

def gallery(request):
    images = Images.get_all()
    location = Locations.get_all(id)

    return render(request, 'photos/photos.html', {'images': images, 'location':location})




def category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images = Images.search_image(search_term)

        message = f'{search_term}'

        return render(request, 'photos/category.html', {'message':message, 'images':images})
    else:
        message = 'You have not searched any term'
        return render(request, 'photos/category.html', {'message':message})

def location(request):
        search_term = request.GET.get('location')
        images = Images.filter_by_location(search_term)
        message = f'{search_term}'
        location = Locations.get_all(id)

        return render(request, 'photos/location.html', {'message':message, 'images':images,'location':location})
   