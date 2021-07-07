from django.shortcuts import render
from .frm import userform
from django.http import HttpResponse
from django.shortcuts import render



def user_form(request):
    form = userform
    context = {'form': form}
    return render(request , "data/user-form.html" , context)
