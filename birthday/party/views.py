from django.shortcuts import render
from .models import Content

def index(request):
    # Get all content objects
    contents = Content.objects.all()
    
    # Define the carousel slides
    carousel_slides = [
        {'image': 'party/images/1.jpg', 'alt_text': 'Slide 1'},
        {'image': 'party/images/2.jpg', 'alt_text': 'Slide 2'},
        {'image': 'party/images/3.jpg', 'alt_text': 'Slide 3'},
        {'image': 'party/images/4.jpg', 'alt_text': 'Slide 4'},
        {'image': 'party/images/5.jpg', 'alt_text': 'Slide 5'},
        {'image': 'party/images/6.jpg', 'alt_text': 'Slide 6'},
        {'image': 'party/images/7.jpg', 'alt_text': 'Slide 7'},
        {'image': 'party/images/8.jpg', 'alt_text': 'Slide 8'},
        {'image': 'party/images/9.jpg', 'alt_text': 'Slide 9'},
        {'image': 'party/images/10.jpg', 'alt_text': 'Slide 10'},

    ]
    
    # Create the context dictionary with both contents and carousel slides
    context = {
        'Contents': contents,
        'carousel_slides': carousel_slides
    }
    
    # Render the template with the combined context
    return render(request, 'party/index.html', context)

def login_view(request):
    return render(request, 'party/login.html')

# create room 
def room_view(request):
    return render(request, 'party/room.html')

def present_view(request):
    return render(request, 'party/present.html')

def letter_view(request):
    return render(request, 'party/letter.html')