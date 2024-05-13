from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student_Registration,Staff_Registration,Login_Info,Question,Answer,Commend,Reply,Saved_Items
# Register your models here.
admin.site.register(Student_Registration)
admin.site.register(Staff_Registration)
admin.site.register(Login_Info)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Commend)
admin.site.register(Reply)
admin.site.register(Saved_Items)






