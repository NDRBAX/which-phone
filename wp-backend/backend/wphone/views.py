import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import jwt
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import *
import random
from django.db.models import Q
from .models import *
from .serializers import *
from .utils import search, get_result
from .data import premium, middle, entry, low, configs


# SUBMIT FORM
@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        user = data['user']
        daily_usage = data['dailyUsage']
        main_usage = data['mainUsage']
        storage_space = data['storageSpace']
        display_size = data['displaySize']
        important_features = data['importantFeatures']
        budget_range = data['budgetRange']

        user = User.objects.get(username=user)

        specs = search(daily_usage, main_usage, storage_space, display_size, important_features, budget_range)

        spec = Specification.objects.create(
            battery=specs['battery'],
            ram=specs['ram'],
            storage=specs['storage'],
            chipset=specs['chipset'],
            screen_size=specs['screen_size'],
            screen_resolution=specs['screen_resolution'],
            rear_camera=specs['rear_camera'],
            rear_camera_video=specs['rear_camera_video'],
            front_camera=specs['front_camera'],
            front_camera_video=specs['front_camera_video'],
            network=specs['network'],
            removal_storage=specs['removal_storage'],
            price_range_min=specs['price'][0],
            price_range_max=specs['price'][1],
            dual_sim=specs['dual_sim'],
            charging=specs['charging'],
            audio_jack=specs['audio_jack'],
        )

        # save to user's history
        user.history.add(spec)

        chipsets = []
        for item in specs['chipset']:
            chipsets.extend(globals()[item])


        
        result = get_result(
            specs['battery'], 
            specs['ram'], 
            specs['storage'], 
            chipsets, 
            specs['screen_size'], 
            specs['screen_resolution'], 
            specs['rear_camera'], 
            specs['rear_camera_video'], 
            specs['front_camera'], 
            specs['front_camera_video'], 
            specs['network'], 
            specs['removal_storage'], 
            specs['price'], 
            specs['dual_sim'], 
            specs['charging'], 
            specs['audio_jack']
        )

        serializer = DeviceSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse('fail')

# ADD/REMOVE TO WIHSLIST
@csrf_exempt
def edit_wishlist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        user = data['user']
        devices = data['devices']
        # print(user, devices)

        if user == "None":
            pass
        else:
            user = User.objects.get(username=user)
            for device_id in devices:
                device = Device.objects.get(id=device_id)
                if device in user.wishlist.all():
                    pass
                else:
                    user.wishlist.add(device)
            # remove devices that are not in the list
            for device in user.wishlist.all():
                if device.id not in devices:
                    user.wishlist.remove(device)


        return HttpResponse('success')
    else:
        return HttpResponse('fail')

# GET WISHLIST
def get_wishlist(request):
    if request.method == 'GET':
        username = request.GET['username']
        user = User.objects.get(username=username)
        wishlist = user.wishlist.all()

        serializer = DeviceSerializer(wishlist, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return HttpResponse('success')
    else:
        return HttpResponse('fail')

# GET BY CATEGORY
@csrf_exempt
def get_categories(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)

        category = data['category']
        print(category)
        # user = data['user']

        
        result = []

        for key, value in configs.items():
            if key == category:
                chipsets = []
                for item in value['chipset']:
                    chipsets.extend(globals()[item])

                result = get_result(
                    value['battery'], 
                    value['ram'], 
                    value['storage'], 
                    chipsets, 
                    value['screen_size'], 
                    value['screen_resolution'], 
                    value['rear_camera'], 
                    value['rear_camera_video'], 
                    value['front_camera'], 
                    value['front_camera_video'], 
                    value['network'], 
                    value['removal_storage'], 
                    value['price'], 
                    value['dual_sim'], 
                    value['charging'], 
                    value['audio_jack']
                )

                if len(result) >= 100:
                    result = list(result)
                    random.shuffle(result)
                    random_elements = result[:100]
                else:
                    random_elements = result

        serializer = DeviceSerializer(random_elements, many=True)

        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse('fail')

# NEWSLETTER
@csrf_exempt
def subscribe_newsletter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']

        # check if email is already in Newsletter
        try:
            newsletter = NewsletterEmails.objects.get(email=email)
            return HttpResponse('Email already exists')
        except NewsletterEmails.DoesNotExist:
            pass

        # add email to Newsletter
        newsletter = NewsletterEmails.objects.create(email=email)
        newsletter.save()

        return HttpResponse('success')
    else:
        return HttpResponse('fail')

# RESET PASSWORD
@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
     

        email = data['email']
        question = data['question']
        answer = data['answer']

        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            return HttpResponse('Invalid email')

        try:
            secure_question = user.secure_question
            print(secure_question)
            secure_answer = user.secure_answer
            print(secure_answer)
        except (user.secure_question.DoesNotExist, user.secure_answer.DoesNotExist):
            return HttpResponse('Invalid question or answer')

        # generate JWT token with password reset claim
        payload = {
            'email': email,
            'question': question,
            'answer': answer,
            'exp': datetime.utcnow() + timedelta(minutes=30),
            'iat': datetime.utcnow(),
            'iss': 'tech-specs',
            'aud': 'tech-specs',
            'sub': 'password-reset'
        }

        print(payload)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        # return JWT token to user  
        return JsonResponse({'token': token}, safe=False)
    else:
        return HttpResponse('fail')

@csrf_exempt
def submit_new_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data['password']
        token = data['token']

        # decode JWT token
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, audience='tech-specs', issuer='tech-specs', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return HttpResponse('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponse('Invalid token')

        # get user email, question, and answer from token
        email = payload['email']
        question = payload['question']
        answer = payload['answer']

        # get user from email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('Invalid email')

        # check if question and answer match the ones stored for the user
        if user.secure_question != question or user.secure_answer != answer:
            return HttpResponse('Invalid question or answer')

        # update user's password
        user.set_password(password)
        user.save()

        return HttpResponse('success')
    else:
        return HttpResponse('fail')

# Change general user settings
@csrf_exempt
def edit_profile(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method')

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid request body')

    current_username = data.get('currentUsername')
    current_email = data.get('currentEmail')
    new_username = data.get('newUsername')
    new_avatar = data.get('newAvatar')

    if not (current_username and current_email):
        return HttpResponseBadRequest('Missing required field')

    try:
        user = User.objects.get(email=current_email)
    except User.DoesNotExist:
        return HttpResponseNotFound('User not found')

    if user.username != current_username:
        return HttpResponseBadRequest('Invalid username')

    if new_avatar and new_avatar != user.avatar_url:
        user.avatar_url = new_avatar

    if new_username:
        if new_username != user.username:
            try:
                User.objects.get(username=new_username)
            except User.DoesNotExist:
                user.username = new_username
            else:
                return HttpResponseBadRequest('Username taken')

    user.save()

    return HttpResponse('success')


@csrf_exempt
def set_secure(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        question = data['question']
        answer = data['answer']

        user = User.objects.get(username=username)
        user.secure_question = question
        user.secure_answer = answer
        user.save()

        return HttpResponse('success')