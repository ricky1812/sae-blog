from django.urls import path
from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from website import settings

urlpatterns=[
				path('',views.home,name='home'),
				path('signup/',views.signup,name='signup'),
				path('login/',views.login_view,name='login'),
				path('update/',views.update_profile,name='update'),
				path('posts/',views.post_list,name='post_list'),
				path('create_post/',views.create_post,name='create_post'),
				path('posts/<key>/',views.post_details,name='post_details'),
				path('posts/<key>/confirm_delete/',views.confirm_delete,name='confirm_delete'),
				path('posts/<key>/confirm_delete/deleted',views.post_delete,name='post_delete'),
				path('posts/<key>/create_comment',views.create_comment,name='create_comment'),
				path('posts/<key>/likes',views.create_like,name='likes'),
			]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
