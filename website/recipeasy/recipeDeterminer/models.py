from django.db import models

# Create your models here.

measurementChoices = (
                        ("g","g"),
                        ("ounce", "ounce"),
                        ("ml","ml")
                     )

class Recipe(models.Model):
    name = models.CharField(max_length=100)



class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=4,decimal_places=2)
    measurement = models.CharField(max_length=100, choices = measurementChoices)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null = True)
    currentCheapestPrice = models.DecimalField(max_digits=4,decimal_places=2, null =True)

    def __str__(self):
        if self.currentCheapestPrice != None:
            return(self.name + currentCheapestPrice)
        else:
            return(self.name)
