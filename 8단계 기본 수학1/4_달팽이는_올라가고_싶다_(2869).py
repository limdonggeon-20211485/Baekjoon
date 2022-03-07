import sys
input = sys.stdin.readline
up, down, goal = map(int, input().split())
if (goal - down) % (up - down) == 0:
    print((goal - down) // (up - down))
else:
    print(((goal - down) // (up - down)) + 1)

'''
달팽이는 하루에 a미터를 올라가고, b미터를 미끄러지니, 하루에 총 a - b미터를 올라간다고 볼 수 있습니다.
이 여정이 끝나는 날에는 b미터 미끄러지는 부분이 없는 것이니, 결과적으로 v - b미터를 올라가는 것이 목표입니다.
그렇다면 a - b미터씩 쭉쭉 올라가서 a - b미터보다 작거나 같은 거리가 남은 날에 올라가면 끝이 납니다.
만일 (v - b)가 정확히 (a - b)로 나누어떨어지지 않는다면, 몫에 1을 더한 값이 정답이 됩니다.
그러나 (v - b)가 정확히 (a - b)로 나누어떨어진다면 하루를 더 계산할 필요가 없어집니다. 
이를 감안해서 처음부터 v - b에 1을 더 빼고 나눈 뒤에, 무조건 1을 더하는 것으로 정답을 구할 수 있습니다.
'''