from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Tweet
from .forms import TweetModelForm 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TweetDetailView(DetailView):
	"""docstring for TweetDetailView"""
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get('pk')
	# 	print(pk)
	# 	return Tweet.objects.get(id=pk)

class TweetListView(ListView):
	queryset = Tweet.objects.all()
	

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		# print(context)
		return context


		
class TweetCreateView(LoginRequiredMixin ,CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/forms.html'
	success_url='/tweets/create'

	def form_valid(self, form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user
			return super(TweetCreateView, self).form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/tweets_update.html'
	success_url = '/tweets/'
	print('------------------------------------------------------')
	def a(self):
		print(self.request.user)
		return super(TweetUpdateView, self).a()
