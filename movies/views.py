from django.shortcuts import render
def post_list( request):
	return render(request, 'movies/post_list.html', {})

