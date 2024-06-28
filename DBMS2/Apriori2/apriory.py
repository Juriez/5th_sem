from collections import defaultdict
import csv


class Apriory2(object):
    def __init__(self, minSupport):
        self.minSupport = minSupport

    def apriory_fit(self, filepath):
        """ this is the main method
        which runs the apriory algo
        and returns the m-lenths 
        frequent term sets"""
        transaction_list = self.get_transactions(filepath)
        item_set = self.get_unique_item_sets(
            transaction_list)  # get the sets of unique items

        self.transaction_length = len(transaction_list)
        self.item_set = item_set

        # to count every item set in transactions
        # default value is set to 0 for all now
        main_item_count_dictionary = defaultdict(int)

        # this will contain the frequent item sets
        # of 1, 2, 3 ... lengths
        main_frequent_item_set = dict()

        # get the one item frequent set
        one_item_frequent_set = self.get_item_with_min_support(
            transaction_list, item_set, main_item_count_dictionary, self.minSupport)

        # **** Main loop for apriory ****#
        k = 1
        current_frequent_item_set = one_item_frequent_set
        while current_frequent_item_set != set():
            main_frequent_item_set[k] = current_frequent_item_set
            k += 1
            current_candidate_item_set = self.get_joined_item_set(
                current_frequent_item_set, k)
            current_frequent_item_set = self.get_item_with_min_support(
                transaction_list, current_candidate_item_set, main_item_count_dictionary, self.minSupport)

        self.item_count_dictionary = main_item_count_dictionary
        self.frequent_item_set = main_frequent_item_set
        return self.item_count_dictionary, self.frequent_item_set

    def get_transactions(self, filepath):
        """ returns the transaction
        as a list of sets"""
        transaction_list = []
        with open(filepath, 'r') as f:
            r = csv.reader(f, delimiter=',')
            for line in r:
                transaction_list.append(set(line))
        return transaction_list

    def get_unique_item_sets(self, transaction_list):
        """ returns 1 item set"""
        one_item_set = set()
        for transaction in transaction_list:
            for item in transaction:
                if item not in one_item_set and item != '':
                    one_item_set.add(frozenset([item]))
        return one_item_set

    def get_joined_item_set(self, current_frequent_item_set, k):
        return set([term1.union(term2) for term1 in current_frequent_item_set for term2 in current_frequent_item_set
                    if len(term1.union(term2)) == k])

    def get_item_with_min_support(self, transaction_list, item_set, item_count_dictionary, min_support):
        """ returns frequent item set according to min support"""
        item_set_ = set()
        temp_item_count_dictionary = defaultdict(int)
        for item in item_set:
            item_count_dictionary[item] += sum(
                [1 for transaction in transaction_list if item.issubset(transaction)])
            temp_item_count_dictionary[item] += sum(
                [1 for transaction in transaction_list if item.issubset(transaction)])

        # now get the item set with min support
        for item, count in temp_item_count_dictionary.items():
            if float(count) >= min_support:
                item_set_.add(item)
            else:
                None

        return item_set_
