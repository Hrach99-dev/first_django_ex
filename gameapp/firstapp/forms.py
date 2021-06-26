from django import forms

class BlogForm(forms.Form):
    num1 = forms.CharField(label='Num1', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a first number'}))
    num2 = forms.CharField(label='Num2', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a seconf number'}))
    oper = forms.CharField(label='Oper', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a oper'}))
    


class AddGameForm(forms.Form):
    quest = forms.CharField(label='Quest', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a quest'}))
    correct = forms.CharField(label='Correct Answer', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a correct answer'}))
    wrong1 = forms.CharField(label='Wrong Answer', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a wrong answer'}))
    wrong2 = forms.CharField(label='Wrong Answer', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a wrong answer'}))
    wrong3 = forms.CharField(label='Wrong Answer', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a wrong answer'}))
    

class GameForm(forms.Form):
    global_answer = forms.CharField(label='Answer', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a answer'}))
    