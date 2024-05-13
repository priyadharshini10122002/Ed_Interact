from django.db import models

# Create your models here.
class Student_Registration(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    
    username=models.CharField(max_length=20,primary_key=True)
    course=models.CharField(max_length=5)
    passkey=models.CharField(max_length=20)

    def __str__(self):
        return self.username



class Staff_Registration(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    
    course=models.CharField(max_length=10)
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

    
   

class Login_Info(models.Model):

    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

    
    
class Question(models.Model):
    question_id=models.BigAutoField(primary_key=True)
    username=models.ForeignKey(Student_Registration,on_delete=models.CASCADE)
    quesiton=models.CharField(max_length=100)
    def __int__(self):
        return self.question_id
  ##  date = models.DateField(auto_now=True)
  ##  time = models.TimeField(auto_now=True)
   

    
class Answer(models.Model):
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
  ##  answer_id=models.CharField(max_length=50)
  ##  id = models.AutoField(primary_key=True, default=1)
    answer=models.CharField(max_length=500)
    username=models.ForeignKey(Login_Info,on_delete=models.CASCADE)
  ##  time=models.CharField(max_length=10)
    def __int__(self):
        return self.answer_id

class Commend(models.Model):
    answer_id=models.ForeignKey(Answer,on_delete=models.CASCADE)
  ##  command_id=models.CharField(max_length=50)
  ##  id = models.AutoField(primary_key=True, default=1)
    command=models.CharField(max_length=500)
    username=models.ForeignKey(Login_Info,on_delete=models.CASCADE)
  ##  time=models.CharField(max_length=10)
   
 
class Reply(models.Model):
    command_id=models.ForeignKey(Commend,on_delete=models.CASCADE)
   ## reply_id=models.CharField(max_length=50)
   ## id = models.AutoField(primary_key=True, default=1)
    reply=models.CharField(max_length=500)
    username=models.ForeignKey(Login_Info,on_delete=models.CASCADE)
   ## time=models.CharField(max_length=10)
   

class Saved_Items(models.Model):
    
    question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
    username=models.ForeignKey(Login_Info,on_delete=models.CASCADE)

   