
from django.urls import path,include
from. import views
app_name='cartoonapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('cartoon/<int:cartoon_id>/',views.detail,name='detail'),
    path('add/',views.add_cartoon,name='add_cartoon'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]