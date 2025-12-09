
# dict1= [ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
# { "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
# "Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
# "genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
dict1={ 1:{ 'name':'forrest gump', 'year':1994 , 'duration':142, 'geners':['Drama','Romance'], },
        2:{ 'name':'avengers endgame', 'year':2019, 'duration':181, 'geners':['Action','Adventure','Drama'] }, 
        3:{ 'name':'back to the future', 'year':1985, 'duration':114, 'geners':['Comedy','Adventure','Sci-Fi'] }, }

print('------------------Welcome---------------------')
print('choose any option : [a]dd [l]ist [s]earch [v]iew [d]elete or [q]uit')
userInput=input('Here:')
newl=[]
dict2={}
# def input_something():
#      while True:
#        dict2['name']=input('enter movie name:') 
#        if type(dict2['name'])==int:
#          print('number jai')
#        else:
#          newl.append(dict2)
#         #  print(newl)

#        dict2['geners']=input('enter genres:')
#        if type(dict2['geners'])==int:
#          print('number hai')
#        else:
#         newl.append(dict2)
#         # print(newl)


#     # a1=input('enter movie name:')
#     # a2=input('enter genres: ')

#     # if a1==int and a2==int:
#     #    print('error')
#     #    return input_something()
#     # else:
#     #    newdd={f'movie: {a1}',f'geners: {a2}',}
#     #    print(newdd)

 
# input_something()

def input_int():
           dict2['year']=input('Its Release Year:')
            
           dict2['duration']=(input('Duration:'))
         
           try:
              num=int(dict2['year'])
              num2=int(dict2['duration'])
              newl.append(dict2)
              print('new-list',newl)
           except Exception as e:
             return input_int()
             
input_int()

for i in userInput:
    if i=='a':
        # input_something()
        # input_int()
        print('hi')

    elif i=='l':
         for i,j in dict1.items():
          if dict1==0:
              print('no movies')
          else: 
            #  if j['name']!=None:
              print(i,'name',j['name'],end=' , ')
              # if j['year']!=None:
              print('year',j['year'])
  
    
    elif i=='s':
       while True:
         newl3=[]
         a=input('type term,game,gump:').lower()
         if a=='term':
             for i,j in dict1.items():
                  if 'term' in j['name']:
                      print(i,'>>',j['name'],end=' ')
                      # print(j['year'])
                      newl3.append(j['year'])
                      tp=tuple(newl3)
                      print(tp)
                      break
                  else:
                    print('Sorry No Movies')   

    elif i=='v':
       while True:
          m=(input('enter index number:'))
          for i ,j in enumerate(dict1.items(),start=1):
            if i==m:
              print(j)
              break
            # else:
              #  print('Invalid index number')   

    elif i=='d':
           p=int(input('enter index number:'))
           if p>len(dict1) :
              print('invalid index')
           else:
              dict1.pop(p-1)
              print('done')
              print(dict1)
    elif i=='q':
       print('Good Bye!!')  
    else:
       print('Invalid')

