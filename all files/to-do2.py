print('---------------To-do-List-----------------')
data=[]
ans=[]
def user_input(prompt):
 while True:
  pr=input(prompt)
  if pr.strip():
   return pr
  else:
   print('enter valid value !!')

def user_input2(prompt):
 while True:
     try:
         pr=int(input(prompt))
         if pr >=1 :
             return pr
         else:
            print('enter number > 1!!!')
     except Exception as e:
       print('enter a valid nuumber')
   
while True:
 print('choose Option: .[c]reate Quiz .[l]ist Quiz .[p]lay Quizz .[u]pdate Quiz .[d]elete Quiz .[e]xit')
 choose=input('Here:')

 if choose=='c':
     question=user_input('write the Question:')
     print('---Give Options---')
     opt1=user_input('opt1:')
     opt2=user_input('opt2:')
     opt3=user_input('opt3:')
     opt4=user_input('opt4:')
     answer=user_input2('Real/Correct answer: opt1 | opt2 | opt3 | opt4:')
     data.append(question)
     data.append(opt1)
     data.append(opt2)
     data.append(opt3)
     data.append(opt4)
     if answer==1:
      ans.append(answer)
      print('Added Sucessfully')
     elif answer==2:
      ans.append(answer)
      print('Added Sucessfully')
     elif answer==3:
      ans.append(answer)
      print('Added Sucessfully')
     elif answer==4:
      ans.append(answer)
      print('Added Sucessfully')
     else:
       print('Idiot!! --> Choose Between -->> 1|2|3|4 !!!!')
     
 elif choose=='l':
       if len(data)==0:
         print('Nothing to See Here')
       else:
           for i,j in enumerate(data):
            print(i+1,j)
    
 elif choose=='u':
   if not data:
     print('Nothing To See Here')
  #  else:
     
    
 elif choose=='p':
   if len(data)==None:
     print('Nothing To See Here')
   else:
     for i,j in enumerate(data[0:len(data)]):
       print(question)
       answer2=user_input2('Choose Between->>(1-4):')
       if answer2 in ans:
         print('correct')
       else:
         print('Wrong')
     
 elif choose=='d':
   if not data:
     print('Nothing TO See Here')
   else:
    for i,j in enumerate(data):
     p=user_input2('Enter the index of Question Yu Wnt to Del:') 
     data.pop(p-1)
     print('Removed Sucessfully')

 elif choose=='e':
     print('Have A Nice Day Sweety')
     break
 
 else:
   print('invalid input')

  
