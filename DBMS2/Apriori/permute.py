
def count_item_frequency(sub_set):
    
    if len(sub_set) == 1:
        sub_set = list(sub_set)
        
    # print("IN: ", sub_set)
    
    cnt = 0
    for k, ls in inventory.items():
        if all(value in ls for value in sub_set):
            # print(ls)
            cnt += 1
            
    return cnt 

def clean_data(prod_list):
    new_list = []
    
    for i in prod_list:
        new_list.append(i.strip())
        
    return new_list

def combine(input_list, length, min_support_cnt):
    # Base case: if the length of the combination is 0, return an empty list
    if length == 0:
        return [[]]

    # Recursive case: if the length of the combination is greater than 0,
    # generate all combinations of the sublists of the input list
    result = []
    for i, element in enumerate(input_list):
        print("I: ", i, element)
        sublist = input_list[i+1:]
        for combination in combine(sublist, length-1, min_support_cnt):
            
            tmp = [element] + combination
            x = count_item_frequency(tmp)
            if x >= min_support_cnt:
                print(tmp)
                result.append([element] + combination)
    return result  


# read data form file
fp = open('apriori_algo/data.txt', 'r')
lines = fp.readlines()

# dictionary to store data
inventory = dict()
products = set()
min_support_cnt = 2

# split data into dictionary
for line in lines:
    label, items = line.split(': ')
    items = clean_data(items.split(' '))
    inventory[label] = items
    
    for item in items:
        products.add(item)
        
        
products = sorted(list(products))
print(products)



# Test the function with a list of integers
ls = products 
ans = {}
for i in range(1, len(ls)-1):
    ls_of_product = combine(ls, i, min_support_cnt)
    for product in ls_of_product:
        ans[tuple(product)] = count_item_frequency(product)
        # print(product, count_item_frequency(product))   

# for key, value in ans.items():
#     print(key, value)