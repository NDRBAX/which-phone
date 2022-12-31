import re
from django.db.models import Q
from .data import  chipset_priority, daily_usage_specs, main_usage_specs, storage_space_specs, display_size_specs, important_features_specs, budget_range_specs
from .models import *

# AVAILABLE RAM IN GB
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

# AVAILABLE STORAGE IN GB
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
                        elif 'TB' in pair:
                            match = re.search(r'(\d+\.\d+)TB', pair)
                            if match:
                                storage = float(match.group(1)) * 1000
                    else:
                        if 'GB' in pair:
                            match = re.search(r'(\d+)GB', pair)
                            if match:
                                storage = int(match.group(1))
                        elif 'MB' in pair:
                            match = re.search(r'(\d+)MB', pair)
                            if match:
                                storage = int(match.group(1)) / 1000
                        elif 'TB' in pair:
                            match = re.search(r'(\d+)TB', pair)
                            if match:
                                storage = int(match.group(1)) * 1000
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
                    elif 'TB' in value:
                        match = re.search(r'(\d+\.\d+)TB', value)
                        if match:
                            storage = float(match.group(1)) * 1000

                else:
                    if 'GB' in value:
                        match = re.search(r'(\d+)GB', value)
                        if match:
                            storage = int(match.group(1))
                    elif 'MB' in value:
                        match = re.search(r'(\d+)MB', value)
                        if match:
                            storage = int(match.group(1)) / 1000
                    elif 'TB' in value:
                        match = re.search(r'(\d+)TB', value)
                        if match:
                            storage = int(match.group(1)) * 1000
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
                elif 'TB' in value:
                    match = re.search(r'(\d+\.\d+)TB', value)
                    if match:
                        storage = float(match.group(1)) * 1000
            else:
                if 'GB' in value:
                    match = re.search(r'(\d+)GB', value)
                    if match:
                        storage = int(match.group(1))
                elif 'MB' in value:
                    match = re.search(r'(\d+)MB', value)
                    if match:
                        storage = int(match.group(1)) / 1000
                elif 'TB' in value:
                    match = re.search(r'(\d+)TB', value)
                    if match:
                        storage = int(match.group(1)) * 1000
                storages_values.append(storage)

        storages_values = list(dict.fromkeys(storages_values))
        storages_values = sorted(storages_values)
        return storages_values
    except:
        return 0

# INTERSECT ARRAY
def intersect_arrays(*arrays):
    arrays = list(filter(None, arrays))
    print("==========================================================>>>>>>>>>>>>>", len(arrays))
    if arrays:
        result = set(arrays[0])
        for array in arrays[1:]:
            result = result.intersection(set(array))
        return result
    else:
        return []

# GET RESULT FROM SPECS
def get_result(battery, ram, storage, chipset, screen_size, screen_resolution, rear_camera, rear_camera_video, front_camera, front_camera_video, network, removal_storage, price, dual_sim, charging, audio_jack):

    print('battery: ', battery)
    print('ram: ', ram)
    print('storage: ', storage)
    print('chipset: ', (chipset))
    print('screen_size: ', screen_size)
    print('screen_resolution: ', screen_resolution)
    print('rear_camera: ', rear_camera)
    print('rear_camera_video: ', rear_camera_video)
    print('front_camera: ', front_camera)
    print('front_camera_video: ', front_camera_video)
    print('network: ', network)
    print('removal_storage: ', removal_storage)
    print('price: ', price)
    print('dual_sim: ', dual_sim)
    print('charging: ', charging)
    print('audio_jack: ', audio_jack)
    
    # RESULT
    result = []

    # DATA
    battery_result = []
    ram_result = []
    chipset_result = []
    storage_result = []
    screen_size_result = []
    screen_resolution_result = []
    rear_camera_result = []
    rear_camera_video_result = []
    front_camera_result = []
    front_camera_video_result = []
    network_3g_result = []
    network_4g_result = []
    network_5g_result = []
    removal_storage_result = []
    price_result = []
    dual_sim_result = []
    charging_result = []
    audio_jack_result = []

    excluded = Q(device_id__id__icontains='pad') | Q(device_id__id__icontains='book') | Q(device_id__id__icontains='tablet') | Q(device_id__id__icontains='galaxy_view') | Q(device_id__id__icontains='galaxy_camera') | Q(device_id__id__icontains='kindle') | Q(device_id__id__icontains='fire')| Q(device_id__id__icontains='tab') | Q(device_id__id__icontains='surface') | Q(device_id__id__icontains='watch') | Q(device_id__id__icontains='shield') | Q(device_id__summary__icontains='tablet') | Q(device_id__summary__icontains='pad') | Q(device_id__summary__icontains='watch') | Q(device_id__summary__icontains='fire') | Q(device_id__summary__icontains='kindle') | Q(device_id__summary__icontains='tab') 

    if battery:
        specs = Device_specification.objects.all().exclude(excluded)
        battery_pattern = r'(\d+|\d+,*\d*) mAh'
        spec_category = 'Battery'
        specification = 'Type'
        specs = specs.filter(Q(spec_category=spec_category)
                             & Q(specification=specification))
        matching_specs = [spec for spec in specs if re.search(battery_pattern, spec.spec_value) and int(
            re.search(battery_pattern, spec.spec_value).group(1).replace(',', '')) >= battery]
        for spec in matching_specs:
            battery_result.extend([spec.device_id])
        print('###################################### BATTERY ######################################')
        print(len(battery_result))

    if ram:
        specs = Device_specification.objects.all().exclude(excluded)
        spec_category = 'Memory'
        specification = 'Internal'
        specs = specs.filter(Q(spec_category=spec_category)
                             & Q(specification=specification))

        for spec in specs:
            ram_capacity = get_available_ram(spec.spec_value)
            if ram_capacity:
                if any(x >= ram for x in map(int, ram_capacity)):
                    ram_result.extend([spec.device_id])
        print('###################################### RAM ######################################')
        print(len(ram_result))

    if storage:
        specs = Device_specification.objects.all().exclude(excluded)
        spec_category = 'Memory'
        specification = 'Internal'
        specs = specs.filter(Q(spec_category=spec_category)
                             & Q(specification=specification))

        for spec in specs:
            storage_capacity = get_storage(spec.spec_value)
            if storage_capacity:
                if any(x >= storage for x in map(int, storage_capacity)):
                    storage_result.extend([spec.device_id])
        print('###################################### STORAGE ######################################')
        print(len(storage_result))

    if chipset:
        specs = Device_specification.objects.all().exclude(excluded)
        spec_category = 'Platform'
        specification = 'Chipset'
        q = Q()
        for chip in chipset:
            q |= Q(spec_category=spec_category) & Q(
                specification=specification) & Q(spec_value__icontains=chip)

        matching_specs = specs.filter(q)

        for spec in matching_specs:
            chipset_result.extend([spec.device_id])
        print('###################################### CHIPSET ######################################')
        print(len(chipset_result))

    if screen_size is not None and any(screen_size):
        min_screen_size = screen_size[0]
        max_screen_size = screen_size[1]

        specs = Device_specification.objects.all().exclude(excluded)
        screen_pattern = r'(^\d+\.\d+) inches'
        spec_category = 'Display'
        specification = 'Size'
        specs = specs.filter(Q(spec_category=spec_category)
            & Q(specification=specification)
            & Q(spec_value__icontains='inch'))

        matching_specs = [spec for spec in specs if re.search(screen_pattern, spec.spec_value) and float(
            re.search(screen_pattern, spec.spec_value).group(1).replace(',', '')) >= min_screen_size and float(re.search(screen_pattern, spec.spec_value).group(1).replace(',', '')) <= max_screen_size]

        for spec in matching_specs:
            screen_size_result.extend([spec.device_id])
        print('###################################### SCREEN SIZE ######################################')
        print(len(screen_size_result))

    if screen_resolution:
        specs = Device_specification.objects.all().exclude(excluded)
        screen_pattern = r'(\d+) x (\d+) pixels'
        specs = specs.filter(Q(spec_category='Display')
            & Q(specification='Resolution')
            & Q(spec_value__icontains='pixels'))

        matching_specs = [spec for spec in specs if re.search(screen_pattern, spec.spec_value) and int(
            re.search(screen_pattern, spec.spec_value).group(1).replace(',', '')) >= screen_resolution]
            

        for spec in matching_specs:
            screen_resolution_result.extend([spec.device_id])
        print('###################################### SCREEN RESOLUTION ######################################')
        print(len(screen_resolution_result))

    if rear_camera:
        specs = Device_specification.objects.all().exclude(excluded)
        rear_camera_pattern = r'\d+(\.\d+)?(?=\sMP)'
        specs = specs.filter(Q(spec_category='Main Camera')
            & Q(specification='Single')
            & Q(spec_value__icontains='MP'))

        matching_specs = [spec for spec in specs if re.search(rear_camera_pattern, spec.spec_value) and float(
            re.search(rear_camera_pattern, spec.spec_value).group(0).replace(',', '')) >= rear_camera]
        for spec in matching_specs:
            rear_camera_result.extend([spec.device_id])
        print('###################################### REAR CAMERA ######################################')
        print(len(rear_camera_result))

    if rear_camera_video:
        specs = Device_specification.objects.all().exclude(excluded)
        rear_camera_video_pattern = r'(\d+)(p|K)'
        specs = specs.filter(Q(spec_category='Main Camera')
            & Q(specification='Video'))
        units = {'p': 1, 'K': 1000}

        matching_specs = [spec for spec in specs if re.search(rear_camera_video_pattern, spec.spec_value) and int(
            re.search(rear_camera_video_pattern, spec.spec_value).group(1).replace(',', '')) * units[re.search(rear_camera_video_pattern, spec.spec_value).group(2)] >= rear_camera_video]
        
        for spec in matching_specs:
            rear_camera_video_result.extend([spec.device_id])
        print('###################################### REAR CAMERA VIDEO ######################################')
        print(len(rear_camera_video_result))

    if front_camera:
        specs = Device_specification.objects.all().exclude(excluded)
        front_camera_pattern = r'\d+(\.\d+)?(?=\sMP)'
        specs = specs.filter(Q(spec_category='Selfie camera')
            & Q(specification__in=['Single', 'Dual', 'Triple', 'Quad', 'Five', 'Penta', 'Hexa'])
            & Q(spec_value__icontains='MP'))

        matching_specs = [spec for spec in specs if re.search(front_camera_pattern, spec.spec_value) and float(
            re.search(front_camera_pattern, spec.spec_value).group(0).replace(',', '')) >= front_camera]

        for spec in matching_specs:
            front_camera_result.extend([spec.device_id])
        print('##################################### FRONT CAMERA RESULT ######################################')
        print(len(front_camera_result))

    if front_camera_video:
        specs = Device_specification.objects.all().exclude(excluded)
        front_camera_video_pattern = r'(\d+)(p|K)'
        specs = specs.filter(Q(spec_category='Selfie camera')
            & Q(specification='Video'))
        units = {'p': 1, 'K': 1000}

        matching_specs = [spec for spec in specs if re.search(front_camera_video_pattern, spec.spec_value) and int(
            re.search(front_camera_video_pattern, spec.spec_value).group(1).replace(',', '')) * units[re.search(front_camera_video_pattern, spec.spec_value).group(2)] >= front_camera_video]
        
        for spec in matching_specs:
            front_camera_video_result.extend([spec.device_id])
        print('###################################### FRONT CAMERA VIDEO ######################################')
        print(len(front_camera_video_result))

    if network is not None and any(network):
        network_3g = network[0]
        network_4g = network[1]
        network_5g = network[2]

        if network_3g:
            specs = Device_specification.objects.all().exclude(excluded)
            specs = specs.filter(Q(spec_category='Network')
                & Q(specification='3G bands'))
            network_3g_pattern = r'(HSDPA|CDMA|UMTS|TD-SCDMA|EV-DO)'
            matching_specs = [spec for spec in specs if re.search(network_3g_pattern, spec.spec_value)]

            for spec in matching_specs:
                network_3g_result.extend([spec.device_id])
        print('###################################### NETWORK ######################################')
        print(len(network_3g_result))

        if network_4g:
            specs = Device_specification.objects.all().exclude(excluded)
            specs = specs.filter(Q(spec_category='Network')
                & Q(specification='4G bands'))
            network_4g_pattern = r'(LTE|(\d+))'
            matching_specs = [spec for spec in specs if re.search(network_4g_pattern, spec.spec_value)]

            for spec in matching_specs:
                network_4g_result.extend([spec.device_id])
        print('###################################### NETWORK ######################################')
        print(len(network_4g_result))

        if network_5g:
            specs = Device_specification.objects.all().exclude(excluded)
            specs = specs.filter(Q(spec_category='Network')
                & Q(specification='5G bands'))
            network_5g_pattern = r'(NSA|SA|(\d+))'

            for spec in specs:
                network_5g_result.extend([spec.device_id])
        print('###################################### NETWORK ######################################')
        print(len(network_5g_result))

    if dual_sim:
        specs = Device_specification.objects.all().exclude(excluded)
        specs = specs.filter(Q(spec_category='Body')
            & Q(specification='SIM'))
        dual_sim_pattern = r'^(Dual|Triple|Quad) SIM'

        matching_specs = [spec for spec in specs if re.search(dual_sim_pattern, spec.spec_value)]

        for spec in matching_specs:
            dual_sim_result.extend([spec.device_id])
        print('###################################### DUAL SIM ######################################')
        print(len(dual_sim_result))

    if audio_jack:
        specs = Device_specification.objects.all().exclude(excluded)
        specs = specs.filter(Q(spec_category='Sound')
            & Q(specification='3.5mm jack') | Q(spec_category='Sound') & Q(spec_value__icontains='audio jack'))

        audio_jack_pattern = r'(?i)yes|2\.5 ?mm audio jack'

        matching_specs = [spec for spec in specs if re.search(audio_jack_pattern, spec.spec_value)]

        for spec in matching_specs:
            audio_jack_result.extend([spec.device_id])
        print('###################################### AUDIO JACK ######################################')
        print(len(audio_jack_result))

    if removal_storage:
        specs = Device_specification.objects.all().exclude(excluded)
        specs = specs.filter(Q(spec_category='Memory')
            & Q(specification='Card slot'))

        removal_storage_pattern = r'(?i)micro|mini'

        matching_specs = [spec for spec in specs if re.search(removal_storage_pattern, spec.spec_value)]

        for spec in matching_specs:
            removal_storage_result.extend([spec.device_id])
        print('###################################### REMOVAL STORAGE ######################################')
        print(len(removal_storage_result))

    if any(price):
        price_min = price[0]
        price_max = price[1]
        
        specs = Device_specification.objects.all().exclude(excluded)
        specs = specs.filter(Q(spec_category='Misc', specification='Price') & (Q(spec_value__contains='₹') | Q(spec_value__contains='INR') | Q(spec_value__contains='EUR') | Q(spec_value__contains='€') | Q(spec_value__contains='Rp') | Q(spec_value__contains='£') | Q(spec_value__contains='$')))
        

        price_pattern = r'(\$|€|₹|C\$|Rp|£)(\D+)\s*(\d{1,3}(,\d{3})*[,.]?\d{0,2})|(\d{1,3}(,\d{3})*[,.]?\d{0,2})(\D+)(EUR|INR)'
        convert = {'$': 1, '€': 1.2, '₹': 0.014, '£': 1.4, 'INR': 0.014, 'EUR': 1.2, 'Rp': 0.000071, 'C$': 0.8}


        for spec in specs:
            # check if price is in USD or not
            if '$' in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(1) == '$':
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif '€' in spec.spec_value and '$' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(1) == '€':
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif '₹' in spec.spec_value and '$' not in spec.spec_value and '€' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(1) == '₹':
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif 'Rp' in spec.spec_value and '$' not in spec.spec_value and '€' not in spec.spec_value and '₹' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(1) == 'Rp':
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif '£' in spec.spec_value and '$' not in spec.spec_value and '€' not in spec.spec_value and '₹' not in spec.spec_value and 'Rp' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(1) == '£':
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif 'EUR' in spec.spec_value and '$' not in spec.spec_value and '€' not in spec.spec_value and '₹' not in spec.spec_value and 'Rp' not in spec.spec_value and '£' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(8) == 'EUR':
                    price_value = float(match.group(5).replace(',', '')) * convert[match.group(8)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue
            elif 'INR' in spec.spec_value and '$' not in spec.spec_value and '€' not in spec.spec_value and '₹' not in spec.spec_value and 'Rp' not in spec.spec_value and '£' not in spec.spec_value and 'EUR' not in spec.spec_value:
                match = re.search(price_pattern, spec.spec_value)
                if match.group(8) == 'INR':
                    price_value = float(match.group(5).replace(',', '')) * convert[match.group(8)]
                    if price_value >= price_min and price_value <= price_max:
                        price_result.extend([spec.device_id])
                    # else pass to next spec
                    else:
                        continue


        print('###################################### PRICE ######################################')
        print(len(price_result))

    if charging:
        specs = Device_specification.objects.all().exclude(excluded)
        specs = specs.filter(Q(spec_category='Battery')
            & Q(specification='Charging'))

        min_charging = 18
        charging_pattern = r'(?i)(\d+)W|(fast charging)'
        matching_specs = [spec for spec in specs if re.search(charging_pattern, spec.spec_value)]

        for spec in matching_specs:
            match = re.search(charging_pattern, spec.spec_value)
            if match:
                if match.group(1) and int(match.group(1)) >= min_charging:
                    charging_result.extend([spec.device_id])
                if match.group(2):
                    charging_result.extend([spec.device_id])
        print('###################################### CHARGING ######################################')
        print(len(charging_result))

    result = intersect_arrays(
        battery_result, ram_result, chipset_result, storage_result, screen_size_result, screen_resolution_result, rear_camera_result, rear_camera_video_result, front_camera_result, front_camera_video_result, network_3g_result, network_4g_result, network_5g_result, removal_storage_result, price_result, dual_sim_result, charging_result, audio_jack_result)

    print('###################################### RESULT ######################################')
    print(result)
    print(len(result), 'devices found')
    return result

# GET SPECS FROM FORM
def search(daily_usage, main_usage, storage_space, display_size, important_features, budget_range):
    max_specs = {
    'ram': 0,
    'battery': 0,
    'storage': 0,
    'removal_storage': False,
    'chipset': [],
    'screen_size': (0,0),
    'screen_resolution': 0,
    'rear_camera': 0,
    'rear_camera_video': 0,
    'front_camera': 0,
    'front_camera_video': 0,
    'network': (False, False, False),
    'price': (False, False),
    'dual_sim': False,
    'charging': False,
    'audio_jack': False
    }

    # STEP 1
    if daily_usage:
        if daily_usage_specs[daily_usage].get('battery'):
            max_specs['battery'] = max(max_specs['battery'], daily_usage_specs[daily_usage]['battery'])

    # STEP 2
    if main_usage:
        for item in main_usage:
            if main_usage_specs[item].get('chipset'):
                all_chipsets = max_specs['chipset'] + main_usage_specs[item]['chipset']
                get_priority = lambda x: chipset_priority[x]
                sorted_chipsets = sorted(all_chipsets, key=get_priority, reverse=True)
                max_specs['chipset'] = [chipset for chipset in sorted_chipsets if chipset not in max_specs['chipset']][:3]

            if main_usage_specs[item].get('ram'):
                max_specs['ram'] = max(max_specs['ram'], main_usage_specs[item]['ram'])
            if main_usage_specs[item].get('battery'):
                max_specs['battery'] = max(max_specs['battery'], main_usage_specs[item]['battery'])
            if main_usage_specs[item].get('network'):
                max_specs['network'] = max(max_specs['network'], main_usage_specs[item]['network'], key=sum)
            if main_usage_specs[item].get('rear_camera'):
                max_specs['rear_camera'] = max(max_specs['rear_camera'], main_usage_specs[item]['rear_camera'])
            if main_usage_specs[item].get('rear_camera_video'):
                max_specs['rear_camera_video'] = max(max_specs['rear_camera_video'], main_usage_specs[item]['rear_camera_video'])
            if main_usage_specs[item].get('front_camera'):
                max_specs['front_camera'] = max(max_specs['front_camera'], main_usage_specs[item]['front_camera'])
            if main_usage_specs[item].get('front_camera_video'):
                max_specs['front_camera_video'] = max(max_specs['front_camera_video'], main_usage_specs[item]['front_camera_video'])
            if main_usage_specs[item].get('screen_resolution'):
                max_specs['screen_resolution'] = max(max_specs['screen_resolution'], main_usage_specs[item]['screen_resolution'])
            if main_usage_specs[item].get('charging'):
                max_specs['charging'] = max(max_specs['charging'], main_usage_specs[item]['charging'])

    # STEP 3
    if storage_space:
        if storage_space_specs[storage_space].get('storage'):
            max_specs['storage'] = max(max_specs['storage'], storage_space_specs[storage_space]['storage'])

    # STEP 4
    if display_size:
        if display_size_specs[display_size].get('screen_size'):
            max_specs['screen_size'] = max(max_specs['screen_size'], display_size_specs[display_size]['screen_size'])

    # STEP 5
    if important_features:
        for item in important_features:
            if important_features_specs[item].get('chipset'):
                max_specs['chipset'] = max(max_specs['chipset'], important_features_specs[item]['chipset'], key=len)
            if important_features_specs[item].get('ram'):
                max_specs['ram'] = max(max_specs['ram'], important_features_specs[item]['ram'])
            if important_features_specs[item].get('battery'):
                max_specs['battery'] = max(max_specs['battery'], important_features_specs[item]['battery'])
            if important_features_specs[item].get('network'):
                max_specs['network'] = max(max_specs['network'], important_features_specs[item]['network'], key=sum)
            if important_features_specs[item].get('rear_camera'):
                max_specs['rear_camera'] = max(max_specs['rear_camera'], important_features_specs[item]['rear_camera'])
            if important_features_specs[item].get('rear_camera_video'):
                max_specs['rear_camera_video'] = max(max_specs['rear_camera_video'], important_features_specs[item]['rear_camera_video'])
            if important_features_specs[item].get('front_camera'):
                max_specs['front_camera'] = max(max_specs['front_camera'], important_features_specs[item]['front_camera'])
            if important_features_specs[item].get('front_camera_video'):
                max_specs['front_camera_video'] = max(max_specs['front_camera_video'], important_features_specs[item]['front_camera_video'])
            if important_features_specs[item].get('screen_resolution'):
                max_specs['screen_resolution'] = max(max_specs['screen_resolution'], important_features_specs[item]['screen_resolution'])
            if important_features_specs[item].get('charging'):
                max_specs['charging'] = max(max_specs['charging'], important_features_specs[item]['charging'])
            if important_features_specs[item].get('dual_sim'):
                max_specs['dual_sim'] = max(max_specs['dual_sim'], important_features_specs[item]['dual_sim'])
            if important_features_specs[item].get('audio_jack'):
                max_specs['audio_jack'] = max(max_specs['audio_jack'], important_features_specs[item]['audio_jack'])
            if important_features_specs[item].get('removal_storage'):
                max_specs['removal_storage'] = max(max_specs['removal_storage'], important_features_specs[item]['removal_storage'])

    # STEP 6
    if budget_range:
        if budget_range_specs[budget_range].get('price'):
            max_specs['price'] = max(max_specs['price'], budget_range_specs[budget_range]['price'])

    for key in max_specs:
        if max_specs[key] == 0:
            max_specs[key] = False


    # result = get_result(
    # max_specs['battery'], 
    # max_specs['ram'], 
    # max_specs['storage'], 
    # chipsets, 
    # max_specs['screen_size'], 
    # max_specs['screen_resolution'], 
    # max_specs['rear_camera'], 
    # max_specs['rear_camera_video'], 
    # max_specs['front_camera'], 
    # max_specs['front_camera_video'], 
    # max_specs['network'], 
    # max_specs['removal_storage'], 
    # max_specs['price'], 
    # max_specs['dual_sim'], 
    # max_specs['charging'], 
    # max_specs['audio_jack'])

    return max_specs


