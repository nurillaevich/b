from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Teacher(BaseModel):
    full_name = models.CharField(max_length=212)
    profession =models.CharField(max_length=212)
    fit = models.TextField()
    image = models.ImageField(upload_to='teacher/%Y/%m/%d')

    def __str__(self):
        return self.full_name


class AboutUs(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=212)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about/%Y/%m/%d')



class Category(BaseModel):
    title = models.CharField(max_length=212)
    description = models.TextField()

class Course(BaseModel):
    title = models.CharField(max_length=212)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='course/%Y/%m/%d')

    def __str__(self):
        return self.title

class News(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=212)
    text = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d')
    date = models.CharField(max_length=212)

    def __str__(self):
        return self.text


