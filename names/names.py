import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements # runtime: 4.526543617248535 seconds O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# -------My First Solution--------- runtime: 0.06606173515319824 seconds 
bst = BSTNode(names_2[500])

for i in names_2:
    bst.insert(i)

for j in names_1:
    if(bst.contains(j)):
        duplicates.append(j)
# ---------------------------------
#  
# -------My Second Solution-------- runtime: 0.636577844619751 seconds
# d = {}
# for i in names_1:
#     if(len(i) in d):
#         d[len(i)] = d[len(i)] + [i]
#     else:
#         d[len(i)] = [i]

# for j in names_2:
#     if(len(j) in d):
#         for x in d[len(j)]:
#             if x == j:
#                 duplicates.append(j)
# --------------------------------- 
#------------STRETCH--------------- runtime: 0.5516815185546875 seconds
# max_name = 0
# for i,j in enumerate(names_2):
#     if( i < len(names_2) - 1):
#         if(len(names_2[i+1]) >= len(j)):
#             max_name = names_2[i+1]

# alpha = []

# for i in range(len(max_name) + 5):
#     alpha.append(list())



# for i in names_2:
#     alpha[len(i)].append(i)

# for i in names_1:
#     for j in alpha[len(i)]:
#         if i == j:
#             duplicates.append(j)
# --------------------------------- 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
