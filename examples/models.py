from django.db import models


class EngineTypes(models.IntegerChoices):
    DIESEL = 1, "diesel"
    BENZ = 2, "benz"
    ELECTRIC = 3, "electric"
    OTHER = 4, "other"


class Engine(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    power = models.PositiveIntegerField()
    engine_type = models.PositiveSmallIntegerField(default=EngineTypes.DIESEL, choices=EngineTypes.choices)

    def __str__(self):
        return f"C: {self.capacity} P: {self.power} T: {self.engine_type}"


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    production_year = models.PositiveIntegerField()
    seats = models.PositiveSmallIntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    engine = models.ForeignKey(Engine, on_delete=models.DO_NOTHING)
    millage = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} - {self.model} ({self.production_year}) E: ({self.engine})"
