from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import AHS, AHS_Detail
from setting_proyek.models import Proyek


# Create your views here.
@login_required(login_url='/login/')
def ahs_detail(request, id=None): #retrieve
	#instance = Post.objects.get(id=1)
	data_proyek_query = Proyek.objects.get(id=id)
	data_ahs_query = AHS.objects.filter(nomor_proyek_id=id)
	detail_ahs_query = AHS.objects.filter(data_ahs_query)
	# 	instance = get_object_or_404(AHS,id=id)
	# share_string = quote_plus(instance.content)
	context = {
		"data_proyek": data_proyek_query,
		 "data_ahs": data_ahs_query,
		 "detail_ahs_query": detail_ahs_query,
	}
	
	return render(request, "ahs/ahs_list.html", context)


def ahs_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")
	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	if request.user.is_authenticated():
		context = {
			"object_list": queryset,
			"title": "List"
		}
	else:
		context = {
			"title": "List"
		}
	return render(request, "post_list.html", context)

def ahs_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Failed Created")

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def ahs_update(request, slug=None):
	instance = get_object_or_404(Post,slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Updated", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}

	return render(request, "post_form.html", context)

def ahs_delete(request, id_detail=None):
	instance = get_object_or_404(Post,id=id_detail)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")

