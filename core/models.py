from django.db import models


class Flatmate(models.Model):
    """Class to represent a flatmate who lives in the flat and pays a share of the bill."""
    
    name = models.CharField(max_length=50)
    days_in_house = models.IntegerField()
    
    def pays(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return f'{bill.amount * weight:.2f}'
    
    def __str__(self):
        return self.name


class Bill(models.Model):
    """Class to represent a bill, with a total amount and period of the bill."""
    
    amount = models.FloatField()
    period = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Bill: {self.amount} for {self.period}'
    
    def __repr__(self):
        return f'Bill: {self.amount} for {self.period}'
