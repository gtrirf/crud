from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def home_page(request):
    return render(request, 'home.html')


class GetTest(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'get_test.html')
        else:
            return redirect('')