from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            
            name_first = form.cleaned_data['name_first']
            name_last = form.cleaned_data['name_last']
            comment = form.cleaned_data['comment']
            email= form.changed_data['email']
            agree= form.changed_data['agree']
            date= form.changed_data['date']
            birth_date= form.changed_data['birth_date']
            value= form.changed_data['value']
            email_addres= form.changed_data['email_addres']
            message= form.changed_data['message']
            email_address= form.changed_data['email_address']
            day= form.changed_data['day']
            favorite_color= form.changed_data['favorite_color']
            favorite_colo= form.changed_data['favorite_colo']
            favorite= form.changed_data['favorite']
            favorite_colorss= form.changed_data['favorite_colorss']
            model_choice= form.changed_data['model_choice']
            model_choices= form.changed_data['model_choices']

            return render(request, 'base.html', {'name_first': name_first, 'name_last':name_last, 'comment': comment, 'email':email,'agree': agree,'date':date,'birth_date':birth_date,'value':value,'email_addres':email_addres ,'message':message,'email_address':email_address ,'day':day,'favorite_color':favorite_color,'favorite_colo':favorite_colo,'favorite':favorite,'favorite_colorss':favorite_colorss,'model_choice':model_choice,'model_choices':model_choices})
    else:
        form = ExampleForm()

    return render(request, 'form.html', {'form': form})

