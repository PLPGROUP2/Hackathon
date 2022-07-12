


 
 
def simple_interest(pricipal,time,rate):
    # print('The principal is', p)
    pricipal= int(input("enter pricipal :"))
    time=int(input('The time period is :'))
    rate=int(input('The rate of interest is :'))
    
    simpleinterest = (pricipal * time * rate)/100
     
    print('The Simple Interest is', simpleinterest)
    return 
simple_interest( 10 ,4 ,5)