from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    page = request.GET.get('page', 1)

    board_list = Board.objects.order_by('-create_date')

    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)

    context = {'board_list' : page_obj}
    return render(request, 'bbsnote/board_list.html', context)


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

@login_required(login_url='common:login')
def comment_create(request, board_id):
    if request.method == 'POST':
        board = Board.objects.get(id=board_id)
        board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
        #comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
        #comment.save()
        #return redirect('bbsnote:detail', board_id=board.id)
    return redirect('bbsnote:detail', board_id=board_id)


@login_required(login_url='common:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.author = request.user
            board.save()
            return redirect('bbsnote:index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})


    