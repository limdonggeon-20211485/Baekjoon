import sys
input = sys.stdin.readline
number = int(input())
for i in range(number):
    floor_count, room_count, customer_count = map(int, input().split())
    if customer_count % floor_count == 0:            #손님 번호와 층 수가 같으면 (손님번호 / 층 개수)가 방 번호 (ex)층이 6개고 6번 손님이면 1호
        room_number = customer_count//floor_count   
    else:                                            #손님 번호와 층 수가 같지 않으면 (손님번호 // 총 개수)+1이 방 번호
        room_number = customer_count//floor_count + 1
    if customer_count % floor_count == 0:            #손님 번호와 층 수가 같으면 층 개수 가 층임 (ex)층이 6개고 12번 손님이면 6층
        floor = floor_count
    else:
        floor = customer_count % floor_count         #손님 번호와 층 수가 같지 않으면 (손님번호 % 층) 개수 (ex)층이 6개고 7번 손님이면 1층
    if room_number >=10:
        print(str(floor) + str(room_number))           #호수가 10이 넘으면 그냥 쓰고 10 안 넘으면 층과 호수 사이에 0 넣어주기
    else:
        print(str(floor) + '0' + str(room_number))