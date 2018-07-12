from IPython.display import clear_output
'''
A Tic TAc Toe game which takes the input in the form of numbers and place your marker where your number is placed in your
numpad and check for win or draw each and every time a player places it's marker.finally asks to play again or not.

'''
h=''
while h!='yes' and h!='no':
    h= input ('Do you want to start the game? \nYes or No :').lower()
while h=='yes':
    

    lt1=[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','\n',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','\n',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','\n',]
    ln=['-----------\n']
    lt=lt1 + ln + lt1 +ln + lt1

    # Marking for X
    
    def playerX(n):
       
        if n==1:
            lt[87]='X'
        elif n==2:
            lt[91]='X'
        elif n==3:
            lt[95]='X'
        elif n==4:
            lt[50]='X'
        elif n==5:
            lt[54]='X'
        elif n==6:
            lt[58]='X'
        elif n==7:
            lt[13]='X'
        elif n==8:
            lt[17]='X'
        elif n==9:
            lt[21]='X'
    

     # Marking for O   
        
    def playerO(m):
        
        if m==1:
            lt[87]='O'
        elif m==2:
            lt[91]='O'
        elif m==3:
            lt[95]='O'
        elif m==4:
            lt[50]='O'
        elif m==5:
            lt[54]='O'
        elif m==6:
            lt[58]='O'
        elif m==7:
            lt[13]='O'
        elif m==8:
            lt[17]='O'
        elif m==9:
            lt[21]='O'
        
            
    
    #Check for winner
    
    def winner():
        if (lt[13]+lt[17]+lt[21]=='XXX' or lt[13]+lt[17]+lt[21]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[58]+lt[54]+lt[50]=='XXX' or lt[58]+lt[54]+lt[50]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[95]+lt[91]+lt[87]=='XXX' or lt[95]+lt[91]+lt[87]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[87]+lt[50]+lt[13]=='XXX' or lt[87]+lt[50]+lt[13]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[91]+lt[54]+lt[17]=='XXX' or lt[91]+lt[54]+lt[17]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[95]+lt[58]+lt[21]=='XXX' or lt[95]+lt[58]+lt[21]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[13]+lt[54]+lt[95]=='XXX' or lt[95]+lt[54]+lt[13]=='OOO'):
            print("You won the Game!!!")
            return True
        elif (lt[87]+lt[54]+lt[21]=='XXX' or lt[87]+lt[54]+lt[21]=='OOO'):
            print("You won the Game!!!")
            return True
        else:
            return False

    # Display board Function
    
    def display():
        st=''
        for l in lt:
            st+=l
        clear_output()
        print(st)
  
    # Main Function


    d=''
    while d.lower()!='x' and d.lower()!='o':
        d=input ('Player 1 wants to select X or O : ')
        if d.lower()=='x':
            c=0
        else:
            c=1

    print('Player 1 will go first')
    
    display()
    
    u=c+9

    while c<u:
        
        
            
        if c%2==0:
            x=10
            while x<1 or x>9:
                x=int(input('Enter the no where you want X (In range between 1-9) : '))
            playerX(x)
            
    
        else:
            y=10
            while y<1 or y>9:
                y=int(input('Enter the no where you want O (In range between 1-9) : '))
            playerO(y)
            
        display()
        
        z=winner()
        if z:
            break
        else:
            c+=1
        
    k=''
    while k.lower()!='yes' and k.lower()!='no':
        k=input('Do you want to play again? \nYes or No : ')
    
    h=k.lower()