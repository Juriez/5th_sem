from cycle_detector import Graph
from cycle_printer import *

# This dictionary will be used in printing cycles (if present)
graph = {}   
try:
    def isConflicting(instruction1, instruction2):
        if instruction1 == "zeros" or instruction2 == "zeros":
            return False
        oper1, oper2 = instruction1[0], instruction2[0]
        data_item1, data_item2 = instruction1[2], instruction2[2]
        if oper1 == "W" or oper2 == "W":
            if data_item1 == data_item2:
                return True
        return False


    file_name = input("Enter complete file path e.g. './Inputs/input.txt'")

    #  Koita transaction ache sheta count korbe.
    with open(file_name) as f:
        first_line = f.readline().split(":")
        no_of_transactions = len(first_line[1].split(','))

    # protita transaction er instruction gulur jonno 2d list created
    ls = [[] for _ in range(no_of_transactions)]

    with open(file_name) as f:
        # skip first 3 lines
        for _ in range(3):
            temp = f.readline()
        line = f.readline()
        while line:
            level1 = line.split(":")
            transaction_no = int(level1[0][1])  # e.g. extract 1 from T1
            count = 0
            for _ in range(len(ls)):
                if _ == transaction_no-1:
                    ls[_].append(level1[1][:-2])
                else:
                    ls[_].append("zeros")
            line = f.readline()

    # PRINT WHOLE SCHEDULE, S
            #schedule shoho print korte chaile nicher 3 ta comment tule dilei hbe.
    # print("SCHEDULE : ")
    # for individual_list in ls:
    #     print(individual_list)
    


    # ekhon directed graph create korbo. node hbe no of transaction er shoman
    g = Graph(no_of_transactions)
    
    L = len(ls[0])     # length of transactions
    for transaction_id in range(no_of_transactions):
        for i in range(L):
            instruction = ls[transaction_id][i]
            for j in range(no_of_transactions):
                if j == transaction_id:
                    continue
                else:
                    for k in range(i+1,L):
                        if isConflicting(instruction, ls[j][k]): #jodi conflict kore tahole ekta edge add korbe
                            g.addEdge(transaction_id,j)
                            if transaction_id not in graph.keys():
                                graph[transaction_id] = [j]
                            else:
                                graph[transaction_id].append(j)
    print("RESULT: ")
    if g.isCyclic():
        print("NOT Conflict Serializable.")
        print("Cycle(s):")
        cycle_printing_fn(graph)
    else:
        print("Conflict Serializable")
        print("Order of execution with Topological Sort")
        order = g.topologicalSort()
        for item in order:
            print("T"+str(item+1),end='->')
except:
    print("There is error in Input file format!")
