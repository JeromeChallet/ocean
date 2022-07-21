from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView


def etechlab(request):
    return render(request,'etechlab/etechlab.html')