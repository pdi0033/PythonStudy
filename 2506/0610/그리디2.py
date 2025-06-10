"""
N개의 회의에 대해 각 회의의 시작시간과 종료시간이 주어진다.
한 회의실에서 사용할 수 있는 최대 회의 개수를 구하시오.
(회의가 겹치면 안 됨)

meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]

1,4
5,7
8,9
"""

def greedyMeeting(meetings):
    # 종료 시간을 기준으로 정렬
    meetings.sort(key=lambda x: x[1])
    count_list = []
    
    while len(meetings) > 0:
        count = 0
        end_time = 0
        mList = [x for x in meetings]
        for start, end in mList:
            if start >= end_time:
                count += 1
                end_time = end
                meetings.remove((start, end))
        count_list.append(count)
    return max(count_list)
        

if __name__ == "__main__":
    meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(greedyMeeting(meetings))