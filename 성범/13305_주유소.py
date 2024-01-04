import sys
input = sys.stdin.readline

city = int(input())
lines = list(map(int, input().split()))
prices = list(map(int, input().split()))
money = 0
min_price= prices[0]

for i in range(city-1):
    if prices[i]<min_price:
        min_price = prices[i]
    
    money += min_price * lines[i]

print(money)