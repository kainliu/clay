# works, but is slow
def k_algo(edges, v):
    connected_set = []
    # [ {1,2,3}, {4,5} ]  -->  add(6,7) / add (1,4) / add(1,3)
    # always use the smallest key to name the subset
    # 
    # parent = [-1 for x in range(0, v)] # using parent to detect subset loop
    added_edges = []
    sorted_edges = sorted(edges, key = lambda t:t[2])
    print sorted_edges
    for edge in sorted_edges:
        print edge
        # add enough edges
        if len(added_edges) == v - 1:
            print 'break'
            break
        
        start_node, end_node, weight = edge
        # print 'start:', start_node, 'end:', end_node
        
        merged = []
        toMerge = []
        other = []
        for s in connected_set:
            same = s.intersection({start_node, end_node})
            
            if len(same) == 1:
                toMerge.append(s)
            elif len(same) == 2:
                merged.append(s)
                break
            elif len(same) == 0:
                other.append(s)
                
            
        if len(merged) > 0: # any 2, repeated
            continue
        elif len(other) == len(connected_set): # create new
            connected_set.append({start_node, end_node})
        else:
            connected_set = [toMerge[0].union(toMerge[1])] + other
        
        added_edges.append(weight) # add this edge into the graph
      
    print 'added edges:', added_edges 
    return sum(added_edges)


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union1(parent, x, y):
    _x = find(parent, x)
    _y = find(parent, y)
    parent[_x] = _y

def k_algo2(edges, v):
    parent = []
    for node in xrange(v + 1):
        parent.append(node)
    # print parent

    added_edges = []
    sorted_edges = sorted(edges, key = lambda t:t[2])
    # print sorted_edges
    for edge in sorted_edges:
        # print edge
        if len(added_edges) == v - 1:
            # print 'break'
            break
        
        start_node, end_node, weight = edge
        # print start_node, end_node
        x = find(parent, start_node)
        y = find(parent, end_node)

        if x!= y:
            added_edges.append(weight)
            union1(parent, x, y)
    return sum(added_edges)

print k_algo([[1, 2, 7], [1, 4, 6], [4, 2, 9], [4, 3, 8], [2, 3, 6]], 4)
print k_algo2([[1, 2, 7], [1, 4, 6], [4, 2, 9], [4, 3, 8], [2, 3, 6]], 4)