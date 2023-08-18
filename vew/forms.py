from django.contrib.auth.forms import UserCreationForm
from .models import User



class DoctorSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','dp','email','address')


    def save(self,commit = True):
        user = super().save(commit= False)
        user.is_doctor = True
        if commit:
            user.save()
        return user
    


class PatientSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name','last_name','dp','email','address')


    def save(self,commit = True):
        user = super().save(commit= False)
        user.is_patient = True
        if commit:
            user.save()
        return user
   