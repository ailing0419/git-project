
#함수 정의
def convert_score(grade):
    match grade:
        case 'A+':
            gpa = 4.5
        case 'A':
            gpa = 4.0
        case 'B+':
            gpa = 3.5
        case 'B':
            gpa = 3.0
        case 'C+':
            gpa = 2.5
        case 'C':
            gpa = 2.0
        case 'D+':
            gpa = 1.5
        case 'D':
            gpa = 1.0
        case 'F':
            gpa = 0.0
    return gpa

#입력
archive_grade, submit_grade = 0, 0
archive_gpa, submit_gpa = 0.0, 0.0
while True:
    user_value = int(input("\n\n작업을 선택하세요.\n1.입력\n2.계산\n"))

    if user_value == 1:
        grade = int(input("\n\n학점을 입력하세요:"))
        gpa = convert_score(input("평점을 입력하세요:"))
        if gpa > 0:
            submit_grade += grade
            submit_gpa += grade * gpa
        archive_grade += grade
        archive_gpa += grade * gpa

        print("입력되었습니다.")
   #출력
    else:
        submit_gpa = round(submit_gpa / submit_grade, 2)
        archive_gpa = round(archive_gpa / archive_grade, 2)

        print("\n제출용: " + str(submit_grade) + "학점 (GPA:" + str(submit_gpa) + ")")
        print("열람용: " + str(archive_grade) + "학점 (GPA:" + str(archive_gpa) + ")")
        print("\n프로그램을 종료합니다.")
        break







