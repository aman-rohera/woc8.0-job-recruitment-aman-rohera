from django.shortcuts import render

def graveyard_welcome(request):
    # Passing a list to practice DTL loops
    context = {
        'greeting': 'Welcome to the CareerSphere Graveyard',
        'spooky_messages': [
            'Beware of the bugs...',
            'Deadlines are closer than they appear...',
            'Your soul is now bound to Django...'
        ]
    }
    return render(request, 'home.html', context)