from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
import re
from .models import *
from .utils import get_available_ram, get_storage

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'avatar_url', 'wishlist', 'history', 'secure_question', 'secure_answer')

    def get_wishlist(self, obj):
        wishlist = obj.wishlist.all()
        return [device.id for device in wishlist]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'url', 'num_devices')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'url': instance.url,
            'num_devices': instance.num_devices,
        }

class DeviceSerializer(serializers.ModelSerializer):
    brand_id = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.SerializerMethodField()
    ram = serializers.SerializerMethodField()
    storage = serializers.SerializerMethodField()
    battery = serializers.SerializerMethodField()
    rear_camera = serializers.SerializerMethodField()
    front_camera = serializers.SerializerMethodField()
    audio_jack = serializers.SerializerMethodField()
    screen_size = serializers.SerializerMethodField()
    standby_time = serializers.SerializerMethodField()
    talk_time = serializers.SerializerMethodField()
    

    class Meta:
        model = Device
        fields = ('id', 'brand_id', 'name', 'url', 'thumbnail', 'summary', 'price', 'ram', 'storage', 'battery', 'rear_camera', 'front_camera', 'audio_jack', 'screen_size', 'standby_time', 'talk_time')

    def get_price(self, instance):
        price = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Misc', specification='Price')
        ).first()
        if price:
            price_pattern = r'(\$|€|₹|C\$|Rp|£)(\D+)\s*(\d{1,3}(,\d{3})*[,.]?\d{0,2})|(\d{1,3}(,\d{3})*[,.]?\d{0,2})(\D+)(EUR|INR)'

            convert = {'$': 1, '€': 1.2, '₹': 0.014, '£': 1.4, 'INR': 0.014, 'EUR': 1.2, 'Rp': 0.000071, 'C$': 0.8}
            match = re.search(price_pattern, price.spec_value)
            usd_flag = False
            euro_flag = False
            if '$' in price.spec_value:
                usd_flag = True
                if match:
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    price_value = round(price_value, 2)
                    if usd_flag:
                        return price_value
                    return price_value 
            if '€' in price.spec_value and usd_flag == False:
                if match:
                    price_value = float(match.group(3).replace(',', ''))  * convert[match.group(1)]
                    price_value = round(price_value, 2)
                    return price_value
            if '₹' in price.spec_value and usd_flag == False:
                if match:
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    price_value = round(price_value, 2)
                    return price_value 
            if 'EUR' in price.spec_value:
                euro_flag = True
                if match:
                    price_value = float(match.group(5).replace(',', '')) * convert[match.group(8)]
                    price_value = round(price_value, 2)
                    return price_value 
            if 'INR' in price.spec_value and euro_flag == False:
                if match:
                    price_value = float(match.group(5).replace(',', '')) * convert[match.group(8)]
                    price_value = round(price_value, 2)
                    return price_value 
            if 'Rp' in price.spec_value and usd_flag == False:
                if match:
                    price_value = float(match.group(3).replace(',', ''))  * convert[match.group(1)]
                    price_value = round(price_value, 2)
                    return price_value
            if '£' in price.spec_value and usd_flag == False:
                if match:
                    price_value = float(match.group(3).replace(',', '')) * convert[match.group(1)]
                    price_value = round(price_value, 2)
                    return price_value 

    def get_ram(self, instance):
        ram = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Memory', specification='Internal')
        ).first()
        
        if ram:
            ram = get_available_ram(ram.spec_value)
            return ram
        else:
            # Return a default value or handle the case where no results are returned
            return ['0']

    def get_storage(self, instance):
        storage = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Memory', specification='Internal')
        ).first()
        
        if storage:
            storage = get_storage(storage.spec_value)
            return storage
        return ['0']

    def get_battery(self, instance):
        battery = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Battery', specification='Type')
        ).first()
        battery = battery.spec_value
        if battery:
            battery_pattern = r'(\d+|\d+,*\d*) mAh'
            match = re.search(battery_pattern, battery)
            if match:
                battery_value = int(match.group(1).replace(',', ''))
                return battery_value
        return None

    def get_rear_camera(self, instance):
        rear_camera = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Main Camera', specification__in=['Single', 'Dual', 'Triple', 'Quad', 'Five', 'Penta', 'Hexa'])).first()
        if rear_camera:
            rear_camera = rear_camera.spec_value
            rear_camera_pattern = r'\d+(\.\d+)?(?=\sMP)'
            match = re.search(rear_camera_pattern, rear_camera)
            if match:
                rear_camera_value = float(match.group(0).replace(',', ''))
                return rear_camera_value
            
        return None
    
    def get_front_camera(self, instance):
        front_camera = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Selfie camera', specification='Single')
        ).first()
        if front_camera:
            front_camera = front_camera.spec_value
            front_camera_pattern = r'\d+(\.\d+)?(?=\sMP)'
            match = re.search(front_camera_pattern, front_camera)
            if match:
                front_camera_value = float(match.group(0).replace(',', ''))
                return front_camera_value
            
        return None

    def get_screen_size(self, instance):
        screen_size = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Display', specification='Size')
        ).first()
        if screen_size:
            screen_size = screen_size.spec_value
            screen_pattern = r'(^\d+\.\d+) inches'
            match = re.search(screen_pattern, screen_size)
            if match:
                screen_size_value = float(match.group(1).replace(',', ''))
                return screen_size_value
            
        return None

    def get_audio_jack(self, instance):
        audio_jack = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Sound', specification='3.5mm jack') | Q(device_id=instance.id, spec_category='Sound', spec_value__icontains='audio jack')
        ).first()

        audio_jack_pattern = r'(?i)yes|2\.5 ?mm audio jack'
        if audio_jack:
            audio_jack = audio_jack.spec_value
            match = re.search(audio_jack_pattern, audio_jack)
            if match:
                return True
        return False

    def get_standby_time(self, instance):
        standby_time = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Battery', specification='Stand-by')
        ).first()
        if standby_time:
            standby_time = standby_time.spec_value
            return standby_time
        return None
    
    def get_music_play(self, instance):
        music_play = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Battery', specification='Music play')
        ).first()
        if music_play:
            music_play = music_play.spec_value
            return music_play
        return None

    def get_talk_time(self, instance):
        talk_time = Device_specification.objects.filter(
            Q(device_id=instance.id, spec_category='Battery', specification='Talk time')
        ).first()
        if talk_time:
            talk_time = talk_time.spec_value
            return talk_time
        return None

    def to_representation(self, instance):
        return {
            'id': instance.id,
            # 'brand_id': instance.brand_id,
            'name': instance.name,
            'price': self.get_price(instance),
            'url': instance.url,
            'thumbnail': instance.thumbnail,
            'summary': instance.summary,
            'show': False,
            'ram': self.get_ram(instance),
            'storage': self.get_storage(instance),
            'battery': self.get_battery(instance),
            'rear_camera': self.get_rear_camera(instance),
            'front_camera': self.get_front_camera(instance),
            'screen_size': self.get_screen_size(instance),
            'audio_jack': self.get_audio_jack(instance),
            'standby_time': self.get_standby_time(instance),
            'music_play': self.get_music_play(instance),
            'talk_time': self.get_talk_time(instance),


        }

class Device_specificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_specification
        fields = ('device_id', 'spec_id', 'spec_category',
                  'specification', 'spec_value')

    def to_representation(self, instance):
        return {
            'device_id': instance.device_id,
            'spec_id': instance.spec_id,
            'spec_category': instance.spec_category,
            'specification': instance.specification,
            'spec_value': instance.spec_value,
        }


