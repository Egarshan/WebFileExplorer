from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.Home, name = 'home'),
	path('start_page/', views.file_list, name = 'file_list'),
	path('new_file/', views.file_upload, name = 'file_upload'),
	path('files/<int:pk>/', views.file_remove, name = 'file_remove'),
	path('new_folder/', views.folder_create, name = 'folder_create'),
	path('new_folder/<int:pk>/', views.folder_remove, name = 'folder_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
