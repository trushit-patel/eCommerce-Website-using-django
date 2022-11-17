from django.shortcuts import redirect, render
from.models import Userdata


from django.views.decorators.csrf import csrf_protect

@csrf_protect

def homepageview(request):
    return render(request,'index.html')

def aboutpageview(request):
    return render(request,'about.html')

def getformdata(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    user = Userdata()
    user.name = name
    user.Email = email
    user.subject = subject
    user.message = message

    user.save()
    return redirect('formdata')

def contactpageview(request):
    return render(request,'contact.html')

def blogpost(request):
    return render(request,'blog-post.html')

def formdata(request):
    myproduct = Userdata.objects.all()
    print(myproduct)
    return render(request, "formdata.html",{'myproduct':myproduct})

def blog(request):
    return render(request,'blog.html')

def checkout(request):
    return render(request,'checkout.html')

def productdetails(request):
    return render(request,'product-details.html')

def products(request):
    return render(request,'products.html')

def terms(request):
    return render(request,'terms.html')

def testimonials(request):
    return render(request,'testimonials.html')