from django.urls import path
from text_to_speech.web.views import index


from . import views

urlpatterns = (
    path("", index, name="index"),

    # adding:
    path('download/<path:path>/', views.download, name='download'),
    path('add-money/', views.add_money, name='add_money'),
)
