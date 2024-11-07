import razorpay
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from.models import*

# Create your views here.

def index(request):
        b = tbl_Products.objects.all()
        a = tbl_add_blog.objects.all()
        return render(request, 'index.html', {"b": b,"a":a})
def admin_login(request):
        return render(request,'admin_login.html')

def check_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/admin_homepage/")
        else:
            return redirect("/admin_login/")

def admin_homepage(request):
      return render(request, 'admin_homepage.html')


def add_category(request):
    return render(request, 'add_category.html')

def save_category(request):
    if request.method == "POST":
        obj = tbl_category()
        obj.category_name = request.POST.get("category_name")
        category_image = request.FILES['category_image']
        fs=FileSystemStorage()
        file=fs.save(category_image.name,category_image)
        url=fs.url(file)
        obj.category_image=url
        obj.save()
        return redirect("/add_category/")

def view_category(request):
    a = tbl_category.objects.all()
    return render(request, "view_category.html", {"a": a})

def edit_category(request,id):
    b = tbl_category.objects.get(id=id)
    return render(request, "edit_category.html", {"b": b})

def update_category(request,id):
    b = tbl_category.objects.get(id=id)
    b.category_name = request.POST.get("category_name")
    try:
        category_image = request.FILES['category_image']
        fs = FileSystemStorage()
        file = fs.save(category_image.name,category_image)
        url = fs.url(file)
        b.category_image = url
    except:
        pass
    b.save()
    return redirect("/view_category/")

def delete_category(request,id):
    b = tbl_category.objects.get(id=id)
    b.delete()
    return redirect("/view_category/")

def add_subcategory(request):
    d=tbl_category.objects.all()
    return render(request, 'add_subcategory.html',{"d":d})

def save_subcategory(request):
    if request.method == "POST":
        obj = tbl_subcategory()
        obj.category_id = request.POST.get("category")
        obj.subcategory_name = request.POST.get("subcategory_name")
        subcategory_image = request.FILES['subcategory_image']
        fs=FileSystemStorage()
        file=fs.save(subcategory_image.name,subcategory_image)
        url=fs.url(file)
        obj.subcategory_image=url
        obj.save()
        return redirect("/add_subcategory/")

def view_subcategory(request):
    a = tbl_subcategory.objects.all()
    return render(request, "view_subcategory.html", {"a": a})

def edit_subcategory(request,id):
    d = tbl_category.objects.all()
    b = tbl_subcategory.objects.get(id=id)
    return render(request, "edit_subcategory.html", {"b": b,"d":d})

def update_subcategory(request,id):
    b = tbl_subcategory.objects.get(id=id)
    b.category_id = request.POST.get("category")
    b.subcategory_name = request.POST.get("subcategory_name")
    try:
        subcategory_image = request.FILES['subcategory_image']
        fs = FileSystemStorage()
        file = fs.save(subcategory_image.name,subcategory_image)
        url = fs.url(file)
        b.subcategory_image = url
    except:
        pass
    b.save()
    return redirect("/view_subcategory/")


def delete_subcategory(request, id):
    b = tbl_subcategory.objects.get(id=id)
    b.delete()

    return redirect("/view_subcategory/")
def add_products(request):
    d=tbl_subcategory.objects.all()
    return render(request, 'add_products.html',{"d":d})


def save_products(request):
    if request.method == "POST":
        obj = tbl_Products()
        obj.name  = request.POST.get("name")
        obj.description = request.POST.get("description")
        obj.grams = request.POST.get("grams")
        obj.pieces = request.POST.get("pieces")
        obj.serves = request.POST.get("serves")
        obj.market_price = request.POST.get("market_price")
        obj.our_price = request.POST.get("our_price")
        image = request.FILES["image"]
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        url=fs.url(file)
        obj.image=url
        obj.sub_category_id=request.POST.get("sub_category")
        obj.save()
        return redirect("/add_products/")


def view_products(request):
    a = tbl_Products.objects.all()
    return render(request, "view_products.html", {"a": a})

def edit_products(request,id):
    a = tbl_subcategory.objects.all()
    b = tbl_Products.objects.get(id=id)
    return render(request, "edit_products.html",{"a":a,"b":b} )

def update_products(request,id):
    b = tbl_Products.objects.get(id=id)
    b.name = request.POST.get("name")
    b.description = request.POST.get("description")
    b.grams = request.POST.get("grams")
    b.pieces = request.POST.get("pieces")
    b.serves = request.POST.get("serves")
    b.market_price = request.POST.get("market_price")
    b.our_price = request.POST.get("our_price")
    b.image = request.FILES["image"]
    try:
        image = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(image.name,image)
        url = fs.url(file)
        b.image = url
        b.sub_category_id = request.POST.get("sub_category")
    except:
        pass
    b.save()
    return redirect("/view_products/")

def delete_products(request, id):
    b = tbl_Products.objects.get(id=id)
    b.delete()
    return redirect("/view_products/")

def products(request):
    a = tbl_Products.objects.all()
    b = tbl_category.objects.all()
    return render(request, 'products.html',{"a":a,"b":b})

def items(request,id):
    g=tbl_category.objects.get(id=id)
    b = tbl_subcategory.objects.filter(category=id)
    d = tbl_Products.objects.filter(sub_category__category=id)
    return render(request, 'items.html', {"b":b, "d":d,"g":g})


def sub_items(request,id):
    g=tbl_subcategory.objects.get(id=id)
    c = tbl_Products.objects.filter(sub_category=id)
    return render(request, 'sub_items.html', {"c": c,"g":g})


razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG', 'oXUZ9Mf5zhjoZsTFLc7RpABO'))
def buy_now(request,id):
    a = tbl_Products.objects.get(id=id)
    currency = "INR"
    amount = int(a.our_price)*100
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'payment_handler'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_amount'] = amount
    context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['a'] = a
    return render(request, 'buy_now.html', context)

def payment_handler(request,id):
    print("hiii")
    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.


    amount = request.POST.get("amount") # Rs. 200
    razorpay_client.payment.capture(payment_id, amount)
    obj = tbl_buy_now()
    obj.first_name = request.POST.get("fname")
    obj.last_name = request.POST.get("lname")
    obj.country = request.POST.get("selection")
    obj.street_address = request.POST.get("houseadd")
    obj.town_city = request.POST.get("city")
    obj.state_country = request.POST.get("state")
    obj.zip = request.POST.get("zip")
    obj.phone = request.POST.get("phone")
    obj.email = request.POST.get("email")
    obj.product_id = id
    obj.save()

    return redirect("/")



def sign_up(request,id):
    a = tbl_Products.objects.get(id=id)
    return render(request, 'sign_up.html',{"a": a})


def save_sign_up(request,id):
    if request.method == "POST":
        obj = tbl_sign_up()
        obj.full_name = request.POST.get("name")
        obj.email = request.POST.get("email")
        obj.password = request.POST.get("password")
        obj.save()
        return redirect("buy_now",id=id)

def logincheck(request,id):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if tbl_sign_up.objects.filter(full_name=username,password=password).exists():
        v=tbl_sign_up.objects.get(full_name=username,password=password)
        request.session['userid']=v.id
        return redirect("buy_now",id=id)
    else:
        return redirect("sign_up", id=id)
def logincheck_cart(request,cart_total):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if tbl_sign_up.objects.filter(full_name=username, password=password).exists():
        v = tbl_sign_up.objects.get(full_name=username, password=password)
        request.session['userid'] = v.id
        return redirect("proceed_to_checkout", cart_total=cart_total )

def add_to_cart(request, id):
    # Get the product or return a 404 if it doesn't exist
    product = get_object_or_404(tbl_Products, id=id)

    # Ensure the session exists
    if not request.session.session_key:
        request.session.create()

    # Fetch the session key after ensuring it's created
    session_key = request.session.session_key

    # Get or create the cart object for the session and product
    cart, created = tbl_cart.objects.get_or_create(session_key=session_key, product_id=id)

    # If the cart already existed, increment the quantity
    if not created:
        cart.quantity += 1
        cart.save()
    else:
        cart.quantity=1
        cart.save()

    return redirect('/cart/')
def decrease_quantity(request,id):
    session_key = request.session.session_key
    cart = tbl_cart.objects.get(session_key=session_key, product_id=id)

    # If the cart already existed, increment the quantity

    cart.quantity -= 1
    cart.save()
    return redirect('/cart/')



def cart(request):
    a = tbl_cart.objects.filter( session_key = request.session.session_key)
    cart_total=sum(i.get_total() for i in a)
    return render(request, 'cart.html',{"a": a,"cart_total":cart_total})



def remove_cart(request, id):
    b = tbl_cart.objects.get(id=id)
    b.delete()
    return redirect("/cart/")


razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG', 'oXUZ9Mf5zhjoZsTFLc7RpABO'))
def proceed_to_checkout(request,cart_total):
    currency = "INR"
    cart_total=float(cart_total)
    amount = int(cart_total) * 100
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    callback_url = 'save_checkout'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_amount'] = amount
    context['razorpay_merchant_key'] = 'rzp_test_9zruMnoLDlsCLG'
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['cart_total']=cart_total
    return render(request, 'proceed_to_checkout.html',context)

def process_checkout(request):
    print("hiii")
    obj=tbl_checkout()
    obj.first_name = request.POST.get("firstname")
    obj.last_name = request.POST.get("lastname")
    obj.country = request.POST.get("country")
    obj.street_address = request.POST.get("address")
    obj.town_city = request.POST.get("city")
    obj.state_country = request.POST.get("state")
    obj.zip = request.POST.get("zip")
    obj.phone = request.POST.get("phone")
    obj.email = request.POST.get("email")
    obj.cart_total=request.POST.get("cart_total")
    obj.save()
    v= tbl_cart.objects.filter( session_key = request.session.session_key)
    for i in v:
        ob=tbl_checkout_products()
        ob.product=i.product
        ob.user_id=request.session['userid']
        ob.quantity=i.quantity
        ob.check_out=obj
        ob.save()



    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.


    amount = request.POST.get("amount") # Rs. 200
    razorpay_client.payment.capture(payment_id, amount)
    v= tbl_cart.objects.filter( session_key = request.session.session_key)
    v.delete()

    return redirect('/')

def single_products(request):
    a = tbl_buy_now.objects.all()
    return render(request, "single_products.html", {"a": a})

def multiple_products(request):
    a = tbl_checkout.objects.all()
    return render(request, "multiple_products.html", {"b": b})


def checkout_products(request,id):
    b = tbl_checkout_products.objects.filter(checkout=id)
    return render(request, "checkout_products.html", {"b": b})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def save_contact(request):
    if request.method == "POST":
        obj = tbl_contact()
        obj.name = request.POST.get("name")
        obj.email = request.POST.get("email")
        obj.phone = request.POST.get("phone")
        obj.message = request.POST.get("message")
        obj.save()
        return redirect("/")

def view_list(request):
    a = tbl_contact.objects.all()
    return render(request, "view_list.html",{"a": a})

def blog(request):
    a = tbl_add_blog.objects.all()
    return render(request, 'blog.html',{"a":a})

def add_blog(request):
    return render(request, 'add_blog.html')

def save_blog(request):
    if request.method == "POST":
        obj = tbl_add_blog()
        obj.blog_title = request.POST.get("title")
        obj.blog_content = request.POST.get("content")
        obj.save()
        return redirect("/admin_homepage/")

def view_blog(request):
    a = tbl_add_blog.objects.all()
    return render(request, 'view_blog.html',{"a": a})

def edit_blog(request,id):
    b = tbl_add_blog.objects.get(id=id)
    return render(request,"edit_blog.html",{"b":b})

def update_blog(request,id):
    b = tbl_add_blog.objects.get(id=id)
    b.blog_title = request.POST.get("title")
    b.blog_content = request.POST.get("content")
    b.save()
    return redirect("/admin_homepage/")

def delete_blog(request,id):
    b = tbl_add_blog.objects.get(id=id)
    b.delete()
    return redirect("/view_blog/")



























