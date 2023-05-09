import random

class CourseHistory:
    def __init__(self):
        self.id = random.randint(10000,100000)
        self.history = []
        self.course_id = {}
        self.submit_grade = {}
        self.archive_grade = {}

    #점수 변환 함수
    @classmethod
    def match_gpa_process(cls,grade):
        convert_gpa = {'A+': 4.5, 'A': 4.0, 'B+': 3.5,
                       'B': 3.0, 'C+': 2.5, 'C': 2.0, 'F': 0.0}
        gpa = convert_gpa[grade]
        return gpa

    #과목 코드 붙이기 함수
    def get_course_id(self,course_name):
        if course_name not in self.course_id.values():
            new_id = random.randint(10000, 100000)
            self.course_id[course_name] = new_id
            self.course_id[new_id] = course_name
            return new_id

        else:
            return self.course_id[course_name]


    #입력 함수
    def input_process(self):
        course_name = input("과목명을 입력하세요: ")
        course_id = self.get_course_id(course_name)
        credit = int(input("학점을 입력하세요: "))
        grade = input("평점을 입력하세요: ")
        gpa = self.match_gpa_process(grade)

        #열람용 학점 처리
        if course_id in self.archive_grade:
            if gpa > self.archive_grade[course_id][1]:
                self.archive_grade[course_id] = (credit, gpa)
        else:
            self.archive_grade[course_id] = (credit, gpa)

        #제출용 학점 처리
        if gpa > 0.0:
            if course_id in self.submit_grade:
                if gpa > self.submit_grade[course_id][1]:
                    self.submit_grade[course_id] = (credit, gpa)
            else:
                self.submit_grade[course_id] = (credit, gpa)

        self.history.append((course_id, credit, grade))


    #출력 함수
    def print_process(self):
        for course in self.history:
            print('[' + self.course_id[course[0]] + ']' +
                  str(course[1]) + '학점:' + course[2])

    #조회 함수
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')
        for course in self.history:
            if course_name == self.course_id[course[0]]:
                print('[' + self.course_id[course[0]] + '] '+
                      str(course[1]) + '학점: ' + course[2])
                break
        else:
            print('해당하는 과목이 없습니다.')

    #계산 함수
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0

        for course_id in self.submit_grade:
            submit_gpa += self.submit_grade[course_id][0] \
                          * self.submit_grade[course_id][1]
            submit_credit += self.submit_grade[course_id][0]

        for course_id in self.archive_grade:
            archive_gpa += self.archive_grade[course_id][0] \
                           * self.archive_grade[course_id][1]
            archive_credit += self.archive_grade[course_id][0]

        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        print('제출용: ' + str(submit_credit) + '학점' +
              '(GPA: ' + str(submit_gpa) + ')')
        print('열람용: ' + str(archive_credit) + '학점' +
              '(GPA: ' + str(archive_gpa) + ')')

#실행코드
course = CourseHistory()

while True:
    user_value = input('\n작업을 선택하세요.\n1.입력\n'
                       '2.출력\n3.조회\n4.계산\n5.종료\n')

    match user_value:
        case '1':
            course.input_process()
            print('입력되었습니다.')
            continue
        case '2':
            course.print_process()
            continue
        case '3':
            course.query_process()
            continue
        case '4':
            course.calculate_process()
            continue
        case '5':
            print('프로그램을 종료합니다.')
            break


