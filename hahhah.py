data={'movie':'anurag','year':4564}



if len(data)==0:
    print('no movies')
else:
   s=input('movie type:')
   for i,j in enumerate(data):
     if s in  (j['movie']):
        print('done')
     else:
        print('sorry')

