
data= [ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]


print('------------------Welcome---------------------')

def input_something(prompt):
   while True:
         pr=input(prompt)
         if pr.strip():
             return pr
         else:
             print('enter a valid value')

def input_int(prompt):
    while True:
        try:
            pr = int(input(prompt))
            if pr >= 1:
                return pr
            else:
                print('Enter an integer >= 1.')
        except Exception as e:
            print('Invalid input. Enter a number.')


while True:
  print('choose any option : [a]dd [l]ist [s]earch [v]iew [d]elete or [q]uit')
  select=input('Here:')
  
  if select=='a':
      mov_name= input_something('enter name: ')
      genres=input_something('enter genres:').split(',')
      year=input_something('enter release year:')
      duration=input_something('enter duration:')

      data.append({
          'name':mov_name,
          'genres':genres,
          'year':year,
          'duration':duration
      })
      print('Added Scucesfully')
    #   print(data)
      for i,j in enumerate(data):
          print(i+1,'Film:',j['name'],'Year:',j['year'],'Category:',j['genres'],'Duration:',j['duration'])
      

  elif select=='l':
       if len(data)==0:
          print('no movies')
       else:
          for i,j in enumerate (data) :
           print(i+1,'Movie:',j['name'],',','Release:',j['year'])

  elif select=='s':
      if len(data)==0:                      
          print('no movies')
      else:
          search=input('search movies:')
        #   for i,j in enumerate(data):
         
        
  elif select=='v':
      if len(data)==0:
          print('no movies')
      else:
          indx=input_int('enter the index:')
          for i,j in enumerate(data):
              if indx>len(data) and indx<=0:
                  print('invalid index')
              else:
                 if indx==i+1:
                  print(j)

  elif select=='d':
        if len(data)==0:
            print('no movies')
        else:
            p=input_int('enter index number:')
            if p>len(data):
              print('invalid index')
            else:
                data.pop(p-1)
                print('Removed Sucessfull')
                print(data)    

  elif select=='q':
      print('Goodbye !!')
      break
  else:
      print('invalid input')
          
 
  