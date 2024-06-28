from collections import defaultdict

def simple_cycles(G):
    def unblock(thisnode, blocked, B):
        stack = set([thisnode])
        while stack:
            node = stack.pop()
            if node in blocked:
                blocked.remove(node)
                stack.update(B[node])
                B[node].clear()
    G = {v: set(nbrs) for (v,nbrs) in G.items()} # create a duplicate copy of the graph
    sccs = strongly_connected_components(G)
    while sccs:
        scc = sccs.pop()
        startnode = scc.pop()
        path=[startnode]
        blocked = set()
        closed = set()
        blocked.add(startnode)
        B = defaultdict(set)
        stack = [ (startnode,list(G[startnode])) ]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                if nextnode == startnode:
                    yield path[:]
                    closed.update(path)
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append( (nextnode,list(G[nextnode])) )
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            if not nbrs:
                if thisnode in closed:
                    unblock(thisnode,blocked,B)
                else:
                    for nbr in G[thisnode]:
                        if thisnode not in B[nbr]:
                            B[nbr].add(thisnode)
                stack.pop()
                path.pop()
        remove_node(G, startnode)
        H = subgraph(G, set(scc))
        sccs.extend(strongly_connected_components(H))

# Tarjan's Method for SCC
def strongly_connected_components(graph):
    index_counter, stack, lowlink, index, result  = [0], [], {}, {}, []
    # Nesting of fns
    def strong_connect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        successors = graph[node]
        for successor in successors:
            if successor not in index:
                strong_connect(successor)
                lowlink[node] = min(lowlink[node],lowlink[successor])
            elif successor in stack:
                lowlink[node] = min(lowlink[node],index[successor])
        if lowlink[node] == index[node]:
            connected_component = []
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            result.append(connected_component[:])
    for node in graph:
        if node not in index:
            strong_connect(node)
    return result

# Both below two fns expect values of G to be sets
def remove_node(G, target):
    del G[target]
    for nbrs in G.values():
        nbrs.discard(target)

# Get the subgraph of G induced by set vertices
def subgraph(G, vertices):
    return {v: G[v] & vertices for v in vertices}


# This fn will be called
# from driver.py automatically
def cycle_printing_fn(graph):
    cycle_no, string = 0,  ''
    for cycle in simple_cycles(graph):
        # Make plausible string
        for ele in cycle:
            string += "T"+str(ele+1)+" "
        print("Cycle #{0}".format(cycle_no+1)+" => "+string)
        cycle_no += 1
        string = ""     # reset string for next cycle