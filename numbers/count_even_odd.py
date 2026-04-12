
def count_even_odd(n):
    even_counter =0
    odd_counter=0
    n = abs(n)
    if n == 0:
       return 1, 0
    while(n>0):      
        last_digit= n%10
        n = n // 10
        if(last_digit % 2==0):
         even_counter +=1

        else:
            odd_counter +=1
    return even_counter,odd_counter  
if __name__ == "__main__":
    num = int(input("Enter number: "))
    evens, odds = count_even_odd(num)
    print(f"Even digits: {evens}, Odd digits: {odds}")