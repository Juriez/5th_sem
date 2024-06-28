# Caution:
# 1. You must include self before each method parameter list
# 2. Must declare the list/variable/dict outside constructor

import pprint


class AprioriAlgo:

    inventory = dict()
    products = set()
    feasible_product = dict()
    minimum_support_count = 0

    def __init__(self, min_support) -> None:
        self.minimum_support_count = min_support

    def loadData(self, fileName):

        # read query_data form file
        fp = open(fileName, 'r')
        lines = fp.readlines()

        # split query_data into dictionary
        for line in lines:
            label, items = line.split(': ')
            items = self.clean_query_data(items.split(' '))
            self.inventory[label] = items

            for item in items:
                self.products.add(item)

        self.products = sorted(list(self.products))

    def count_item_frequency(self, item_sub_set):

        if len(item_sub_set) == 1:
            item_sub_set = list(item_sub_set)

        cnt = 0
        for k, ls in self.inventory.items():
            if all(item_count in ls for item_count in item_sub_set):
                cnt += 1

        return cnt

    def checkEquality(self, items, A):
        
        flag = False
        
        for i in range(len(items)):
            if items[i] == A[i]:
                flag = True
            else:
                flag = False
                break
                
        return flag

    def clean_query_data(self, prod_list):
        """_summary_

        Args:
            prod_list (list): each products list

        Returns:
            list: White space removed list
        """
        new_list = []

        for i in prod_list:
            new_list.append(i.strip())

        return new_list

    def combinition(self, input_list, length, min_support_cnt):
        
        """
        Args:
            input_list (list): each products list
            length (int): total products
            min_support_cnt (int): minimum support count

        Returns:
            list[list]: list of all possible combination of products
        """

        # Base case: if the length of the combination is 0, return an empty list
        if length == 0:
            return [[]]

        # Recursive case: if the length of the combination is greater than 0,
        # generate all combinations of the sublists of the input list
        result = []
        for i, element in enumerate(input_list):
            sublist = input_list[i+1:]
            for combination in self.combinition(sublist, length-1, min_support_cnt):

                tmp = [element] + combination
                x = self.count_item_frequency(tmp)
                if x >= min_support_cnt:
                    result.append([element] + combination)

        return result

    def createProductList(self):
        ls = self.products

        for i in range(1, len(ls)-1):
            ls_of_product = self.combinition(ls, i, self.minimum_support_count)
            
            for product in ls_of_product:
                self.feasible_product[tuple(product)] = self.count_item_frequency(product)

        print("All Products with frequencies")
        pprint.pprint(self.feasible_product)
        return self.feasible_product

    def showSpecificProduct(self, product_amount):

        print("\nShow particular products: ")
        for items, item_count in self.feasible_product.items():
            if len(items) == product_amount:
                print(items, ':', item_count)

    def calculateConfidence(self, query):

        # query_data = input("Enter query (ex. I2 I3 | I1): ")
        print("\nCalculate Confidence: ")
        A, B = query.split('=>')
        tmp_items = set()
        
        for i in A.split(' '): tmp_items.add(i)
        for i in B.split(' '): tmp_items.add(i)
        
        AUB = sorted(tuple(tmp_items))
        A = sorted(tuple(A.strip().split(' ')))

        support_cnt_AUB = 0
        support_cnt_A = 0

        for items, item_count in self.feasible_product.items():
            
            if len(items) == len(AUB):
                if self.checkEquality(items, AUB):
                    support_cnt_AUB = item_count

            if len(items) == len(A):
                if self.checkEquality(items, A):
                    support_cnt_A = item_count

        print("P(AUB): ", AUB, support_cnt_AUB)
        print("P(A): ", A, support_cnt_A)
        
        try:
            print("\nP(B|A): ", (support_cnt_AUB / support_cnt_A)*100, "%")
        except:
            print("\nThere's no feasible product pair in the inventory")


if __name__ == '__main__':

    aprioriAlgo = AprioriAlgo(min_support=2)

    aprioriAlgo.loadData(fileName='Apriori/data.txt')
    aprioriAlgo.createProductList()
    aprioriAlgo.showSpecificProduct(product_amount=1)
    aprioriAlgo.calculateConfidence(query='Bread Butter=>Sauce')

