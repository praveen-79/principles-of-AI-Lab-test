from selectors import deque

def water_jug_astar(jug1_capacity,jug2_capacity,target):
    queue=deque()
    visited=set()
    
    initial_state=(0,0)
    queue.append((initial_state))
    visited.add((initial_state))

    while queue:
        current_state=queue.popleft()
        if current_state==target:
            return current_state
        
        x,y=current_state

        if (0,y) not in visited:
            queue.append((0,y))
            visited.add((0,y))

        if (x,0) not in visited:
            queue.append((x,0))
            visited.add((x,0))

        if (jug1_capacity,y) not in visited:
            queue.append((jug1_capacity,y))
            visited.add((jug1_capacity,y))

        if (x,jug2_capacity) not in visited:
            queue.append((x,jug2_capacity))
            visited.add((x,jug2_capacity))

        pour_amount=MIN(x,jug2_capacity-y)
        if (x-pour_amount,jug2_capacity) not in visited:
            queue.append((x-pour_amount,jug2_capacity))
            visited.add((x-pour_amount,jug2_capacity))

        pour_amount=MIN(y,jug1_capacity-x)
        if (jug1_capacity,x+y-pour_amount) not in visited:
            queue.append((jug1_capacity,x+y-pour_amount))
            visited.add((jug1_capacity,x+y-pour_amount))


jug1_capacity=3
jug2_capacity=5
target=7

result= water_jug_astar(jug1_capacity,jug2_capacity,target)

print(result[0],result[1])