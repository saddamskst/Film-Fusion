from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from ContactPage.models import *
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def error_page(request,exception):
	return render(request,"notfound404.html")

def home(request):
	return render(request,'index.html')

def detail(request):
	return render(request,'detail.html')

def movielist(request):
	return render(request,'movie-list.html')

def team(request):
	return render(request,'about.html')

def contact(request):
	try:
		if request.method=="POST":
			x=Contact_List()
			x.Name=request.POST['name']
			x.Email=request.POST['email']
			x.Phone=request.POST['phone']
			x.Message=request.POST['message']
			print(request.POST['name'])
			x.save()
			return redirect('/')
		else:
			return redirect('/contact')
			
	       
	except Exception as e:
		return HttpResponse(e)

					   
	return render(request,'contact.html')

# def signup(request):
# 	return render(request,'signup.html')






def login(request):
	try:
		if request.user.is_authenticated:
			return  redirect('')

		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['pass']

			print(email)
			print(password)

			user=authenticate(request,username=email,password=password)

			if user is not None:
				auth_login(request,user)
				messages.success(request,"Successfully Login")
				return redirect('/')
			else:
				messages.error(request,"Something Went Wrong")
				return redirect('/login')
		return render(request,'log.html')
	except Exception as e:
		return HttpResponse(e)

	

def signup(request):
	try:
		if request.user.is_authenticated:

			return  redirect('')

		if request.method == 'POST':
			name = request.POST['name']
			
			email = request.POST['email']
			password = request.POST['pass']
			cpassword = request.POST['Cpass']
			#print(name,email,password,cpassword)
			#messages(name,email,password,cpassword)

			
			email_check = User.objects.filter(username=email).exists()
			
			
			if email_check == True:
				messages.error(request,"Your Number  Already Exists")
				return redirect('/signup')
			else:
			# if email_check == True:
			# 	messages.error(request,"Your Email Already Exists")
			# 	return redirect('/signup')


			# if len(phone) != 10:
			# 	messages.error(request,'phone number Should Be 10 Digit')
			# 	return redirect('/signup')
			
			# elif password != cpassword:
			# 	messages.error(request,"Password And Confirm Did'nt Match")
			# 	return redirect('/signup')

			# else:
				users = User.objects.create_user(username=email,password=cpassword)
				users.first_name = name

				users.save()
				messages.success(request,"Your Account Successfully Created")
				return redirect('/login')


		return render(request,'signup.html')
	except Exception as e:
		return HttpResponse(e)
		


def logout(request):
	auth_logout(request)
	messages.success(request,"Logout Successfully")
	return redirect('/login')





		
