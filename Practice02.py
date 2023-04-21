import random
#변량 초기화
code, grade, score ,gpa = 0, 0, 0,0
archive_score, submit_score = 0, 0
archive_gpa, submit_gpa = 0.0, 0.0

subject_id = {}
subject_information = ()
subject_list = []
convert_score = {'A+':4.5, 'A':4.0, 'B+':3.5, 'B':3.0, 'C+':2.5, 'C':2.0, 'F':0.0}

#코드 붙이기 함수
def subject_code(subject_id,subject_name):
    if  subject_name not in subject_id.values():
        code = random.randint(10000, 99999)
    else:
        code = list(subject_id.keys())[list(subject_id.values()).index(subject_name)]
    subject_id[code] = subject_name
    return subject_id

while True:
#작업 선택
    user_value = input("\n작업을 선택하세요.\n1.입력\n2.출력\n3.계산\n")
#입력
    if user_value == '1':

        subject_name = input("과목명을 입력하세요:\n")
        subject_code(subject_id,subject_name)
        score = int(input("학점을 입력하세요:\n"))
        grade = input("평점을 입력하세요:\n")
        subject_information = tuple((code,score,grade))
        subject_list.append((subject_name,score,grade))
        gpa = float(convert_score[grade])

        if gpa > 0.0:
            submit_score += score
            submit_gpa += gpa * score
        archive_score += score
        archive_gpa += score * gpa
        print("입력되었습니다.\n")

#출력
    elif user_value == '2':
        for subject in subject_list:
            print('['+subject[0]+']'+str(subject[1])+'학점:'+subject[2])
#출력
    else:
        submit_gpa = round(submit_gpa / submit_score, 2)
        archive_gpa = round(archive_gpa / archive_score, 2)

        print("\n제출용: " + str(submit_score) + "학점 (GPA:" + str(submit_gpa) + ")")
        print("열람용: " + str(archive_score) + "학점 (GPA:" + str(archive_gpa) + ")")
        print("\n프로그램을 종료합니다.")
        print(subject_id)
        break


















#grade,score=0,0

#trance=dict({'A+':4.5,'A':4.0,'F':0.0})
#grade=int(input("학점"))
#score=input("평점")
#print(int(trance[score])*grade)







