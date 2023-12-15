from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from ecomapp.models import Category,Product,Usermember,cart1,Contact,Book
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import os

# Create your views here.

def home(request):
    category=Category.objects.all()
    return render(request,'home.html',{'category':category})

def about(request):
    category=Category.objects.all()
    return render(request,'about.html',{'category':category})

def contact(request):
    category=Category.objects.all()
    return render(request,'contact.html',{'category':category})

def contactdb(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        subject=request.POST['subject']
        message=request.POST['message']
        contacts=Contact(name=name,email=email,number=number,subject=subject,message=message)
        contacts.save()
        return redirect('contact')
    
def viewcontact(request):
    contact=Contact.objects.all()
    return render(request,'viewmessages.html',{'contact':contact})



def loginpage(request):
    category=Category.objects.all()
    return render(request,'loginpage.html',{'category':category})

def loginfunc(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,f'Welcome {username}')
                return redirect('adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.success(request,f'Welcome {username}')
                return redirect('userhome')
        else:
            messages.info(request,'Invalid Username or Password. Try Again.')
            return redirect('loginpage')
    else:
        return render(request,'loginpage.html')

@login_required(login_url='loginfunc')
def adminhome(request):
    return render(request,'adminhome.html')

@login_required(login_url='loginpage')
def addcategory(request):
    return render(request,'addcategory.html')

def add_categorydb(request):
    if request.method=="POST":
        category=request.POST['category']
        category=Category(category=category)
        category.save()
        messages.info(request,'Category Added')
        return redirect('addcategory')
    
@login_required(login_url='loginfunc')    
def addproduct(request):
    categories=Category.objects.all()
    return render(request,'addproduct.html',{'category':categories})

def add_productdb(request):
    if request.method=='POST':
        product=request.POST['product']
        author=request.POST['author']
        price=request.POST['price']
        sel=request.POST['sel']
        category1=Category.objects.get(id=sel)
        image=request.FILES.get('file')
        products=Product(product=product,author=author,price=price,category=category1,image=image)
        products.save()
        messages.info(request,'Product Added Successfully')
        return redirect('addproduct')

@login_required(login_url='loginfunc')   
def showproduct(request):
    product=Product.objects.all()
    return render(request,'showproduct.html',{'products':product})

def deletepage(request,pk):
    prd=Product.objects.get(id=pk)
    prd.delete()
    return redirect('showproduct')

@login_required(login_url='loginfunc')    
def admin_logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    category=Category.objects.all()
    return render(request,'signup.html',{'category':category})

def signupdb(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        email=request.POST.get('email')
        address=request.POST.get('address')
        number=request.POST.get('number')
        image=request.FILES.get('file')
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This Username is already exist!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
                user.save()

                member=Usermember(address=address,number=number,image=image,user=user)
                member.save()
                # subject='Greeting From St Marys College'
                # message='Congratulations, \nYour staff registration successfully completed \nYour login credentials \n \nUsername: '+uname+'\n'+'Password: '+password
                # send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
                return redirect('loginpage')
        else:
            messages.info(request,'Password doesnt Match!!!')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    
@login_required(login_url='loginfunc')
def show_user(request):
    user1=Usermember.objects.all()
    return render(request,'viewusers.html',{'user':user1})

def delete(request,pk):
    user=Usermember.objects.get(id=pk)
    if user.image:
        user.image.delete()
    user.delete()
    user.user.delete()
    return redirect('show_user')

@login_required(login_url='loginpage')
def userhome(request):
    category=Category.objects.all()
    current_user=request.user.id
    user1=Usermember.objects.get(user_id=current_user)
    return render(request,'userhome.html',{'category':category, 'users':user1})

@login_required(login_url='loginfunc')  
def edituser(request):
    category=Category.objects.all()
    current_user=request.user.id
    user1=Usermember.objects.get(user_id=current_user)
    user2=User.objects.get(id=current_user)
    if request.method=='POST':
        user2.first_name=request.POST.get('fname')
        user2.last_name=request.POST.get('lname')
        user2.email=request.POST.get('email')
        user1.address=request.POST.get('address')
        user1.number=request.POST.get('number')
        if len(request.FILES)!=0:
            if len(user1.image)>0:
                os.remove(user1.image.path)
            user1.image=request.FILES.get('file')
        user1.save()
        user2.save()
        return redirect('userhome')
    return render(request,'edit.html',{'users':user1,'category':category}) 

@login_required(login_url='loginfunc') 
def requestbook(request):
    category=Category.objects.all()
    current_user=request.user.id
    user1=Usermember.objects.get(user_id=current_user)
    return render(request,'requestbook.html',{'category':category, 'users':user1})

def requestbookdb(request):
    if request.method=='POST':
        isbn=request.POST['isbn']
        title=request.POST['title']
        author=request.POST['author']
        qty=request.POST['qty']
        email=request.POST['email']
        number=request.POST['number']
        books=Book(isbn=isbn,title=title,author=author,quantity=qty,email=email,number=number)
        books.save()
        return redirect('requestbook')
    return render(request,'requestbook.html')

def viewrequestbook(request):
    books=Book.objects.all()
    return render(request,'viewrequestbook.html',{'book':books})


def userproduct(request,id):
    if request.user.is_authenticated:
        category=Category.objects.all()
        cat=Category.objects.get(id=id)
        current_user=request.user.id
        user1=Usermember.objects.get(user_id=current_user)
        product=Product.objects.all().filter(category_id=id)
        return render(request,'userproducts.html',{'category':category, 'cat':cat, 'users':user1,'product':product})
    else:
        product=Product.objects.all().filter(category_id=id)
        category=Category.objects.all()
        cat=Category.objects.get(id=id)
        return render(request,'commonproduct.html',{'category':category, 'cat':cat, 'product':product})

@login_required(login_url='loginfunc')
def addcart(request, pk):
    product = Product.objects.get(id=pk)
    cartitem,created= cart1.objects.get_or_create(product=product,user=request.user)
    if not created:
        cartitem.quantity += 1
    cartitem.save()
    return redirect('view_cart')

@login_required(login_url='loginfunc')
def view_cart(request):
    cart_items = cart1.objects.filter(user=request.user)
    each_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items=sum([item.quantity for item in cart_items])
    if each_price>0:
        amount=(117+each_price)
    else:
        amount=0
    current_user=request.user.id
    user1=Usermember.objects.get(user_id=current_user)
    category=Category.objects.all()
    return render(request,'cart.html',{'cart_items':cart_items,'each_price':each_price, 'total_items':total_items,'users':user1,'amount':amount,'category':category})

def remove(request, item_id):
    cart_item = cart1.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')