from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm

# Create your views here.
def index(request):
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list' : board_list}
    #return HttpResponse("bbsnote에 오신 것을 환영합니다.")
    return render(request, 'bbsnote/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    #comment.save()
    return redirect('bbsnote:detail', board_id=board.id)

def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})