from django.core.paginator import Paginator
from django.shortcuts import render
from .models import RunningShoe
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import QuizForm
from .models import Answer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def shoe_list(request):
    shoes = RunningShoe.objects.all()

    answered_questions = request.session.get('answered_questions', [])
    selected_answers = Answer.objects.filter(question_id__in=answered_questions)

    for answer in selected_answers:
        filter_kwargs = {answer.filter_field: answer.filter_value}
        shoes = shoes.filter(**filter_kwargs)

    # Pagination
    paginator = Paginator(shoes, 5)  # Show 5 shoes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recommender/shoe_list.html', {'page_obj': page_obj})

# View for displaying a detailed shoe page
def shoe_detail(request, shoe_id):
    shoe = get_object_or_404(RunningShoe, id=shoe_id)
    return render(request, 'recommender/shoe_detail.html', {'shoe': shoe})

def quiz(request):
    # Get the list of answered questions from the session
    answered_questions = request.session.get('answered_questions', [])
    # Get the first unanswered question
    question = Question.objects.exclude(id__in=answered_questions).first()

    # If no unanswered question, redirect to the shoe list (or a results page)
    if not question:
        return redirect('shoe_list')

    if request.method == 'POST':
        form = QuizForm(request.POST, question=question)
        if form.is_valid():
            # Retrieve the selected answer id from the form data
            selected_answer_id = form.cleaned_data['answer']
            # (Optional) Use selected_answer_id if needed
            answered_questions.append(question.id)
            request.session['answered_questions'] = answered_questions
            return redirect('quiz')
    else:
        form = QuizForm(question=question)

    return render(request, 'recommender/quiz.html', {'form': form, 'question': question})


def reset_quiz(request):
    # Clear all session data related to answered questions
    if 'answered_questions' in request.session:
        del request.session['answered_questions']
    return redirect('quiz')
