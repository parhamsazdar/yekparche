from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    path('create_file/', views.FileCreate.as_view(), name="create_file"),
    path('handle_come/<int:pk>', views.SeminarCustomerCome.as_view(), name='handle_come_bool'),
    path('seprate_backup/<int:pk>',views.SeminarCustomerBackup.as_view(),name='seprate_backup'),

]
