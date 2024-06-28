def count_item_frequency(sub_set):

    if len(sub_set) == 1:
        sub_set = list(sub_set)

    # print("IN: ", sub_set)

    cnt = 0
    for k, ls in inventory.items():
        if all(item_count in ls for item_count in sub_set):
            # print(ls)
            cnt += 1

    return cnt


def checkEquality(items, A):
    flag = False
    # print("--", (items))
    for i in range(len(items)):
        if items[i] == A[i]:
            flag = True
        else:
            flag = False

    return flag


def clean_query_data(prod_list):
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
        sublist = input_list[i+1:]
        if count_item_frequency(sublist) >= min_support_cnt:
            for combination in combine(sublist, length-1, min_support_cnt):

                tmp = [element] + combination
                x = count_item_frequency(tmp)
                if x >= min_support_cnt:
                    result.append([element] + combination)

    return result


if __name__ == '__main__':

    # read Support count
    min_support_cnt = int(input("Enter support count: "))

    # read query_data form file
    fp = open('apriori_algo/data.txt', 'r')
    lines = fp.readlines()

    # store query_data
    inventory = dict()
    products = set()

    # split query_data into dictionary
    for line in lines:
        label, items = line.split(': ')
        items = clean_query_data(items.split(' '))
        inventory[label] = items

        for item in items:
            products.add(item)

    products = sorted(list(products))

    # Generate all combinations of the products with product count >= min_support_cnt
    ls = products
    feasible_product = {}

    for i in range(1, len(ls)-1):
        ls_of_product = combine(ls, i, min_support_cnt)
        for product in ls_of_product:
            feasible_product[tuple(product)] = count_item_frequency(product)

    # read query size
    query = int(input("Enter item size: "))
    # count of each items
    print("Item Count: ")
    for items, item_count in feasible_product.items():
        if len(items) == query:
            print(items, item_count)

    for items, item_count in feasible_product.items():
        print(items, item_count)

    # calculate confidence
    # I1 I2 | I5
    # A | B
    # p(B|A) = support_cnt(AUB) / support_cnt(A)
    # query_data = "I2 | I1 I3"

    print("\nCalculate Confidence: ")
    A, B = query.split('|')
    tmp_items = set()
    
    for i in A.split(' '): tmp_items.add(i)
    for i in B.split(' '): tmp_items.add(i)
    
    AUB = sorted(tuple(tmp_items))
    A = sorted(tuple(A.strip().split(' ')))

    support_cnt_AUB = 0
    support_cnt_A = 0

    for items, item_count in feasible_product.items():
        
        if len(items) == len(AUB):
            if checkEquality(items, AUB):
                support_cnt_AUB = item_count

        if len(items) == len(A):
            if checkEquality(items, A):
                support_cnt_A = item_count

    print("P(AUB): ", AUB, support_cnt_AUB)
    print("P(A): ", A, support_cnt_A)
    
    try:
        print("P(B|A): ", (support_cnt_AUB / support_cnt_A)*100, "%")
    except:
        print("Divide by zero error!")


    print("\nP(AUB): ", tuple(AUB), support_cnt_AUB)
    print("P(A): ", A, support_cnt_A)
    try:
        print("P(B|A): ", (support_cnt_AUB / support_cnt_A)*100, "%")
    except ZeroDivisionError:
        print("Divide by zero error! [Element doesn't exists]")
