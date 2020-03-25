from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

SECURITY_QUESTIONS = (
    ('0','What was the house number and street name you lived in as a child?'),
    ('1','What were the last four digits of your childhood telephone number?'),
    ('2','What primary school did you attend?'),
    ('3','In what town or city was your first full time job?'),
    ('4','In what town or city did you meet your spouse/partner?'),
    ('5','What is the middle name of your oldest child?'),
    ('6',"What are the last five digits of your driver's licence number?"),
    ('7',"What is your grandmother's (on your mother's side) maiden name?"),
    ('8',"What is your spouse or partner's mother's maiden name?"),
    ('9','In what town or city did your mother and father meet?'),
    ('10','What time of the day were you born? (hh:mm)'),
    ('11','What time of the day was your first child born? (hh:mm)'),
)

class RegularUserCreation(UserCreationForm):
    email = forms.EmailField(required=True)
    question1 = forms.ChoiceField(choices=SECURITY_QUESTIONS)
    question2 = forms.ChoiceField(choices=SECURITY_QUESTIONS)
    answer1 = forms.CharField(min_length=1, max_length=20)
    answer2 = forms.CharField(min_length=1, max_length=20)

    question1.widget.attrs.update({'style': 'font-size:12pt'})
    question2.widget.attrs.update({'style': 'font-size:12pt'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",'question1','answer1','question2','answer2')

    def save(self, commit=True):
        user = super(RegularUserCreation, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.question1 = self.cleaned_data["question1"]
        user.question2 = self.cleaned_data["question2"]
        user.answer1 = self.cleaned_data["answer1"]
        user.answer2 = self.cleaned_data["answer2"]

        if commit:
            user.save()
        return user