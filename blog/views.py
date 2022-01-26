from django.http import HttpResponse
from django.shortcuts import render

data={
    "blogs": [
        {
            "id":1,
            "title":"erdem okutan",
            "image":"portal.png",
            "is_active": True,
            "is_home": False,
            "description":"fevkaladenin fevkinde"
        },
{
            "id":2,
            "title":"beyin fukarası erdem",
            "image":"portal.png",
            "is_active": True,
            "is_home": True,
            "description":"fevkaladenin fevkinde"
        },
{
            "id":3,
            "title":"zihin züğürdü erdem",
            "image":"portal.png",
            "is_active": False,
            "is_home": True,
            "description":"fevkaladenin fevkinde"
        }
    ]
}
# Create your views here.
def index(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request, "blog/index.html",context)


def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html",context)


def blog_details(request, id):
    blogs=data["blogs"]
    selectedBlog=None

    for blog in blogs:
        if blog["id"]==id:
            selectedBlog=blog


    return render(request, "blog/blog-details.html", {
       "blog": selectedBlog
    })
