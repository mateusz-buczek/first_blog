from django.http import HttpResponse


def blog_index(request):
    return HttpResponse("This is main blog page.")