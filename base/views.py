from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Topic, Message , User
from django.db.models import Q
from .forms import RoomFroms , UserForm , MyUsercreationform
from django.http import JsonResponse
# Create your views here.


def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            

        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Log the user in if authentication succeeds
            login(request, user)
            # Replace 'home' with the name of your home route
            return redirect('home')
        else:
            # Show an error message if authentication fails
            messages.error(request, 'Invalid username or password')
  

    # Render the login page
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form =MyUsercreationform
    if request.method == 'POST':
        form =MyUsercreationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An erro occured during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)

        )
    topics = Topic.objects.all()[0:5]
    rooms_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {
        'rooms': rooms,
        'topics': topics,
        'room': topics,
        'room_count': rooms_count,
        'room_messages': room_messages
    }
    return render(request, 'base/index.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')


        )
        room.participants.add(request. user)
        return redirect('rooms', pk=room.id)
    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants

    }
    return render(request, 'base/room.html', context)


def userprofile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        'user': user,
        'rooms': rooms,
        'room_messages': room_messages,
        'topics': topics

    }
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createroom(request):
    form = RoomFroms()
    topics = Topic.objects.all()

    if request.method == 'POST':
           topic_name = request.POST.get('topic')
           topic, created = Topic.objects.get_or_create(name=topic_name)
           Room.objects.create(
               host=request.user,
               topic=topic,
               name=request.POST.get('name'),
               description=request.POST.get('description')

           )
           return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomFroms(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic =  topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    context ={ 'form': form ,  'topics':topics , 'room':room}
    return render (request, 'base/room_form.html', context)
@login_required(login_url='login')
def deleteroom(request, pk):
    room =Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
        
    if request.method  == 'POST':
        room.delete()
        return redirect('home')    
     
    return render(request, 'base/delete.html' , {'obj':room} )


@login_required(login_url='login')
def deletemessage(request, pk):
    message =Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here!!')
        
    if request.method  == 'POST':
        message.delete()
        return redirect('home')    
     
    return render(request, 'base/delete.html' , {'obj':message} )
 
@login_required(login_url='login')
def updateuser(request):
    user = request.user
    form = UserForm(instance=user)  # Initialize form with the current user instance
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES ,instance=user)
        if form.is_valid():
            form.save()  # Save the updated user details
            return redirect('profile', pk=user.id)  # Redirect to profile
        else:
            print(form.errors)  # Debugging: print errors if form is invalid
    return render(request, 'base/update-user.html', {'form': form})



def custom_search(request):
    query = request.GET.get("q", "")
    user_results = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
    topic_results = Topic.objects.filter(name__icontains=query)
    return render(request, "base/custom_search_results.html", {"users": user_results, "topics": topic_results})



def broadcast_message(request):
    if request.method == 'POST':
        # Process the POST data
        message = request.POST.get('message')
        # Logic to handle broadcast (e.g., save to DB or send notifications)
        return JsonResponse({'status': 'success', 'message': message})
    return render(request, 'base/broadcast.html')

def topicpage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topic =Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html' , {'topic': topic} )

def activitypage(request):
    room_messages = Message.objects.all()
    return render (request, 'base/activity.html' , {'room_messages': room_messages})