import json
import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        user = data['user']
        print(user)
        
        # search for user in db
        user = User.objects.get(username=user)
        print(user)

       
        checked = data['values']
        # save step, question and checked choices
        # save_data = values(user=user,  checked=checked)
        # save_data.save()

        gb_ram_min4 = []
        # find phone that have more than 4GB ram and push device_id into gb_ram_min4
        # for device in Device.objects.all():
        #     print(device.name)
        # #     specifications = device.device_specification_set.all()
        # #     for specification in specifications:
        # #         if specification.spec_category == 'RAM':
        # #             if specification.spec_value >= '4GB':
        # #                 gb_ram_min4.append(device.id)
        # # print(gb_ram_min4)

        for specs in Device_specification.objects.all():
            if specs.spec_category == 'Memory':
                if specs.specification == 'Internal':
                    if(get_ram(specs.spec_value) >= 4):
                        gb_ram_min4.append(specs.device_id)
        print(gb_ram_min4)
         

        
        return HttpResponse('success')
    else:
        return HttpResponse('fail')


def get_ram(value):
    ram = 0
    match = re.search(r'(\d+)(?:GB|MB) RAM', value)
    if match:
        ram = int(match.group(1))
    if 'MB' in value:
        ram = ram / 1000
    return ram

def get_device_specifications(request, device_id):
    device = get_object_or_404(device, pk=device_id)
    print(device)

    specifications = device.device_specification_set.all()
    print(specifications)

    serializer = device_specificationsSerializer(specifications, many=True)
    print(serializer.data)
    return HttpResponse('success')

# function to search into json data 
def search(daily_usage, main_usage, important_feautures, particular_feautures, budget_range):



    if daily_usage == 'Less than 1 hour':
        spec_category = 'Battery'
        specification = 'Type'
        value = '2000mAh'
    elif daily_usage == '1-2 hours':
        spec_category = 'Battery'
        specification = 'Type'
        value = '3000mAh'
    elif daily_usage == '2-3 hours':
        spec_category = 'Battery'
        specification = 'Type'
        value = '4000mAh'
    elif daily_usage == 'More than 3 hours':
        spec_category = 'Battery'
        specification = 'Type'
        value = '5000mAh'
    
    if main_usage == 'Calls, Messaging and Mails':
        soc = 'SoC (Qualcomm Snapdragon 662 or MediaTek Helio G80)'
        battery_life = 'battery_life (min 4000mAh)'
        screen_resolution = 'screen_resolution (min 5.5-inch)'
        ram = 'ram (at least 3 GB)'
        storage_capacity = 'storage_capacity (at least 64 GB)'
        removable_storage = 'removable_storage'
        charging_time = 'charging_time'
        connectivity = 'connectivity (4G LTE)'
    elif main_usage == 'Multimedia (Music, Videos, Photos)':
        soc = 'SoC (Qualcomm Snapdragon 888 or Apple A14 Bionic)'
        screen_resolution = 'screen_resolution (at least 1080p - Quad HD)'
        storage_capacity = 'storage_capacity (at least 64 GB)'
        ram = 'ram (4 GB min)'
        removable_storage = 'removable_storage'
        battery_life = 'battery_life'
        video_quality = 'video_quality'
        rear_camera = 'rear_camera'
        front_camera = 'front_camera'
    elif main_usage == 'Gaming':
        soc = 'SoC (Qualcomm Snapdragon 888 or Apple A14 Bionic)'
        screen_resolution = 'screen_resolution (at least 1080p - Quad HD)'
        ram = 'ram (4 GB min)'
        gpu = 'GPU (Adreno 660 or Apple GPU 4)'
        battery_life = 'battery_life'
        chargin_time = 'chargin_time'
    elif main_usage == 'Social Networks':
        soc = 'SoC (Qualcomm Snapdragon 888 or Apple A14 Bionic)'
        screen_resolution = 'screen_resolution (at least 1080p - Quad HD, 5.5-inch)'
        storage_capacity = 'storage_capacity (at least 64 GB)'
        ram = 'ram (4 GB min)'
        removable_storage = 'removable_storage'
        battery_life = 'battery_life'
        video_quality = 'video_quality'
        rear_camera = 'rear_camera'
        front_camera = 'front_camera'
    elif main_usage == 'Web Browsing':
        soc = 'SoC (Qualcomm Snapdragon 662 or MediaTek Helio G80)'
        battery_life = 'battery_life (min 4000mAh)'
        screen_resolution = 'screen_resolution (min 5.5-inch)'
        ram = 'ram (at least 3 GB)'
        storage_capacity = 'storage_capacity (at least 64 GB)'
        removable_storage = 'removable_storage'
        charging_time = 'charging_time'
        connectivity = 'connectivity (4G LTE)'
    elif main_usage == 'News, Weather and GPS':
        soc = 'SoC (Qualcomm Snapdragon 662 or MediaTek Helio G80)'
        battery_life = 'battery_life (min 4000mAh)'
        screen_resolution = 'screen_resolution (min 5.5-inch)'
        ram = 'ram (at least 3 GB)'
        storage_capacity = 'storage_capacity (at least 64 GB)'
        removable_storage = 'removable_storage'
        charging_time = 'charging_time'
        connectivity = 'connectivity (4G LTE)'

    if important_feautures == 'High Resolution Screen':
        screen_resolution = 'screen_resolution (at least 1080p - Quad HD)'
    elif important_feautures == 'Dedicated Graphics Processor':
        gpu = 'GPU (Adreno 660 or Apple GPU 4)'
    elif important_feautures == 'Large Battery':
        battery_life = 'battery_life (min 4000mAh)'
        charging_time = 'charging_time'
    elif important_feautures == 'High Quality Camera':
        rear_camera = 'rear_camera'
        front_camera = 'front_camera'
    elif important_feautures == 'Plenty of Storage Space':
        storage_capacity = 'storage_capacity (at least 64 GB)'
        removable_storage = 'removable_storage'
    elif important_feautures == 'Long-range Connectivity':
        connectivity = 'connectivity (4G LTE)'
    elif important_feautures == 'Fast Charging':
        charging_time = 'charging_time'
    elif important_feautures == 'Large Display':
        screen_resolution = 'screen_resolution (at least 1080p - Quad HD, 5.5-inch)'
    elif important_feautures == 'High Quality Audio':
        audio_quality = 'audio_quality'


    if particular_feautures == 'Age-appropriate content':
        age_appropriate_content = 'age_appropriate_content'
    elif particular_feautures == 'Parental controls':
        parental_controls = 'parental_controls'
    elif particular_feautures == 'Simple user interface':
        simple_user_interface = 'simple_user_interface'
    elif particular_feautures == 'Large, easy-to-press buttons':
        large_buttons = 'large_buttons'
    elif particular_feautures == 'Hearing aid compatibility mode':
        hearing_aid_compatibility = 'hearing_aid_compatibility'

    if budget_range == 'Under $200':
        budget = 'budget (under $200)'
    elif budget_range == '$200 - $400':
        budget = 'budget ($200 - $400)'
    elif budget_range == '$400 - $600':
        budget = 'budget ($400 - $600)'
    elif budget_range == 'Over $600':
        budget = 'budget (over $600)'



