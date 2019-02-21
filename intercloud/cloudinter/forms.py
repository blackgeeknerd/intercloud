#import needed dependencies
from django import forms
from .models import *

#options for the student employment status
employmentStatus_Stu = (('Student', 'Student',), ('Employed(Part-Time)', 'Employed(Part-Time)',),('Employed(Full-Time)', 'Employed(Full-Time)',), ('Unemployed', 'Unemployed',), ('Self Employed', 'Self Employed'))
parent_employmentSta = (('Employed(Part-Time)', 'Employed(Part-Time)',),('Employed(Full-Time)', 'Employed(Full-Time)',), ('Unemployed', 'Unemployed',), ('Self Employed', 'Self Employed'))

class QuestionForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100,  
                               widget=forms.TextInput(attrs={'class': 'form-control form-group', 'name': 'fullname', 'placeholder' : 'Full Name'}))
    age = forms.CharField(max_length=10,  
                               widget=forms.TextInput(attrs={'class': 'form-control form-group', 'name': 'age', 'placeholder' : 'Age'}))
    phone_number = forms.CharField(max_length=10,  
                               widget=forms.TextInput(attrs={'class': 'form-control form-group', 'name': 'phonenumber', 'placeholder' : 'xxxxxxxxx'}))
    email = forms.EmailField(max_length=40,
                widget=forms.TextInput(attrs={'class': 'form-control form-group', 'name': 'email', 'required' : True, 'placeholder' : 'Email'}))
    address = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'address', 'required' : True, 'placeholder' : 'Residential Address'}))
    state = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'state', 'required' : True, 'placeholder' : 'State'}))
    school = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'school', 'required' : True, 'placeholder' : 'Secondary School'}))
    university = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'university', 'required' : True, 'placeholder' : 'Tetiary Institute'}))
    course = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'school', 'required' : True, 'placeholder' : 'Course Studied'}))
    university_start = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-group', 'name': 'university_start', 'required' : True, 'placeholder' : 'YYYY-MM-DD'}),help_text='Required. Format: YYYY-MM-DD')
    university_end = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-group ', 'name': 'university_end', 'required' : True, 'placeholder' : 'YYYY-MM-DD'}),help_text='Required. Format: YYYY-MM-DD')
    employment_status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-group', 'name': 'employment_status', 'required' : True, 'placeholder' : 'Student Employment Status'}), choices=employmentStatus_Stu)   
    parent_employment = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-group', 'name': 'parent_employment', 'required' : True, 'placeholder' : 'Parent Employment Status'}), choices=parent_employmentSta)   
    program_knowledge = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'prog_knowledge', 'required' : True, 'placeholder' : 'Program Knowledge'}))
    database_knowledge = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'database_knowledge', 'required' : True, 'placeholder' : 'Database Knowledge'}))
    operatingsystem_knowledge = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'operatingsystem_knowledge', 'required' : True, 'placeholder' : 'Operating System Knowledge'}))
    note = forms.CharField(max_length=200,
                widget=forms.TextInput(attrs={'class': 'form-control form-group ', 'name': 'comment', 'required' : True, 'placeholder' : 'Comment'}))

     #function that saves the user details after user submits form
    def save(self, commit=False):
        detail = super(QuestionForm, self).save(commit=False)
        detail.school = self.cleaned_data['school']
        detail.fullname = self.cleaned_data['fullname']
        detail.age = self.cleaned_data['age']
        detail.university = self.cleaned_data['university']
        detail.course = self.cleaned_data['course']
        detail.university_start = self.cleaned_data['university_start']
        detail.university_end = self.cleaned_data['university_end']
        detail.employment_status = self.cleaned_data['employment_status']
        detail.parent_employment = self.cleaned_data['parent_employment']
        detail.prog_knowledge = self.cleaned_data['program_knowledge']
        detail.database_knowledge = self.cleaned_data['database_knowledge']
        detail.operatingsystem_knowledge = self.cleaned_data['operatingsystem_knowledge']
        detail.note = self.cleaned_data['note']
        detail.phonenumber = self.cleaned_data['phone_number']




        # details.serialnumb = self.cleaned_data['serialnumb']

        if commit:
            detail.save()
        return detail

    class Meta:
        model = Question
        fields = ('fullname', 'age', 'address','school', 'state',)


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)