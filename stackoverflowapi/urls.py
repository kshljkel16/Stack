
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import ProblemViewset, ReplyViewset, CommentViewset

router = DefaultRouter()
router.register('problems', ProblemViewset)
router.register('replies', ReplyViewset)
router.register('comments', CommentViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include('account.urls')),
    path('api/v2/', include(router.urls)),

]
