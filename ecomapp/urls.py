from django.urls import path
from .import views
urlpatterns = [
    #Both
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contactdb',views.contactdb,name='contactdb'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('loginfunc',views.loginfunc,name='loginfunc'),
    path('signup',views.signup,name='signup'),
    path('signupdb',views.signupdb,name='signupdb'),
    #Admin
    path('adminhome',views.adminhome,name='adminhome'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('add_categorydb',views.add_categorydb,name='add_categorydb'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('add_productdb',views.add_productdb,name='add_productdb'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('show_user',views.show_user,name='show_user'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('viewcontact',views.viewcontact,name='viewcontact'),
    path('viewrequestbook',views.viewrequestbook,name='viewrequestbook'),
    path('admin_logout',views.admin_logout,name='admin_logout'),

    #User
    path('userhome',views.userhome,name='userhome'),
    path('edituser',views.edituser,name='edituser'),
    path('requestbook',views.requestbook,name='requestbook'),
    path('requestbookdb',views.requestbookdb,name='requestbookdb'),
    path('userproduct/<int:id>',views.userproduct,name='userproduct'),
    path('addcart/<int:pk>',views.addcart,name='addcart'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('remove/<item_id>',views.remove,name='remove')
]