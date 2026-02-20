from django.shortcuts import render, redirect, get_object_or_404
from .models import Land


# 🏠 HOME PAGE
def home(request):
    query = request.GET.get('q')

    if query:
        lands = Land.objects.filter(title__icontains=query)
    else:
        lands = Land.objects.all()

    return render(request, 'land_app/index.html', {'lands': lands})


# ➕ POST LAND
def post_land(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        area = request.POST.get('area')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')

        Land.objects.create(
            title=title,
            description=request.POST.get('description'),
            owner_name=request.POST.get('owner_name'),
            owner_phone=request.POST.get('owner_phone'),
            price=price,
            area_sqft=area,
            image1=request.FILES.get('image1'),
            image2=request.FILES.get('image2'),
            image3=request.FILES.get('image3'),
            image4=request.FILES.get('image4'),
            image5=request.FILES.get('image5'),
            latitude=lat if lat else None,
            longitude=lon if lon else None
        )

        return redirect('home')

    return render(request, 'land_app/post_land.html')


# 🔍 LAND DETAIL PAGE
def land_detail(request, land_id):
    land = get_object_or_404(Land, id=land_id)
    return render(request, 'land_app/land_detail.html', {'land': land})


# 🛒 ADD TO CART
def add_to_cart(request, land_id):
    cart = request.session.get('cart', [])

    if land_id not in cart:
        cart.append(land_id)

    request.session['cart'] = cart
    return redirect('cart')


# 🛍 CART PAGE
def cart(request):
    cart_ids = request.session.get('cart', [])
    lands = Land.objects.filter(id__in=cart_ids)

    return render(request, 'land_app/cart.html', {'lands': lands})