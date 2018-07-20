from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name'])<5:
            errors['name'] = 'Course name must be at least 5 characters.'
        if len(postData['desc'])<15:
            errors['desc'] = 'Course description must be at least 15 characters.'
        return errors
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
