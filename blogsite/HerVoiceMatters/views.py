from django.shortcuts import render,redirect,get_object_or_404
from .models import Post ,Event, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView ,TemplateView,DetailView
from django.contrib.auth.models import User
from .forms import ContactForm

# Create your views here.
#home view index page
class HomeView(TemplateView):
	template_name = 'base.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:6]
		return context


class PostList(ListView):
	template_name = 'blog.html'
	context_object_name = 'posts'
	paginate_by = 3 # Show 25 contacts per page

#Filter posts displayed by their category 
	def get_queryset(self,request,*args,**kwargs):
		category = self.request.GET.get('category',' ')

		if category == 'women_talk':
			return Post.objects.filter(category = 'girl')
		elif category =='fashion':
			return Post.objects.filter(category = 'fas')
		elif category == 'food':
			return Post.objects.filter(category = 'food')
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
	template_name = "gallery_list.html"
	context_object_name = 'galleries'

	def get_queryset(self):
		return Gallery.objects.all()

	def get_context_data(self, **kwargs):
		context = super(GalleryList, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:2]
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
	model = Post
	template_name = 'event_detail.html'
	context_object_name = "event"

	def get_context_data(self, **kwargs):
		context = super(EventDetail, self).get_context_data( **kwargs)
		context['events'] = Event.objects.all()[:2]
		context['posts'] = Post.objects.all()[:7]
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
	form_class = 'ContactForm'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name, {"form":form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			pass

			# username = form.cleaned_data['username']
			# email = form.cleaned_data['email']





