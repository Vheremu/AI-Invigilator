from django.contrib import admin
from .models import Sitting , Candidate , CandidateRequests
# Register your models here.
admin.site.register(Sitting)
admin.site.register(Candidate)
admin.site.register(CandidateRequests)
