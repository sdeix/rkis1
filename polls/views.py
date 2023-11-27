from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import CreationForm, AddForm, AddFormchoice



from . import models



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        try:
            voter = models.Voters.objects.get(question=question,voter=request.user)
            last_choise = models.Choice.objects.get(pk=voter.choise.id)
            question.votes -= 1
            last_choise.votes -= 1
            last_choise.save()
            voter.delete()
        except:
            pass
        voter = models.Voters.objects.create(question=question,voter=request.user,choise=selected_choice)
        question.votes += 1
        selected_choice.votes += 1
        selected_choice.save()
        question.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


class BBLoginView(LoginView):
    template_name = 'register/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'register/logout.html'



class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'register/reg.html'

class DeleteProfile(DeleteView):
    model = models.User
    success_url = reverse_lazy('index')
    template_name = 'register/delete.html'

class UpdateProfile(UpdateView):
    model = models.User
    success_url = reverse_lazy('index')
    template_name = 'register/profile_update.html'
    fields = ['username','avatar']



def addchoice(request):
    formset = [AddFormchoice() for i in range(Question.object.filter(id=pk).num_of_questions)]
    return render(request, 'polls/addchoice.html', {'formset': formset})

def addquestion(request):
    if request.method == 'POST':
        if 'AddQuestionsBtn' in request.POST:
            form = AddForm(request.POST, request.FILES)
            if form.is_valid():
                new_Question = form.save(commit=False)
                new_Question.pic = form.cleaned_data['img']
                new_Question.save()
                formset = [AddFormchoice() for i in range(new_Question.num_of_questions)]
                return render(request, 'polls/addchoice.html', {'formset': formset, 'Qid': new_Question.id})
        else:
            for i in range(Question.objects.get(id=request.POST.get('Qid')).num_of_questions):
                form = AddFormchoice({'choice_text':request.POST.getlist('choice_text')[i]})
                if form.is_valid():
                    print(request.POST)
                    new_Choice = form.save(commit=False)
                    new_Choice.question = Question.objects.get(id=request.POST.get('Qid'))
                    new_Choice.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = AddForm()
        return render(request, 'polls/addquestion.html', {'form': form})

