def sum_mix(arr):  # 함수 정의 시작
    total = 0  # 총합을 저장할 변수 초기화
    for i in arr:  # 배열의 각 요소에 대해 반복
        if str(i).isdigit():  # 현재 요소가 숫자인지 확인
            total += int(i)  # 숫자인 경우, 정수로 변환하여 총합에 더함
        else:  # 현재 요소가 숫자가 아닌 경우
            total += int(i)  # 문자열이지만 정수로 변환하여 총합에 더함
    return total  # 최종 총합 반환
