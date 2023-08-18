from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import CreateView,View,FormView
from.models import User
from .forms import DoctorSignupForm,PatientSignupForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

class Dashboard(View):
    def get(self,r):
        data = {
            "user" : User.objects.get(pk=r.user.id)
            
        }
        return render(r,"dashboard.html",data)
class DoctorView(CreateView):
    model = User
    form_class = DoctorSignupForm
    template_name = "signup/register.html"



    def get_context_data(self,**kwargs):
        kwargs['user_type'] = "doctor"
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return render("dashboard.html")



class PatientView(CreateView):
    model = User
    form_class = PatientSignupForm
    template_name = "signup/register.html"

    def get_context_data(self,**kwargs):
        kwargs['user_type'] = "patient"
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect("dashboard")
        


class Homepage(View):
    def get(self,r):
        return render(r,"home.html")
    

class LoginView(FormView):
    template_name = "signup/login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def post(self,r):
        username = r.POST.get("username")
        password = r.POST.get("password")

        user = authenticate(username = username,password=password)


        if user is not None:
            if user.is_active:
                login(r,user)
                return redirect("dashboard")
            else:
                return HttpResponse("inactive user")
        else:
            return HttpResponse("invalid Username or Password")

    
class Logout(View):
    def get(self,r):
        logout(r)
        return redirect("homepage")
    

    



