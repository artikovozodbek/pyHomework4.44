class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []
        self._average = 0 

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(F"{grade} bahosi qoshildi")
            self._average = sum(self.__grades) / len(self.__grades)
        else:
            print("Notogri baho")

    def calculate_average(self):
        return f"ortacha baxo: {self._average}"

    def get_status(self):
        avg = self._average
        if avg >= 90:
            return "A'lo"
        elif avg >= 80:
            return "Yaxshi"
        elif avg >= 70:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"
        


student = Student("Nodira", "S123")
student.add_grade(90)
student.add_grade(80)
print(student.calculate_average()) 
print(student.get_status())          
student.add_grade(1500)      