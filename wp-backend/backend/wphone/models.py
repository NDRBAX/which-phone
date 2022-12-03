from django.db import models

# Create your models here.
class wishlist(models.Model):
    # user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='wishlist')
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)



# step: step,
#           question: [
#             {
#               label: label,
#               checked: checked,
#             },
#           ],

class values(models.Model):
    step = models.IntegerField()
    label = models.CharField(max_length=500)
    checked = models.CharField(max_length=500)