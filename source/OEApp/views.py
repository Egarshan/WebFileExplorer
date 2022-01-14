from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.core.files.storage import FileSystemStorage
from .forms import FileForm, FolderForm
from .models import File, Folder
import os

class Home(TemplateView):
	template_name = 'home.html'


def folder_create(request):
	if request.method == 'POST':
		form = FolderForm(request.POST, request.FILES)
		#path_name = os.path.dirname("media/") 
		folder_name = os.path.dirname("media/") + '\\' + form.data.get('name')			#NEED MAKE NAME FROM FORM!!!
		os.mkdir(folder_name)
		if form.is_valid():
			form.save()
			return redirect('folder_create')
	else:
		form = FolderForm()
		return render(request, 'folder_create.html', {
			'form': form
	})


def folder_remove(request, pk):
	if request.method == 'POST':
		folder = Folder.objects.get(pk=pk)
		folder.delete()
		return redirect('file_list')


def file_list(request):
	if request.method == 'GET':
		files = File.objects.all()
		folders = Folder.objects.all()
		media_path = os.path.dirname("media/")
		storage_list = os.listdir(media_path)
		checker = 1

		if len(storage_list) != 0:
			for loc_doc in storage_list:
				for l_file in files:
					if l_file.path == loc_doc:
						checker = 0
						break
				if checker == 1:
					if os.path.isfile(media_path + '\\' + loc_doc):
						File.objects.create(path = loc_doc)
				else:
					checker = 1

				for l_folder in folders:
					if l_folder.name == loc_doc:
						checker = 0
						break
				if checker == 1:
					if os.path.isdir(media_path + '\\' + loc_doc):
						Folder.objects.create(name = loc_doc)
				else:
					checker = 1

		return render(request, 'file_list.html', {
			'files': files,
			'folders': folders
		})


def file_upload(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('file_upload')
	else:
		form = FileForm()
	form = FileForm()
	return render(request, 'file_upload.html', {
		'form': form
	})

def file_remove(request, pk):
	if request.method == 'POST':
		file = File.objects.get(pk=pk)
		file.delete()
		return redirect('file_list')
