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
                    available_ram = get_available_ram(specs.spec_value)
                    if available_ram == 0:
                        continue
                    elif len(available_ram) >= 1:
                        for ram in available_ram:
                            if ram >= 4:
                                gb_ram_min4.append(specs.device_id)
                            
        print(gb_ram_min4)
         

        
        return HttpResponse('success')
    else:
        return HttpResponse('fail')

def get_available_ram(value):
    try:
        ram_values = []
        if ',' in value:
            pairs = value.split(', ')
            for pair in pairs:
                match = re.search(r'(\d+)(?:GB|MB) RAM', pair)
                if match:
                    ram = int(match.group(1))
                if 'MB' in pair:
                    ram = ram / 1000
                if 'ROM' in pair:
                    continue
                ram_values.append(ram)
        elif 'RAM' in value:
            match = re.search(r'(\d+)(?:GB|MB) RAM', value)
            if match:
                ram = int(match.group(1))
            if 'MB' in value:
                ram = ram / 1000
            if 'ROM' in value:
                return 0
            ram_values.append(ram)
        else:
            return 0
        ram_values = list(dict.fromkeys(ram_values))
        ram_values = sorted(ram_values)
        return ram_values
    except:
        return 0

def get_battery(value):
    try:
        battery = 0
        if 'mAh' in value:
            match = re.search(r'(\d+) mAh', value)
            if match:
                battery = int(match.group(1))
        elif 'mAh' not in value:
            return 0
        return battery
    except:
        return 0

def get_storage(value):
    try:
        storages_values = []
        if 'RAM' in value:
            value = re.sub(r'\d+(?:GB|MB) RAM', '', value)
            if ',' in value:
                pairs = value.split(',')
                for pair in pairs:
                    if '.' in pair:
                        if 'GB' in pair:
                            match = re.search(r'(\d+\.\d+)GB', pair)
                            if match:
                                storage = float(match.group(1))
                        elif 'MB' in pair:
                            match = re.search(r'(\d+\.\d+)MB', pair)
                            if match:
                                storage = float(match.group(1)) / 1000
                    else:
                        if 'GB' in pair:
                            match = re.search(r'(\d+)GB', pair)
                            if match:
                                storage = int(match.group(1))
                        elif 'MB' in pair:
                            match = re.search(r'(\d+)MB', pair)
                            if match:
                                storage = int(match.group(1)) / 1000
                    storages_values.append(storage)

            else:
                if '.' in value:
                    if 'GB' in value:
                        match = re.search(r'(\d+\.\d+)GB', value)
                        if match:
                            storage = float(match.group(1))
                    elif 'MB' in value:
                        match = re.search(r'(\d+\.\d+)MB', value)
                        if match:
                            storage = float(match.group(1)) / 1000
                else:
                    if 'GB' in value:
                        match = re.search(r'(\d+)GB', value)
                        if match:
                            storage = int(match.group(1))
                    elif 'MB' in value:
                        match = re.search(r'(\d+)MB', value)
                        if match:
                            storage = int(match.group(1)) / 1000
                storages_values.append(storage)
        else:
            if '.' in value:
                if 'GB' in value:
                    match = re.search(r'(\d+\.\d+)GB', value)
                    if match:
                        storage = float(match.group(1))
                elif 'MB' in value:
                    match = re.search(r'(\d+\.\d+)MB', value)
                    if match:
                        storage = float(match.group(1)) / 1000
            else:
                if 'GB' in value:
                    match = re.search(r'(\d+)GB', value)
                    if match:
                        storage = int(match.group(1))
                elif 'MB' in value:
                    match = re.search(r'(\d+)MB', value)
                    if match:
                        storage = int(match.group(1)) / 1000
                storages_values.append(storage)

        storages_values = list(dict.fromkeys(storages_values))
        storages_values = sorted(storages_values)
        return storages_values
    except:
        return 0

def get_removal_storage(value):
    try:
        if re.search(r'microSD', value, re.IGNORECASE):
            return True
        else:
            return False
    except:
        return False

def get_chipset(value):
    try:
        if 'Qualcomm' and 'Snapdragon' in value:
            # get the number after the word Snapdragon and check if there is a letter or a symbol after it via regex
            chipset = re.search(r'Snapdragon (\d+)([a-zA-Z])?', value)
            if chipset:
                return value;
            else:
                # check if after the word Snapdragon there is a letter and a number
                chipset = re.search(r'Snapdragon ([a-zA-Z])(\d+)', value)
                if chipset:
                    return value
        elif 'Apple' in value:
            chipset = re.search(r'A(\d+)', value)
            if chipset:
                return value
        elif 'Mediatek' in value:
            chipset = re.search(r'MT(\d+)', value)
            if chipset:
                return value
        elif 'Intel' in value:
            chipset = re.search(r'Atom Z(\d+)', value)
            if chipset:
                return value
            else:
                chipset = re.search(r'Atom x|X(\d+)', value)
                if chipset:
                    return value
        elif 'Exynos' in value:
            chipset = re.search(r'Exynos (\d+)', value)
            if chipset:
                return value
        elif 'Kirin' in value:
            chipset = re.search(r'Kirin (\d+)', value)
            if chipset:
                return value
        elif 'Nvidia' in value:
            chipset = re.search(r'Tegra (\d+)', value)
            if chipset:
                return value
        elif 'Xiaomi' in value:
            chipset = re.search(r'S(\d+)', value)
            if chipset:
                return value
        elif 'Unisoc' in value:
            chipset = re.search(r'Unisoc Tiger(\d+)', value)
            if chipset:
                return value
        elif 'Spreadtrum' in value:
            chipset = re.search(r'SC(\d+)', value) or re.search(r'(\d+)', value)
            if chipset:
                return value
        else:
            return None
    except:
        return None

def get_screen_size(value):
    try:
        screen_size = re.search(r'(\d+.\d+)', value)
        if screen_size:
            return screen_size.group(1)
        else:
            return None
    except:
        return None

def get_screen_resolution(value):
    try:
        screen_resolution = re.search(r'(\d+ x \d+)', value)
        if screen_resolution:
            return screen_resolution.group(1)
        else:
            return None
    except:
        return None

def get_camera(value):
    try:
        main_camera = re.search(r'(\d+) MP', value)
        if main_camera:
            return main_camera.group(1)
        else:
            return None
    except:
        return None

def get_camera_video(value):
    try:
        # check via regex if value contains 1080p@30fps or 4K@30fps 
        main_camera_video = re.search(r'(\d+K|2160p|1080p|720p|480p|360p)', value)
        if main_camera_video:
            return value
        else:
            return None
    except:
        return None

# function to search into json data 
def search(daily_usage, main_usage, important_feautures, particular_feautures, budget_range):
    elite = ['Qualcomm Snapdragon 888', 'Apple A14 Bionic', 'Samsung Exynos 2100', 'Huawei Kirin 9000', 'Xiaomi Surge S88', 'Qualcomm Snapdragon 865', 'Qualcomm Snapdragon 870', 'Apple A13 Bionic', 'Samsung Exynos 990', 'Huawei Kirin 990', 'Nvidia Tegra X1', 'Xiaomi Surge S3']

    premium = ['Qualcomm Snapdragon 855', 'Apple A12 Bionic', 'Samsung Exynos 9820', 'Huawei Kirin 980', 'Xiaomi Surge S88', 'Qualcomm Snapdragon 845', 'Apple A11 Bionic', 'Samsung Exynos 9810', 'Huawei Kirin 970', 'Nvidia Tegra X1']

    mid_range = ['Qualcomm Snapdragon 835', 'Apple A10 Fusion', 'Samsung Exynos 8895', 'Intel Atom x3-C3200', 'Huawei Kirin 960', 'Nvidia Tegra X1', 'Qualcomm Snapdragon 821', 'Qualcomm Snapdragon 690', 'Apple A9', 'Samsung Exynos 8890', 'Intel Atom x3-C3200', 'Huawei Kirin 950', 'Qualcomm Snapdragon 778G']

    entry_range = ['Qualcomm Snapdragon 820', 'Qualcomm Snapdragon 750G', 'Apple A8', 'Samsung Exynos 7420', 'Intel Atom x5-Z8500', 'Huawei Kirin 935', 'Qualcomm Snapdragon 810', 'Apple A8', 'Samsung Exynos 7420', 'Intel Atom x5-Z8500', 'Huawei Kirin 935', 'Qualcomm Snapdragon 662', 'Qualcomm Snapdragon 768G', 'Qualcomm Snapdragon 780G']


    low_range = [
        'Qualcomm Snapdragon 765G', 'MediaTek Dimensity 1000L', 'Samsung Exynos 980',
        'Qualcomm Snapdragon 730', 'MediaTek Helio G90T', 'Samsung Exynos 9610',
        'Qualcomm Snapdragon 720G', 'MediaTek Helio G80', 'Samsung Exynos 9611',
        'Qualcomm Snapdragon 675', 'MediaTek Helio P70', 'Samsung Exynos 9610', 'Unisoc Tiger T7510', 'Spreadtrum SC9863A',
        'Qualcomm Snapdragon 670', 'Qualcomm Snapdragon 800', 'Qualcomm Snapdragon 801', 'Qualcomm Snapdragon 600', 'Qualcomm Snapdragon 805', 'Qualcomm Snapdragon 808', 'MediaTek Helio P60', 'Samsung Exynos 7885', 'Unisoc Tiger T710', 'Spreadtrum SC9853i',
        'Qualcomm Snapdragon 660', 'MediaTek Helio P23', 'Samsung Exynos 7870', 'Unisoc Tiger T660', 'Spreadtrum SC9853i',
        'Qualcomm Snapdragon 650', 'MediaTek Helio X10', 'Samsung Exynos 7580', 'Unisoc Tiger T6500', 'Spreadtrum SC9830',
        'Qualcomm Snapdragon 636', 'MediaTek Helio P23', 'Samsung Exynos 7870', 'Unisoc Tiger T722', 'Spreadtrum SC9853i',
        'Qualcomm Snapdragon 630', 'MediaTek Helio P60', 'Samsung Exynos 7885', 'Unisoc Tiger T7500', 'Spreadtrum SC9853i',
        'Qualcomm Snapdragon 625', 'MediaTek Helio P23', 'Samsung Exynos 7870', 'Unisoc Tiger T720', 'Spreadtrum SC9853i',
        'Qualcomm Snapdragon 617', 'MediaTek Helio X10', 'Samsung Exynos 7580', 'Unisoc Tiger T7500', 'Spreadtrum SC9830',
        'Qualcomm Snapdragon 615', 'MediaTek Helio X10', 'Samsung Exynos 7580', 'Unisoc Tiger T7500', 'Spreadtrum SC9830',
        'Qualcomm Snapdragon 612', 'MediaTek Helio X10', 'Samsung Exynos 7580', 'Unisoc Tiger T7500', 'Spreadtrum SC9830',
        'Qualcomm Snapdragon 610', 'MediaTek Helio X10', 'Samsung Exynos 7580', 'Unisoc Tiger T7500', 'Spreadtrum SC9830'
    ]


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
        chipset = entry_range and low_range
        screen_size = 5.5
        ram = 3
        storage_capacity = 64
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



