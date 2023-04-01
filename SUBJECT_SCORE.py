
TOTAL_GRADE = 0                     #열람용 학점 초기화
TOTAL_GRADE2 = 0                    #제출용 학점 초기화
SUBJECT_SCORE = 0                   #평점 환산 합계 초기화
VALUE = 0                           #(교과목별 평점 * 학점)의 총합계 초기화

answer = int(input("작업을 선택하세요.\n1.입력\n2.계산\n"))

#입력 작업 선택시 학점 및
#평점 입력 ,저장,총합 계산후 변수에 저장
#저장 끝난후 반복
while answer == 1:
    print("\n학점을 입력하세요:")
    grade = int(input())
    grade_2 = grade
    TOTAL_GRADE += grade
    print("평점을 입력하세요:")
    subject_score = input()

    if subject_score == 'A+':       #학점 구분 및 환산
        score = 4.5
    elif subject_score == 'A':
        score = 4.0
    elif subject_score == 'B+':
        score = 3.5
    elif subject_score == 'B':
        score = 3.0
    elif subject_score == 'C+':
        score = 2.5
    elif subject_score == 'C':
        score = 2.0
    elif subject_score == 'D+':
        score = 1.5
    elif subject_score == 'D':
        score = 1.0
    else:
        score = 0.0
        grade_2 = 0

    TOTAL_GRADE2 += grade_2
    SUBJECT_SCORE += score
    VALUE += grade * score
    print("입력되었습니다.")
    answer = int(input("\n\n작업을 선택 하세요.\n1.입력\n2.계산\n"))


    #계산 작업 선택시 평균 GPA계산 후
    # 출력 및 반복 정지
    if answer == 2:
        AVERAGE_SCORE = round(VALUE / TOTAL_GRADE, 2)               #열람용 GPA계산 및 소수점아래 2자리까지 보류
        AVERAGE_SCORE2 = round(VALUE / TOTAL_GRADE2, 2)             #제출용 GPA계산 및 소수점아래 2자리까지 보류
        print("\n제출용: " + str(TOTAL_GRADE2) + "학점 (GPA:" + str(AVERAGE_SCORE2) + ")")
        print("열람용: " + str(TOTAL_GRADE) + "학점 (GPA:" + str(AVERAGE_SCORE) + ")")
        print("\n프로그램을 종료합니다.")
        break

    continue







