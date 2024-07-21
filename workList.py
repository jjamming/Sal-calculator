from datetime import datetime, timedelta
month = int(input("몇 월의 정보입니까? : "))
work_days = []
print("일 한 날짜 입력(공백으로 구분): ")
arr = list(map(int, input().split(' ')))
print(month,"월 근무 시간")
basic_work=0 
night_work = 0
for i in arr:
    day = datetime(datetime.now().year,month,i)
    weekday = day.weekday()
    if weekday == 6:
        print(i,"일 17:00-22:00")
    else :
        print(i,"일 17:00-23:00")
        night_work += 1
    basic_work += 5
total_work = basic_work + night_work
print(f"총 {total_work}시간입니다(기본{basic_work}+야간{night_work})")