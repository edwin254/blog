from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .models import Post ,Event, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView ,TemplateView,DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import ContactForm,LoginForm, SignUpForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#home view index page
class HomeView(TemplateView):
	template_name = 'base.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:6]
		context['gallery'] = Gallery.objects.all()[:4]
		return context


class PostList(ListView,LoginRequiredMixin):
	template_name = 'blog.html'
	context_object_name = 'posts'
	paginate_by = 3 # Show 10 posts per page

#Filter posts displayed by their category 
	def get_queryset(self,**kwargs):
		category = self.kwargs['category']

		if category is not 'all' and  not 'None':
			return Post.objects.filter(category= category)
		else:
			return Post.objects.all()

	def get_context_data(self, **kwargs):
		context = super(PostList, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:20]
		return context

class EventList(ListView):
	template_name = 'event_list.html'
	context_object_name= "events"
	paginate_by = 10

	def get_queryset(self):
		return Event.objects.all()

	def get_context_data(self, **kwargs):
		context = super(EventList, self).get_context_data( **kwargs)
		context['posts'] = Post.objects.all()[:20]
		return context

class GalleryList(ListView):
	template_name = "gallery.html"
	context_object_name = 'gallery'

	def get_queryset(self):
		return Gallery.objects.all()

	def get_context_data(self, **kwargs):
		context = super(GalleryList, self).get_context_data( **kwargs)
		context['posts'] = Post.objects.all()[:7]
		return context

#Model Details view

class PostDetail(DetailView):
	queryset = Post.objects.all()
	template_name = 'post_detail.html'
	context_object_name = "post"

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data( **kwargs)  
		context['posts'] = Post.objects.all()[:7]
		return context

class EventDetail(DetailView):
	model = Event
	template_name = 'event_detail.html'
	context_object_name = "event"

	def get_context_data(self, **kwargs):
		context = super(EventDetail, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:5]
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
	form_class = ContactForm

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name, {"form":form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			from_email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			try:
				send_mail(subject, message, from_email, [' '])

			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			messages.error(request, "MESSAGE SENT SUCCESSFULLY.")
			messages.error(request, "Thank you for your feedback.")
			return redirect('/contact')

		else:
			messages.error(request, "Please dont Leave fields blank.")
			return render(request,self.template_name,{"form":form})




class AboutView(TemplateView):
	template_name = 'about.html'

	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data( **kwargs)
		context['posts'] = Post.objects.all()[:5]
		return context



#logout view
# class UserLogoutView(TemplateView):
# 	template_name = 'login.html'

# 	def get(self, request):
# 		logout(self.request)
# 		messages.error(request, "Successfully Logged out.")
# 		return redirect('blog:login')



# user  login view
# class UserLoginView(TemplateView):

# 	form_class = LoginForm
# 	template_name = 'login.html'

# 	def get(self,request):
# 		form = self.form_class(None)
# 		return render(request, self.template_name,{"form":form})

# 	def post(self,request):
# 		form = self.form_class(request.POST or None)

# 		if form.is_valid():

# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']

# 			user = authenticate(username= username, password= password)

# 			if user:
# 				if user.is_active:
# 					login(request,user)
# 					messages.success(request, " Welcome to HerVoiceMatters %s" %(user.username))
# 					return redirect('blog:home')
# 				else:
# 					messages.info(request, " Your account is not active, Please contact the admin" )
# 					return render(request, self.template_name,{"form":form})
# 			else:
# 				messages.error(request, " You are not a registered user or you used wrong information")
# 				return render(request, self.template_name, {"form":form})
# 		else:
# 			messages.error(request, "Please dont Leave fields blank.")
# 			return render(request, self.template_name, {"form":form})


# #signup view
# class SignUpView(CreateView):

# 	form_class = SignUpForm
# 	template_name = 'signup.html'

# 	def get(self,request):
# 		sign_form = self.form_class(None)
# 		return render(request, self.template_name,{"form":sign_form})

# 	def post(self,request):
# 		form = self.form_class(request.POST or None)

# 		if form.is_valid():
# 			new_user = form.save(commit = False )

# 			username = form.cleaned_data['username']
# 			email = form.cleaned_data['email']
# 			password = form.cleaned_data['password']
# 			password2 = form.cleaned_data['password2']

# 			#check whether username exists
# 			user,created = User.objects.get_or_create(username = username, email = email)

# 			if user and not created:
# 				messages.error(request, " The username already exist,Please choose a different one")
# 				return render(request, self.template_name, {"form":form})

# 			if len(password) >= 8:
# 				if password == password2:
# 					new_user.set_password(password)
# 					new_user.save()
# 				else:
# 					messages.error(request, " Please make sure both passwords match")
# 					return render(request, self.template_name, {"form":form})
# 			else:
# 			    messages.error(request, "your Password should be 8 characters or longer")
# 			    return render(request, self.template_name, {"form":form})

# 			return redirect('blog:login')

# 		else:
# 			return render(request, self.template_name, {'form':form})







	