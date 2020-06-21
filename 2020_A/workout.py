import heapq

def get_max_diff(m,k):
    
    d = []
    p = m[0]
    for i in range(1, len(m)):
        d.append(-1*(m[i]-p))
        p = m[i]
    
    heapq.heapify(d)

    for i in range(k):
        largest = heapq.heappop(d)
        a = int(largest/2)
        b = largest - a
        heapq.heappush(d, a)
        heapq.heappush(d, b)

        # print(d)
    return -1*d[0]

# t = int(input())
# for _ in range(t):
#     n,k = list(map(int, input().split()))
#     m = list(map(int, input().split()))
#     result = get_max_diff(m,k)
#     print("Case #{}: {}".format(_+1, result))

tests = [
    [[10,13,15,16,17],2],
    [[9,10,20,26,30],6],
    [[1,2,3,4,5,6,7,10], 3],
    [[1,3], 1]
]

for i, test in enumerate(tests):
    result = get_max_diff(test[0], test[1])
    print("Case {}: {}".format(i+1, result))