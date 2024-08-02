from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data =((1, "CourseAdviser"),(2, "Lecturer"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminCourseAdviser(models.Model):
    id = models.AutoField(primary_key=True)
    admin= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "1. Admin"


class Lecturers(models.Model):
    id = models.AutoField(primary_key=True)
    admin= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "2. Lecturers"



class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "3. Departments"


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    lecturer_id = models.ForeignKey(Lecturers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() 

    class Meta:
        verbose_name_plural = "4. Courses"


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    profile_pic = models.FileField()
    address = models.TextField()
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    session_start = models.DateField()
    session_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() 

    class Meta:
        verbose_name_plural = "5. Students"



class Results(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    result_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "6. Results"


class Grades(models.Model):
    id  = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    result_id = models.ForeignKey(Results, on_delete=models.CASCADE)
    status= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "7. Grades"

class Temporary_Widthdrawal(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    withdrawal_date = models.CharField(max_length=200)
    message = models.TextField()
    withdrawal_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "8. Temporary_Withdrawal"


class Leave_Lecturers(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_id = models.ForeignKey(Lecturers, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=200)
    message = models.TextField()
    leave_status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "9. Leave_Lecturers"


class Notification_Students(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "10. Notification_Students"


class Notification_Lecturers(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_id = models.ForeignKey(Lecturers, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "11. Notification_Lecturers"


class Feedback_Students(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "12. Feedback_Students"

    
class Feedback_Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    lecturer_id = models.ForeignKey(Lecturers, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    class Meta:
        verbose_name_plural = "13. Feedback_Lecturer"

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminCourseAdviser.objects.create(admin=instance)
        if instance.user_type == 2:
            Lecturers.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admincourseadviser.save()
    if instance.user_type == 2:
        instance.lecturers.save()
    if instance.user_type == 3:
        instance.students.save()