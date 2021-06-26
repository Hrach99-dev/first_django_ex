import random
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import BlogForm, AddGameForm, GameForm
from .models import Calc, Quest

# Create your views here.
def index(request):
   
    return render(request, 'index.html')




def about(request):
    form = BlogForm(request.POST)
    result = None
    if form.is_valid():
        if form.cleaned_data['oper'] == '+':
            result = int(form.cleaned_data['num1']) + int(form.cleaned_data['num2'])
        elif form.cleaned_data['oper'] == '-':
            result = int(form.cleaned_data['num1']) - int(form.cleaned_data['num2'])
        elif form.cleaned_data['oper'] == '*':
            result = int(form.cleaned_data['num1']) * int(form.cleaned_data['num2'])
        elif form.cleaned_data['oper'] == '/':
            result = float(form.cleaned_data['num1']) / float(form.cleaned_data['num2'])

        num = Calc(num1=form.cleaned_data['num1'], num2=form.cleaned_data['num2'], oper=form.cleaned_data['oper'], result=result)
        num.save()

        return redirect('about')
    numbers = Calc.objects.all()
    return render(request, 'about.html', {'numbers':numbers, 'form': form})


def runner(request):
    return render(request, 'runner.html')


mdict = {}
count = 0
correct_result = 0
def game(request):
    
    global mdict
    global count
    global correct_result

    quests = Quest.objects.all()
    

    if len(quests) < 1:
        return redirect('addquest')
    else:
        quest = quests[count]
        value_list = [quest.correct, quest.wrong1, quest.wrong2, quest.wrong3]
        random.shuffle(value_list)

        form = GameForm(request.POST)

        if form.is_valid():

            form_answer = form.cleaned_data['global_answer']
            
            if count == len(quests) - 1:
                return redirect('runner')

            if form_answer == quest.correct:
                flag = True
                correct_result += 1 
            else:
                flag = False
                
            mdict[quest.quest] = [form_answer, flag]
            count += 1
                        
            return redirect('game')
    return render(request, 'game.html', {'key':quest.quest, 'form':form, 'value_list':value_list, 'mdict':mdict, 'count':count,'correct_result':correct_result})


def addquest(request):
    form = AddGameForm(request.POST)
    if form.is_valid():
        quest = Quest(quest=form.cleaned_data['quest'],
                    correct=form.cleaned_data['correct'],
                    wrong1=form.cleaned_data['wrong1'],
                    wrong2=form.cleaned_data['wrong2'],
                    wrong3=form.cleaned_data['wrong3'])

        quest.save()
        return redirect('runner')
    return render(request, 'addquest.html', {'form':form})

