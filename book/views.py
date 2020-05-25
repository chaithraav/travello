from django.shortcuts import render,get_object_or_404
from . models import Places,reservation,Payment
from .forms import reservationForm,PaymentForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.
# 
def booking(request):
    dests = Places.objects.all()
    return render(request,'booking.html',{'dests': dests})

def booknow(request,pk):
    template_name = 'booknow.html'
    #form = reservationForm(request.POST or None)
    place_id = get_object_or_404(Places,  pk=pk)

    if request.method == 'GET':
        form = reservationForm()
    else:
        form = reservationForm(request.POST)
        try:
            if form.is_valid():
                place_id_save = form.save(commit = False)
                p = form.save(commit = False)
                place_id_save.user = request.user
                p.place_id = Places.objects.get(pk=pk)
                place_id_save.save()
                form = reservationForm()
                #form.save()
                messages.success(request, 'YOU ARE ONE STEP AHEAD FOR BOOKING!')

        except Exception as e:
             messages.warning(request, 'error in saving. Error: {}'.format(e))

    context = {
        'form':form,
        'place_id':place_id,
    }
    return render(request, template_name, context)

def edit(request, pk):
    template_name = 'booknow.html'
    post = get_object_or_404(reservation, pk=pk)

    if request.method == "POST":
        form = reservationForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'updated')
        except Exception as e:
            messages.warning(request, 'Not saved due to error: {}'.format(e))

    else:
        form = reservationForm(instance=post)

    context ={
        'form': form,
        'post': post,
    }

    return render(request, template_name, context)

def delete(request, pk):
    template_name = 'booknow.html'
    post = get_object_or_404(reservation, pk=pk)

    try:
        if request.method == "POST":
            form = reservationForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'you have succesfully deleted your booking')
        else:
            form = reservationForm(instance=post)
    except Exception as e:
        messages.warning(request, 'could not cancel your booking: {}'.format(e))
    context = {
         'form': form,
         'post': post,
    }

    return render(request, template_name, context)

def cancel(request):
    template_name = 'cancel.html'

    details = reservation.objects.all()

    context = {
        'items': details,
    }
    return render(request,template_name,context)

def payment(request):
    template_name = 'payment.html'
    form = PaymentForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'YOUR BOOKING IS CONFIRMED!!!')

    except Exception as e:
        form = PaymentForm()
        messages.warning(request, 'error in saving. Error: {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = reservation.objects.filter(Q(name__icontains=srch))

            if match:
                return render(request, 'search.html', {'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('search')

    return render(request, 'search.html')

def mybooking(request):
    template_name = 'cancel.html'

    details = reservation.objects.filter(user = request.user)

    context = {
        'items': details,
    }
    return render(request,template_name,context)