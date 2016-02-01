from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def ahs_detail(request, id=None): #retrieve
	# instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post,slug=slug)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)


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
