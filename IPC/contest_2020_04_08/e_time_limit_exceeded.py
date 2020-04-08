line = input()
X, Y = [int(n) for n in line.split()]

value = "TLE"
route_cost = []
for _ in range(X):
    line = input()
    cost, time = [int(n) for n in line.split()]
    route_cost.append([cost, time])

route_cost.sort(key=lambda x: x[0])
for cost, time in route_cost:
    if time > Y:
        continue
    else:
        value = cost
        break
print(value)