graph = {

'KYO': ['VPER', 'KJ'],
'VPER': ['DDLK', 'ATRA'],
'KJ': ['RYNA'],
'DDLK': [],
'ATRA': [],
'RYNA': [],
}

def display_graph(graph):
    for node in graph:
        print(node, "->", graph[node])
        
        display_graph(graph)
        