from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, PropertyPostForm, FilterResultsForm
from .models import Properties, Comments, ImageElement
import time


def index(request):
    return render(request, 'ecommerce/index.html')


def detail(request):
    form = FilterResultsForm(request.POST or None)
    search = request.GET['q']
    properties = get_list_or_404(Properties, locality=search)
    images = []
    images_filter = []
    for property in properties:
        images.append(ImageElement.objects.filter(post=property).first())

    if request.method == 'POST':
        if request.POST['sort_filter'] == "filter":
            property_type = request.POST['property_type']
            bhk = request.POST['BHK']
            price = request.POST['price']
            construction_status = request.POST['construction_status']
            area = request.POST['area']

            if property_type != 'No Preference':
                if bhk != 'No Preference':
                    if price != 'No Preference':
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price)
                    else:
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk)
                else:
                    if price != 'No Preference':
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type, price=price,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type, price=price,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type, price=price,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type, price=price)
                    else:
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type)
            else:
                if bhk != 'No Preference':
                    if price != 'No Preference':
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk, price=price)
                    else:
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    property_type=property_type,
                                                                    BHK=bhk)
                else:
                    if price != 'No Preference':
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search, price=price,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search, price=price,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search, price=price,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search, price=price)
                    else:
                        if construction_status != 'No Preference':
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    construction_status=construction_status,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    construction_status=construction_status)
                        else:
                            if area != 'No Preference':
                                properties_filter = get_list_or_404(Properties, locality=search,
                                                                    area=area)
                            else:
                                properties_filter = get_list_or_404(Properties, locality=search)



            for property in properties_filter:
                images_filter.append(ImageElement.objects.filter(post=property).first())

            return render(request, 'ecommerce/detail.html', {'properties': properties_filter, 'images': images_filter,
                                                             'form': form})

        elif request.POST['sort_filter'] == "sort":
            value = request.POST['sort']
            if value == 'relevance':
                images = sorted(images, key=lambda image: image.post.property_title)
            elif value == 'price_low_to_high':
                images = sorted(images, key=lambda image: image.post.price)
            elif value == 'price_high_low':
                images = reversed(sorted(images, key=lambda image: image.post.price))
            elif value == 'sqft_low_high':
                images = sorted(images, key=lambda image: image.post.area)
            elif value == 'sqft_high_low':
                images = reversed(sorted(images, key=lambda image: image.post.area))
            elif value == 'latest':
                images = reversed(sorted(images, key=lambda image: image.post.post_date_time))

            return render(request, 'ecommerce/detail.html', {'properties': properties, 'images': images, 'form': form})

    return render(request, 'ecommerce/detail.html', {'properties': properties, 'images': images, 'form': form})


def property_detail(request, pk):
    property_obj = get_object_or_404(Properties, pk=pk)
    comments = Comments.objects.filter(property_title=property_obj.property_title)
    images = ImageElement.objects.filter(post=property_obj)

    if request.method == 'POST':
        if request.POST.get('a', False):
            com = Comments()
            com.user = request.user
            com.property_title = property_obj.property_title
            com.datetime = str(time.asctime(time.localtime(time.time())))
            com.comment = request.POST['a']
            com.save()
        else:
            message = str(request.user.first_name) + str(
                request.user.last_name) + 'visited your profile.\nTheir contact: ' + str(property_obj.user.contact)
            send_mail('Your post on REES has a visitor', message, 'rohan.jagtap@spit.ac.in', [property_obj.user.email],
                      fail_silently=False)

    return render(request, 'ecommerce/property_detail.html',
                  {'property': property_obj, 'comments': comments, 'images': images})


def post_property(request):
    i = 1
    form = PropertyPostForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.user.is_authenticated and (
            request.user.type == "seller" or request.user.type == "lessor"):
        property_obj = form.save(commit=False)
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
