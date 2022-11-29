from django.urls import path

from . import views


urlpatterns = [
    path('', views.apiOverview,name="blog-apiOverview"),
    path('myfeed/',views.getfeed,name="getfeed"),
    path('explore/',views.explore,name="explore"),
    path('createpost/',views.createpost,name="createpost"),
    path('updatelike/',views.updatelike,name="updatelike"),
    path('addreadlater/',views.addreadlater,name="addreadlater"),
    path('getreadlater/',views.getreadlater,name="getreadlater"),
    path('unfollow/<int:id>/',views.unfollow,name="unfollow"),
    path('follow/',views.follow,name="follow"),
    path('output/',views.output,name="output"),

]
