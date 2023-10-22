target = int(input("Enter a number between 0 and 1000: ")) 
even_sum = 0
#for number in range(1,target+1):
  #if number % 2 == 0:
  #  even_sum += number

for number in range(2, target+1, 2):
  even_sum += number
print(even_sum)