from django.db import models

# Shoe Model
class RunningShoe(models.Model):
    BRAND_CHOICES = [
        ('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Brooks', 'Brooks'),
        ('Saucony', 'Saucony'), ('Hoka', 'Hoka'), ('ON', 'ON')
    ]
    STRIDE_CHOICES = [('Forefoot', 'Forefoot'), ('Midfoot', 'Midfoot'), ('Heel', 'Heel')]
    PRONATION_CHOICES = [('Neutral', 'Neutral'), ('Overpronation', 'Overpronation'), ('Supination', 'Supination')]
    CUSHION_CHOICES = [('Minimalist', 'Minimalist'), ('Moderate', 'Moderate'), ('Max Cushion', 'Max Cushion')]
    FOOT_SHAPE_CHOICES = [('Narrow', 'Narrow'), ('Standard', 'Standard'), ('Wide', 'Wide')]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    stride_type = models.CharField(max_length=50, choices=STRIDE_CHOICES)
    pronation = models.CharField(max_length=50, choices=PRONATION_CHOICES)
    cushioning = models.CharField(max_length=50, choices=CUSHION_CHOICES)
    foot_shape = models.CharField(max_length=50, choices=FOOT_SHAPE_CHOICES)

# Question Model
class Question(models.Model):
    text = models.CharField(max_length=255)  # The question text

    def __str__(self):
        return self.text

# Answer Model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)  # The answer text
    filter_field = models.CharField(max_length=50)  # The field to filter shoes by (e.g., stride_type, foot_shape)
    filter_value = models.CharField(max_length=50)  # The value to filter by (e.g., 'Forefoot', 'Narrow')


    def __str__(self):
        return f"{self.text}"