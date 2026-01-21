from django.shortcuts import render, redirect
from .models import TrainingRecord
from .forms import RecordForm

def timeline(request):

    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline')
    else:
        form = RecordForm() 


    records = TrainingRecord.objects.all().order_by('-date', '-created_at')

    context = {
        'form': form,
        'records': records
    }
    return render(request, 'timeline.html', context)