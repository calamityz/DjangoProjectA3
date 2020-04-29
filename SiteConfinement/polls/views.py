from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Test")
# Create your views here.
