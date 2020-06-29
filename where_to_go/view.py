from django.shortcuts import render


def show_start_page(request):
    print('start page started')
    return render(request, 'index.html')
