from django.shortcuts import render

# Create your views here.

def showMain(request):
	return render(request, 'main/about.html')

def showReports(request):
	return render(request, 'main/service.html')

def showOutreach(request):
	return render(request, 'main/blog-item.html')

def showHome(request):
	return render(request, 'main/index.html')

def showNews(request):
	return render(request, 'main/blog.html')