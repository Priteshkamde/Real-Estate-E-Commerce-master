from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, PropertyPostForm
from .models import Properties, Comments, ImageElement
import time


def index(request):
    return render(request, 'ecommerce/index.html')


def detail(request):
    search = request.GET['q']
    properties = get_list_or_404(Properties, locality=search)
    if request.method == 'POST':
        value = request.POST['sort']
        if value == 'relevance':
            pass
            # properties.sort(properties.)

    return render(request, 'ecommerce/detail.html', {'properties': properties})


def property_detail(request, pk):
    property_obj = get_object_or_404(Properties, pk=pk)
    comments = Comments.objects.all()
    images = ImageElement.objects.all()
    if request.method == 'POST':
        com = Comments()
        com.user = request.user
        com.property_title = property_obj.property_title
        com.datetime = str(time.asctime(time.localtime(time.time())))
        com.comment = request.POST['a']
        com.save()
    return render(request, 'ecommerce/property_detail.html',
                  {'property': property_obj, 'comments': comments, 'images': images})


def post_property(request):
    i = 1
    form = PropertyPostForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.user.is_authenticated and (
            request.user.type == "seller" or request.user.type == "lessor"):
        property_obj = form.save(commit=False)
        property_obj.post_date_time = time.asctime(time.localtime(time.time()))
        property_obj.user = request.user
        property_obj.property_title = form.cleaned_data['property_title']
        if request.user.type == "seller":
            property_obj.buy_rent = 'Sale'
        else:
            property_obj.buy_rent = 'Rent'
        property_obj.locality = form.cleaned_data['locality']
        property_obj.property_type = form.cleaned_data['property_type']
        property_obj.price = int(form.cleaned_data['price'])
        property_obj.BHK = form.cleaned_data['BHK']
        property_obj.construction_status = form.cleaned_data['construction_status']
        property_obj.area = int(form.cleaned_data['area'])
        property_obj.address = form.cleaned_data['address']
        property_obj.description = form.cleaned_data['description']
        property_obj.save()
        image = request.FILES.get('image' + str(i), False)
        while image:
            image_obj = ImageElement()
            image_obj.image = request.FILES['image' + str(i)]
            image_obj.post = property_obj
            image_obj.save()
            i = i + 1
            image = request.FILES.get('image' + str(i), False)

    return render(request, 'ecommerce/post_property.html', {'form': form})


def dashboard(request):
    properties = Properties.objects.all()
    return render(request, 'ecommerce/dashboard.html', {'properties': properties})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'ecommerce/index.html')
            else:
                return render(request, 'ecommerce/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ecommerce/login.html', {'error_message': 'Invalid login'})
    return render(request, 'ecommerce/login.html')


def register_user(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user.set_password(password)
        user.email = form.cleaned_data['email']
        user.contact = form.cleaned_data['contact']
        user.type = form.cleaned_data['type']
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'ecommerce/index.html')
    context = {
        "form": form,
    }
    return render(request, 'ecommerce/register.html', context)


def logout_user(request):
    logout(request)
    form = CustomUserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'ecommerce/login.html', context)
