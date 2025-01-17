from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class Scheme(models.Model):
    scheme_id = models.AutoField(primary_key=True)
    scheme_name = models.CharField(max_length=20)

    def __str__(self):
        return self.scheme_name

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    scheme_id = models.ForeignKey(Scheme, on_delete=models.CASCADE, related_name='branches')
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch_name}-{self.scheme_id.scheme_name}"
    
class Semester(models.Model):
    sem_id = models.AutoField(primary_key=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='semesters')
    sem_number = models.IntegerField(default=1)

    def __str__(self):
        return f"Semester {self.sem_number} - {self.branch_id.branch_name} - {self.branch_id.scheme_id}"
    
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='subjects_branch')
    subject_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.subject_name} - Sem {self.semester_id.sem_number}-Branch{self.branch_id}"
    
class Notes(models.Model):
    subject_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='notes')
    notes_link = models.URLField()

    def __str__(self):
        return f"Notes for {self.semester_id.sem_number} - {self.semester_id.branch_id.branch_name}"
    
class YTLink(models.Model):
    subject_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='yt_links')
    subject_name = models.CharField(max_length=100)
    links = models.URLField()

    def __str__(self):
        return f"{self.subject_name} - Semester {self.semester_id.sem_number}"
    
class Newsletter(models.Model):
    member_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class KTUUpdates(models.Model):
    update_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    link = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
            self.send_email_to_subscribers()
        else:
            super().save(*args, **kwargs)
    def send_email_to_subscribers(self):
        subscribers = Newsletter.objects.all()
        subject = f'New Update: {self.title}'
        message = f'Check out the latest update:\n\nTitle: {self.title}\nContent: {self.content}\nLink: {self.link}'
        recipient_list = [subscriber.email for subscriber in subscribers]

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

