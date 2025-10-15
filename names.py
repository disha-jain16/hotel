# List of names  
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]  
  
# Print each name  
for name in names:  
    print(name)  
  
# Search for a name  
search_name = "Charlie"  
if search_name in names:  
    print(f"{search_name} is in the list.")  
else:  
    print(f"{search_name} is not in the list.")  
  
# Sort names alphabetically  
names.sort()  
print("Sorted names:", names)  
