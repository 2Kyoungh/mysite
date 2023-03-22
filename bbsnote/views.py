from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

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