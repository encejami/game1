class Game:
    def __init__(self):
        while True:

            print('''
                        welcome
            1 : for even and odd Numbers
            2 : for sentence wihtout duple
            3 : for Number from zero to your number
            4 : for devided
            5 : for for devided to 100
            Exit to any other number 
            ''')
            user_choice = eval(input("Enter your choice : "))

            if user_choice == 1:
                numb=eval(input("Enter list of Numbers : "))
                self.odd_even(list(numb))
            elif user_choice==2:
                sentns=input("Enter a sentence : ")
                self.sentencc(sentns)
            elif user_choice ==3:
                endNumber =eval(input("Enter the End Number : "))
                self.numbers(endNumber) 
            elif user_choice == 4:
                s,z=eval(input("Enter two NUMbers : " ))
                self.two_num(s, z)
            elif user_choice ==5:
                s,t=eval(input("Enter two Numbers : "))
                self.num_zeroto100(s, t)
            else:
                break
       
        print("Thank yuoooooooooooooo")                
        
    def odd_even(self,x):
        even = []
        odd = []
        for i in x:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        print(f"even number are : {even} and odd number are :{odd}")

    def sentencc(self,x):
        letter = x.split(' ')
        after=[]
        for i in letter:
            if i  in (after):
                continue
            else:
                after.append(i)
        y=" ".join(after)
        print(y)

    def numbers(self,x):
        for i in range(x):
            print(i)

    def two_num (self,x,y):
        a=[]
        for i in range(y):
            if i%x==0:
                a.append(i)
            else:
                continue
        print(a)
                
    def num_zeroto100(self,x,y):
        a=[]
        for i in range(100):
            if i%x==0 and i%y==0 :
                a.append(i)
        print(a)

    

print("wwwww")
g1=Game()


