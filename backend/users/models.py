from django.db import models

class Cities(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"

class Countries(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
        

class AcademicLevels(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "AcademicLevels"

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    academic_level = models.ForeignKey(AcademicLevels, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)    