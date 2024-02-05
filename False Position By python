f = [1,0,1,-2]
def func(f, x):
    sum=0
    temp=0
    for i in range(len(f)):
        sum+=f[i]*(x**(len(f)-1-temp))
        temp+=1
        
    return sum
def falseposition(f, xl, xu, epsilon):
   old_x=0

   while(True):
      new_x=(xu*func(f,xl)-xl*func(f,xu))/(func(f,xl)-func(f,xu))
      if func(f,xl)*func(f,new_x)<0:
        xu=new_x
      else:
           xl=new_x
      if abs((new_x-old_x)/new_x)*100<epsilon:
         break
      old_x=new_x
      return new_x
      x=falseposition(f, -2, 2, .005)
print('root',x)
print("f(x) at root:", func(f, x))
