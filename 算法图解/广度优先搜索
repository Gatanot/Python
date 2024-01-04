from collections import deque

def person_is_seller(name):
    return name[0]=='t'

graph = {}
graph["you"] = ["al","bo","cl"]
graph["bo"] = ["an","pe"]
graph["al"] = ["pe"]
graph["cl"] = ["th","jo"]
graph["an"] = []
graph["pe"] = []
graph["th"] = []
graph["jo"] = []

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person +" is a mango seller")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

search("you")