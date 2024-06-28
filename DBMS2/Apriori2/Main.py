from apriory import Apriory2

# file_path = "Apriory/retail_dataset.csv"
# file_path = "Apriory/item_set.csv"
file_path = "Apriory2/book_dataSet.csv"
min_support = 2

object_apriory = Apriory2(min_support)

item_count_dict, frequent_item_set = object_apriory.apriory_fit(file_path)

# # ****** frequent items *******#
for key, value in frequent_item_set.items():
    print('frequent {}-term set:'.format(key))
    print('-'*20)
    for itemset in value:
        print(list(itemset))
    print()


# ****** Query *******#
print("/t*****Query Section*****\n [Note: Query format A,B > C,D ]\n")
print("Enter a query to find confidence:")
query = input()
lhs, rhs = query.split('>')
lhs.strip()
rhs.strip()

lhs_items = set()
for item in lhs.split(','):
    lhs_items.add(item.strip())
rhs_items = set()
for item in rhs.split(','):
    rhs_items.add(item.strip())

# print(lhs_items, rhs_items)

up_items = lhs_items.union(rhs_items)
down_items = lhs_items
up_count = 0
down_count = 0
for items, support_count in item_count_dict.items():
    if items == up_items:
        up_count = support_count
    elif items == down_items:
        down_count = support_count
    else:
        None

# print(up_count, down_count)
print("Confidence: ", (up_count/down_count)*100, "%")
