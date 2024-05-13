from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Student_Registration,Staff_Registration,Login_Info,Question,Answer,Commend,Saved_Items,Reply
from django.db import connection

#Data_Extraction From Database
def feed():
                         questions = Question.objects.all()
                         data = []
                         for ins in questions:
                              print(ins)  
                                                      
                              question_data = {
                                   'username': ins.username,
                                     'question': ins.quesiton,
                                     'question_id':ins.question_id,
                                     'ques_obj':ins,
                                     'answers': []}
                              
                              answers = Answer.objects.filter(question_id=ins.question_id)
                              for a in answers:
                                print(a)
                                
                                answer_data = {
                                    'username': a.username,
                                     'answer': a.answer,
                                     'answer_obj':a,
                                      'comments': []}
                                comments = Commend.objects.filter(answer_id=a.id)
                                for c in comments:
                                      print(c)
                                      comment_data = {
                                        'username': c.username,
                                        'comment': c.command,
                                        'comment_obj':c,
                                        'replies': []}
                                      replies = Reply.objects.filter(command_id=c.id)
                                      for r in replies:
                                          print(r)
                                          reply_data = {
                                             'username': r.username,
                                             'reply': r.reply,
                                             'reply_obj':r}
                    
                                          comment_data['replies'].append(reply_data)
                                      answer_data['comments'].append(comment_data)
                                question_data['answers'].append(answer_data)
                              data.append(question_data)
                         return data


#Function to Post a Question in Database
def question_post(request):
     if request.method == 'POST':
        sesssion_username = request.session.get('username')
        st_register_username = Student_Registration.objects.get(username=sesssion_username)
        username =  st_register_username .username
        print(type(sesssion_username))
        print(sesssion_username)
        print(st_register_username)
        print(username)
        question =request.POST['question_content']
        ques_obj=Question(username= st_register_username, quesiton=question)
        ques_obj.save()        
        val=feed()  
        print(val)
        return render(request, 'student_index.html', {'data': val})
     
#Function to Save a Command in Database     
def command_save(request):
     if request.method =='POST':
          #Content
          content=request.POST['command_content']
          print(content)
          ans_id=request.POST['myField']
          print(ans_id)

          ans_id_val = ans_id.split('(')[-1].split(')')[0]       
          print(ans_id_val)
       
          ans=Answer.objects.get(id=ans_id_val)
          print(ans)
          #Username
          
          sesssion_username = request.session.get('username')
          st_register_username = Login_Info.objects.get(username=sesssion_username)
          print( st_register_username )
          #print(username)
          com_obj=Commend(answer_id =ans,command=content,username=st_register_username)
          com_obj.save()   
          val=feed()
          return render (request,'student_index.html',{'data': val})
 
#Function for forward the process of Command Submission in Database 
def command_post(request,answer_id):
     if request.method == 'POST':
        get_answer_id=answer_id
        print("helo")
        number_str = get_answer_id.split('(')[-1].split(')')[0]       
        print(number_str)
        #Username Process
        sesssion_username = request.session.get('username')
        st_register_username = Student_Registration.objects.get(username=sesssion_username)
        username =  st_register_username .username
        ans_obj=Answer.objects.filter(id=number_str)
        print(ans_obj)
        return render(request, 'Command.html', {'data': ans_obj})
        
        #print(type(sesssion_username))
        #print(sesssion_username)
        #print(st_register_username)
        #print(username)

        #Conetent Getting
        content = request.POST['commandText']
        buttonValue =request.POST['buttonValue']

        print(content,buttonValue)
        
        #Answer Id for the commmand
        if request.is_ajax():
        # Assuming you're expecting 'answerObj' in the POST data
            answer_obj = request.POST.get('answerObj')
        
        # Process the data as needed
        # For now, let's just print it
            print(answer_obj)
        #Save the info in database
       # ques_obj=Commend(username= st_register_username, quesiton=question)
       # ques_obj.save()


        val=feed()  
        print(val)
        return render(request, 'student_index.html', {'data': val})

#Function to forward the execution to the Answer page     
def answer_post(request,question_id):
     if request.method == 'POST':
        
        
      #  number_str = question_id.split('(')[-1].split(')')[0]       
      #  print(number_str)
        #Username Process
        sesssion_username = request.session.get('username')
        st_register_username = Staff_Registration.objects.get(username=sesssion_username)
        #username =  st_register_username .username
        sf= Question.objects.all()
       # for i in sf:
       #      print(i.question_id)

        ans_obj=Question.objects.filter(question_id=question_id)
        print(ans_obj)
        for i in ans_obj:
             print(i.quesiton)

        return render(request, 'Answer.html', {'data': ans_obj})

#Function to save the Answer in Database     
def answer_save(request):
     if request.method =='POST':
          #Content
          content=request.POST['answer_content']
          print(content)
          ans_id=request.POST['myField']
          print(ans_id)

          ans_id_val = ans_id.split('(')[-1].split(')')[0]       
          print(ans_id_val)
       
          ans=Question.objects.get(question_id=ans_id_val)
          print(ans)
          #Username
          
          sesssion_username = request.session.get('username')
          st_register_username = Login_Info.objects.get(username=sesssion_username)
          print( st_register_username )

          #print(username)
          com_obj=Answer(question_id =ans,answer=content,username=st_register_username)
          com_obj.save()   

          val=feed()
          return render (request,'staff_index.html',{'data': val})

#Function to forward the execution to Reply Page
def reply_post(request,commmand_id):
     if request.method == 'POST':
        get_com_id=commmand_id
        number_str = get_com_id.split('(')[-1].split(')')[0]       
        print(number_str)
        #Username Process
        sesssion_username = request.session.get('username')
        st_register_username = Login_Info.objects.get(username=sesssion_username)
        username =  st_register_username .username
        com_obj=Commend.objects.filter(id=number_str)
        print(com_obj)
        return render(request, 'Reply.html', {'data': com_obj})
       
#Function to forward the Reply in Database       
def reply_save(request):
     if request.method =='POST':
          #Content
          content=request.POST['reply_content']
          print(content)
          rep_id=request.POST['myField']
          print(rep_id)
          rep_id_val = rep_id.split('(')[-1].split(')')[0]       
          print(rep_id_val)
          rep =Commend.objects.get(id=rep_id_val)
          print(rep)
          #Username
          sesssion_username = request.session.get('username')
          st_register_username = Login_Info.objects.get(username=sesssion_username)
          print( st_register_username )
          #print(username)
          rep_obj=Reply(command_id =rep,reply=content,username=st_register_username)
          rep_obj.save()
                       
          val=feed()
          st= Student_Registration.objects.all()
          sf= Staff_Registration.objects.all()
          
          print(st)
          for i in st:
             if(i.username==sesssion_username):
                  return render(request, 'student_index.html', {'data': val})
          for i in sf:
             if(i.username==sesssion_username):
                  return render(request, 'staff_index.html', {'data': val})   
          
          
          
          #return render (request,'student_index.html',{'data': val})   
     






















#Function to render the home page    
def index(request):
   return render(request,"Index.html")

#Login Verification
def Login_Submmission(request):
    if request.method == 'POST':
        getusername=request.POST['username']
        getpassword=request.POST['password']
        getuser_type=request.POST['user_type']

        try:
                user = Login_Info.objects.get(username=getusername)
                #print(user.username,user.password)
                if(getusername == user.username and getpassword == user.password):
                    request.session['username'] = getusername 

                    if(getuser_type=='Student'):                       
                        val=feed()  
                        return render(request, 'student_index.html', {'data': val})
                       #print(val)
                                                  
                    if(getuser_type=='Staff'):
                     val=feed() 
                     return render(request, 'staff_index.html', {'data': val}) 
                       #print(val)
                      
        except  Login_Info.DoesNotExist:
                print("None")

        
#Function to render login page after clicking login button   
def Login(request):
   return render(request,"Login.html")

#Function to render login Failed page after submitting a invalid credentials   
def Login_Failed(request):
    return render(request,"Login_Failed.html")

#Function to return the execution to main
def BacktoHome(request):
        ses_username = request.session.get('username')
        print(ses_username)
     
        st= Student_Registration.objects.all()
        sf= Staff_Registration.objects.all()
        val=feed()  
      
        print(st)
        for i in st:
             if(i.username==ses_username):
                  return render(request, 'student_index.html', {'data': val})
        for i in sf:
             if(i.username==ses_username):
                  return render(request, 'staff_index.html', {'data': val})   

#Function to render Contact page after clicking Contact button                
def Contact(request):
    return render(request,"Contact.html")

#Function to render Register page after clicking Register button   
def Register(request):
    return render(request,"Registration.html")

#Function to render Student Registration page after clicking  RegisterationAs button   
def Student_Register(request):
    return render(request,"Student_Register.html")

#Function to render Staff Registration page after clicking  RegisterationAs button   
def Staff_Register(request):
    return render(request,"Staff_Register.html")

#Function to render After registration page after successfull Registration  
def After_Registration(request):
    return render (request,"After_Registration.html")

#Function to render Registeration page after clicking Register button   
def RegisterAs(request):
    return render(request,"RegisterAs.html")

#Function to render About page after clicking About button   
def About(request):
    return render(request,"About.html")

#Function to render Dashboard page after clicking Dashboard button   
def Dashboard(request):
    ses_username = request.session.get('username')
    print(ses_username)
    
    ques_obj=Question.objects.filter(username=ses_username)
    q=[]
    for ins in ques_obj:
        q.append(ins)
    print(q)    

    def feed():
                      #  print(ques)

                        questions = Question.objects.all()
                     #   print(questions)

                       # for ins in questions :
                        #    if ins in  ques:
                           #if ins in ques:   
                            #  print(ins)
                            #  print(question_ids)
                            #  if(ins in question_ids):                             
                        data = []
                        for ins in questions :
                            if ins in q:
                              print("it's Here")
                              print(ins)
                              question_data = {
                                   'username': ins.username,
                                     'question': ins.quesiton,
                                     'question_id':ins.question_id,
                                     'answers': []}
                              
                              answers = Answer.objects.filter(question_id=ins.question_id)
                              for a in answers:
                                answer_data = {
                                    'username': a.username,
                                     'answer': a.answer,
                                      'comments': []}
                                comments = Commend.objects.filter(answer_id=a.id)
                                for c in comments:
                                      comment_data = {
                                        'username': c.username,
                                        'comment': c.command,
                                        'replies': []}
                                      replies = Reply.objects.filter(command_id=c.id)
                                      for r in replies:
                                          reply_data = {
                                             'username': r.username,
                                             'reply': r.reply}
                    
                                          comment_data['replies'].append(reply_data)
                                      answer_data['comments'].append(comment_data)
                                question_data['answers'].append(answer_data)
                              data.append(question_data)
                        return data
         
 
   

    val=feed()
    return render(request, 'Dashboard.html', {'data': val}) 


   # answer_obj=Answer.objects.filter(username=ses_username)
   # if len(answer_obj)!= 0 :
   #     a=[]
   #     print(answer_obj)
   #     for ins in answer_obj:
   #          a.append(ins.answer_id)
   #     print(a)

   # com_obj=Commend.objects.filter(username=ses_username)
   # if len(com_obj) != 0:
   #     a=[]
   #     print(com_obj)
   #     for ins in com_obj:
   #         a.append(ins.command_id)
   #     print(a)



    #for ins in answer_obj:
    #     a.append(ins.an)
        
             

    #ans_obj=Answer.objects.filter()
#    return render(request,"student_index.html")
from django.shortcuts import render, redirect
from .models import Student_Registration, Staff_Registration

#Function to render Profile Updation page after clicking Profile button   
def Profile_Update(request):
    if request.method == 'POST':
        ses_username = request.session.get('username')
        u_name = request.POST['name']
        u_mobile = request.POST['mobile']
        u_email = request.POST['email']
        u_course = request.POST['course']

        # Check if the user is a student or staff
        if Student_Registration.objects.filter(username=ses_username).exists():
            prof_obj = Student_Registration.objects.get(username=ses_username)
        elif Staff_Registration.objects.filter(username=ses_username).exists():
            prof_obj = Staff_Registration.objects.get(username=ses_username)
        else:
            # Handle the case where the user is not found
            return render(request, "Profile_Error.html")

        # Update profile fields
        prof_obj.name = u_name
        prof_obj.mobile = u_mobile
        prof_obj.email = u_email
        prof_obj.course = u_course

        # Save the updated profile
        prof_obj.save()

        return render(request, "Profile_Success.html")

   


#Function to store the student updated profile info to Database   
def St_Profile_Update(request):
       if request.method == 'POST':
         
         u_name= request.POST['name']
         u_mobile= request.POST['mobile']
         u_email= request.POST['email']
         u_course= request.POST['course']       
         prof_obj=Student_Registration(name=u_name,mobile=u_mobile,email=u_email,course=u_course)
         prof_obj.save()   
         return render(request,"Profile_Success.html")

#Function to store the staff updated profile info to Database   
def Sf_Profile_Update(request):
       if request.method == 'POST':
         u_name= request.POST['name']
         u_mobile= request.POST['mobile']
         u_email= request.POST['email']
         u_course= request.POST['course']
         prof_obj=Staff_Registration(name=u_name,mobile=u_mobile,email=u_email,course=u_course)
         prof_obj.save()   
         return render(request,"Profile_Success.html")


       



         print(u_name)
          
         return render(request,"Profile.html")
#Function to render profile after clicking profile button   
def Profile(request):
    ses_username = request.session.get('username')
    print(ses_username)


    st_register_username= Student_Registration.objects.all()

    sf_register_username= Staff_Registration.objects.all()

    #st= Student_Registration.objects.all()
    #sf= Staff_Registration.objects.all()
    #val=feed()  
    #  
    #    print(st)
    for i in st_register_username:
        if(i.username==ses_username):
            st_data=Student_Registration.objects.filter(username=ses_username)
            print(st_data)
            return render(request, 'Profile.html', {'data': st_data})
    for i in sf_register_username:
        if(i.username==ses_username):
            sf_data=Staff_Registration.objects.filter(username=ses_username)
            print(sf_data)
            return render(request, 'Profile.html', {'data': sf_data})   


   


              #print(st_register_username)
              #info=[]
              #for a in st_register_username:
              #     print(ins.name)

                  

                  # print(ins.name)
                  # print(ins.mobile)  
             # print(info)





    for ins in sf_register_username:
         if ins.username==ses_username:
            sf_register_username=Staff_Registration.objects.get(username=ses_username)
            print(sf_register_username)
            return render(request,"Profile.html",{'sf_data' : sf_register_username})

                     
     




    
      #  sesssion_username = request.session.get('username')     
   
#Function to render if the user save the feed second time 
def Already_Saved(request):
     return render(request,'Already_Saved.html')

#Function to save the feed to the Database
def Save_Item(request,question_id):
        print("Hello")
        ses_username = request.session.get('username')
        print(ses_username)
       # print(question_id) 
        ques_obj=Question.objects.get(question_id=question_id)
        print(ques_obj)
        log_obj=Login_Info.objects.get(username=ses_username)
        #print(log_obj)
     #   saveed_obj = Saved_Items.objects.filter(question_id=ques_obj)
    #    print(saveed_obj)
        print("Hello")
        sa_ques_obj=Saved_Items.objects.filter(username=ses_username)
        print(sa_ques_obj)
        for ins in sa_ques_obj:
             if ins.question_id == ques_obj:
                  print("Matched")
                  return render(request,'Already_Saved.html')
        save_obj=Saved_Items(username=log_obj, question_id=ques_obj)
        save_obj.save()
        val=feed()  
        st= Student_Registration.objects.all()
        sf= Staff_Registration.objects.all()
        print(st)
        for i in st:
             if(i.username==ses_username):
                  return render(request, 'student_index.html', {'data': val})
        for i in sf:
             if(i.username==ses_username):
                  return render(request, 'staff_index.html', {'data': val})     
                  


      #  if(ses_username)
      #  if(st_log_obj=Student_Registration.objects.get(username=ses_username)):
      #       return render(request, 'student_index.html', {'data': val})
      #  
      #  if(sf_log_obj=Staff_Registration.objects.get(username=ses_username)):
      #       return render(request,'staff_index.html',{'data': val})
             
             
        
        
#Funtion to render the Saved_Items  data form database after clicking a saved_Items button
def Saved_Items_List(request):
    #print("Hello")
    sesssion_username = request.session.get('username')
    print(sesssion_username)
    #print(sesssion_username)
  #  log_obj=Login_Info.objects.get(username=sesssion_username)
  #  print(log_obj)
    sa_ques_obj=Saved_Items.objects.filter(username=sesssion_username)
    print("Hello")
    print(sa_ques_obj)

    ques=[]
    for ins in sa_ques_obj:
         ques.append(ins.question_id)
         print(ins.question_id)

                     
    def feed():
                      #  print(ques)

                        questions = Question.objects.all()
                     #   print(questions)

                       # for ins in questions :
                        #    if ins in  ques:
                           #if ins in ques:   
                            #  print(ins)
                            #  print(question_ids)
                            #  if(ins in question_ids):                             
                        data = []
                        for ins in questions :
                            if ins in ques:
                              print("it's Here")
                              print(ins)
                              question_data = {
                                   'username': ins.username,
                                     'question': ins.quesiton,
                                     'question_id':ins.question_id,
                                     'answers': []}
                              
                              answers = Answer.objects.filter(question_id=ins.question_id)
                              for a in answers:
                                answer_data = {
                                    'username': a.username,
                                     'answer': a.answer,
                                      'comments': []}
                                comments = Commend.objects.filter(answer_id=a.id)
                                for c in comments:
                                      comment_data = {
                                        'username': c.username,
                                        'comment': c.command,
                                        'replies': []}
                                      replies = Reply.objects.filter(command_id=c.id)
                                      for r in replies:
                                          reply_data = {
                                             'username': r.username,
                                             'reply': r.reply}
                    
                                          comment_data['replies'].append(reply_data)
                                      answer_data['comments'].append(comment_data)
                                question_data['answers'].append(answer_data)
                              data.append(question_data)
                        return data
         
 
   

    val=feed()
    return render(request, 'Saved_Items.html', {'data': val}) 
                         
               
              
               
    
    
   # for ins in sa:
      #   if(sesssion_username==ins.username and ins.question_id==)
#    print(sa)

    #sa=Saved_Items.objects.get(username=sesssion_username)
    #print(sa)
    
    
 
   
        




#Function to store the Student Registration data into Database
def st_register_submission(request):
    if request.method == 'POST':
            name=request.POST['name']
            mobile=request.POST['mobile']
            email=request.POST['email']
            username=request.POST['username']
            course=request.POST['course']        
            passkey=request.POST['password']
            print(passkey)

            stu_obj=Student_Registration(name=name,mobile=mobile,email=email,username=username,course=course,passkey=passkey)
            stu_obj.save()

            log_obj=Login_Info(username=username,password=passkey)
            log_obj.save()

            if (stu_obj and log_obj):
                return render(request,"After_Registration.html")

   # return render(request,"registeration_submission.html")
   

#Function to store the Staff Registration data into Database   
def sf_register_submission(request):
    if request.method == 'POST':
            name=request.POST['name']
            mobile=request.POST['mobile']
            email=request.POST['email']
            department=request.POST['department']
            username=request.POST['username']
            password=request.POST['password']
            sta_obj=Staff_Registration(name=name,mobile=mobile,email=email,course=department,username=username,password=password)
            sta_obj.save()
            log_obj=Login_Info(username=username,password=password)
            log_obj.save()
            if (sta_obj and log_obj):
                return render( request,"After_Registration.html")


