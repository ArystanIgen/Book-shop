from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', views.BookViewSet, basename='book')
router.register('journals', views.JournalViewSet, basename='book')
app_name = "book"
urlpatterns = [

]
urlpatterns += router.urls