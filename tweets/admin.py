from django.contrib import admin

# Register your models here.
from .forms import TweetModelForm
from .models import Tweet



class TweetModelAdmin(admin.ModelAdmin):
	#sform = TweetModelForm
	class Meta:
		model = Tweet
		


admin.site.register(Tweet, TweetModelAdmin)