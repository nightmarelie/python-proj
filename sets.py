my_set = {"January", "February", "March"}

# items in a set do not have order
# items cannot be referred to by index
# items cannot be changed, only added/removed

my_set.add('April')

for item in my_set:
    print(f"{item}\n")

my_set.add('April')
print(my_set)
