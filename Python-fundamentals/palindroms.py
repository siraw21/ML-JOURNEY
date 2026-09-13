count = 0
total = 0

def reverse_number_slice(num):
    return int(str(num)[::-1])


for i in range(1, 1000000):
   i_bin = bin(i)
   i_bin = i_bin[2:]
   if i == reverse_number_slice(i) and i_bin == i_bin[::-1]:
       print(i)
       count += 1
       total += i

print(f" Total value: {count}")
print(f" Their Sum: {total}")

