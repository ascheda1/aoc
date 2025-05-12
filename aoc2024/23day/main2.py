import sys
from collections import defaultdict
import itertools

def find_triples(connections):
    triples = set()
    for a, neighbors in connections.items():
        for x, y in itertools.combinations(neighbors, 2):
            if y in connections[x]:
                triples.add(tuple(sorted([a, x, y])))
    return triples

def grow_clique(clique, connections):
    clique = set(clique)
    while True:
        for x in clique:
            for y in connections.get(x):
                if connections.get(y).issuperset(clique):
                    clique.add(y)
                    break
            else:
                continue
            break
        else:
            break
    return clique


with open(sys.argv[1]) as f:
    connections = defaultdict(set)
    for a, b in (line.strip().split('-') for line in f):
        connections[a].add(b)
        connections[b].add(a)

triples = find_triples(connections)
print(sum(any(x[0] == 't' for x in triple) for triple in triples))

max_clique = set()
visited = set()
for triple in triples:
    if triple[0] in visited:
        continue
    clique = grow_clique(triple, connections)
    visited.update(clique)
    max_clique = max(max_clique, clique, key=len)
print(','.join(sorted(max_clique)))
