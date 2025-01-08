'''
ex:2
from functools import reduce
numbers=[1,2,3,4,5]
squared_no=list(map(lambda x:x*x, numbers))
print(squared_no)
odd_sq_no=list(filter(lambda x: x%2!=0, squared_no))
print(odd_sq_no)
sum_odd_sq= reduce(lambda x,y:x+y,odd_sq_no)
print(sum_odd_sq)

'''
'''
ex 3:
from functools import reduce

# Input: List of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]

# Step 1: Flatten the list using reduce
flattened_list = reduce(lambda acc, elem: acc + elem, list_of_lists)

# Step 2: Find the maximum value
max_value = max(flattened_list)

# Print the results
print("Flattened List:", flattened_list)
print("Maximum Value:", max_value)
'''
'''ex5:
from datetime import datetime
import random
now=datetime.now()
formated_datetime=now.strftime("%Y-%m-%d_%H%M%S")
random_int=random.randint(1000,9999)
file_name=f"file_{formated_datetime}_{random_int}.txt"

with open(file_name,"w") as file:
    file.write("hello world!")
print(f"file saved as:{file_name} ")
'''
import argparse
import random
import string

# Step 1: Set up argparse to accept --length argument
parser = argparse.ArgumentParser(description="Generate a random password")
parser.add_argument("--length", type=int, default=8, help="Length of the random password (default: 8)")

# Step 2: Parse the arguments
args = parser.parse_args()

# Step 3: Generate the random password
password_length = args.length
password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

# Step 4: Print the generated password
print(f"Generated password: {password}")
