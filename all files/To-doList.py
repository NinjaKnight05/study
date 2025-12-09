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
         if pr >=0 :
             return pr
         else:
            print('enter number > 1!!!')
     except Exception as e:
       print('enter a valid nuumber')

while True:
 print('choose Option: .[c]reate Quiz .[l]ist Quiz .[p]lay Quizz .[u]pdate Quiz .[d]elete Quiz .[e]xit')
 choose=input('Here:')
 if choose=='c':
     data2=[]
     question=user_input('write the Question:')
     print('---Give Options---')
     opt1=user_input('opt1:')
     opt2=user_input('opt2:')
     opt3=user_input('opt3:')
     opt4=user_input('opt4:')
     answer=user_input2('Real/Correct answer: opt1 | opt2 | opt3 | opt4:')
     data2.append(question)
     data2.append(opt1)
     data2.append(opt2)
     data2.append(opt3)
     data2.append(opt4)
     data.append(data2)
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
   if len(data)==None:
     print('Nothing To See Here')
   else:
     indx=user_input2('Add the Question no. depends how many you added:')-1
     if indx>len(data):
        break
     else:
      indx2=user_input2('write 0 for question & 1-2-3-4 for options:')
     if indx>=5:
        print('not valid try again')
     else:
      newitem=user_input('change question/option:')
      data[indx].pop(indx2)
      data[indx].insert(indx2,newitem)
      print('Changed Sucessfully')

 elif choose=='p':
   if len(data)==None:
     print('Nothing To See Here')
   else:
     for i,j in enumerate(data[0:len(data)]):
       print(j)
       a=user_input2('choose 1-4:')
       if a in ans:
         print('Your Genious')
       else:
         print('Better Luck Next Time')
         
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

  
