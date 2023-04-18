from django.shortcuts import render
from blog.models import Post


def main(request):
    return render(
        request,
        'single_pages/main.html'
    )
