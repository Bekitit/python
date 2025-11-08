def main():
    n = int(input('ensert number'))
    if(n % 2 != 0):
        print('weird1')
        main()
    elif(n % 2 == 0 and n < 5 and n > 2):
        print("Not weird1")
        main()
    elif(n % 2 == 0 and n < 20 and n > 6):
        print('weird')
        main()
    elif(n % 2 == 0 and n > 20):
        print('Not weird') 
        main()       
main()        