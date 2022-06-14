import random

from django.shortcuts import HttpResponse, render

topics = [
    {"id": 1, "title": "routing", "body": "Routing is .."},
    {"id": 2, "title": "view", "body": "View is .."},
    {"id": 3, "title": "model", "body": "Model is .."},
]
# Create your views here.
def index(request):
    global topics
    ol = ""
    for topic in topics:
        ol += f'<li><a>{topic["title"]}</a></li>'
    return HttpResponse(
        f"""
    <html>
    </body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    """
    )


def create(request):
    return HttpResponse("Create")


def read(request, id):
    return HttpResponse("Read!" + id)
