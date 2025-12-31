from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('pastes/', views.create_paste, name='create_paste'),
    path('pastes/<uuid:paste_id>/', views.get_paste, name='get_paste'),
   
    

]
