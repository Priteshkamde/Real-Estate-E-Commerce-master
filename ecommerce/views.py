from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from .models import Properties, Comments
import time


def index(request):
    return render(request, 'ecommerce/index.html')


def detail(request):
    search = request.GET['q']
    properties = get_list_or_404(Properties, locality=search)
    return render(request, 'ecommerce/detail.html', {'properties': properties})


def property_detail(request, pk):
    property_obj = get_object_or_404(Properties, pk=pk)
    comments = Comments.objects.all()
    if request.method == 'POST':
        com = Comments()
        com.user = request.user
        com.property_title = property_obj.property_title
        com.datetime = str(time.asctime(time.localtime(time.time())))
        com.comment = request.POST['a']
        com.save()
    return render(request, 'ecommerce/property_detail.html', {'property': property_obj, 'comments': comments})


def post_property(request):
    if request.method == "POST" and request.user.is_authenticated and request.user.type == "seller":
        property_obj = Properties()
        property_obj.user = request.user
        property_obj.property_title = request.POST['m']
        property_obj.buy_rent = request.POST['p']
        property_obj.locality = request.POST['q']
        property_obj.property_type = request.POST['r']
        property_obj.price = int(request.POST['s'])
        if request.POST['t'] is not None:
            property_obj.BHK = request.POST['t']
        else:
            property_obj.BHK = '0'
        property_obj.construction_status = request.POST['u']
        property_obj.area = int(request.POST['v'])
        property_obj.address = request.POST['w']
        property_obj.description = request.POST['x']
        property_obj.save()

    return render(request, 'ecommerce/post_property.html')


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
