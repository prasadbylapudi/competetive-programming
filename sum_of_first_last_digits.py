

x=int(input())
last_digit=x%10;
while(x>=10):
    x=x//10
    
sum_of_first_last_digit=x+last_digit;

print(sum_of_first_last_digit)

