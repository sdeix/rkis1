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
from .forms import CreationForm

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
        
        selected_voters = question.voters_set.get()
        selected_voters.add(request.user)
        selected_voters.save()
        selected_choice.votes += 1
        selected_choice.save()
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