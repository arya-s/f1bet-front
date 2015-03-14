from django.contrib import admin

from f1betcore.models import RedditUser, Team, Driver, DriverShort, Race, Bet

admin.site.register(RedditUser)
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(DriverShort)
admin.site.register(Race)
admin.site.register(Bet)