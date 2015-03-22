from django.conf.urls import url, include
from django.contrib import admin
from f1betcore.models import RedditUser, Team, Driver, DriverShort, Race, Bet
from rest_framework import serializers, viewsets, routers

class RedditUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RedditUser
        fields = ('url', 'name', 'flair', 'last_active', 'points')

class RedditUserViewSet(viewsets.ModelViewSet):
    queryset = RedditUser.objects.all()
    serializer_class = RedditUserSerializer


router = routers.DefaultRouter()
router.register(r'users', RedditUserViewSet)

urlpatterns = [
    url(r'^', include('f1betcore.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]