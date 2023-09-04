from django.contrib import admin
from .models import Voter
from .models import Candidate
from .models import Vote

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('cid','cname','partyname','vote_count')

admin.site.register(Vote)
admin.site.register(Voter)
admin.site.register(Candidate,CandidateAdmin)
