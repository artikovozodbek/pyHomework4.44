class Employee:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 20.0):
        self.name = name
        self.em_id = employee_id
        self.hour_rate = hourly_rate
        self.__working_hours = []  

    def log_hours(self, hour: int):
        if hour > 0 and hour < 24:
            self.__working_hours.append(hour)  
            # print(f"{hour} soat qo'shildi")
            return True                        
        else:
            # print("Xato son")
            return False                       

    def total_hours(self):
        return sum(self.__working_hours)       
    
    def calculate_salary(self):           
        return sum(self.__working_hours) * self.hour_rate
    
    def reset_hours(self):
        self.__working_hours.clear()


    

employee = Employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))   	# True
print(employee.log_hours(9))   	# True
print(employee.log_hours(10))  	# True
print(employee.log_hours(25))  	# False 

print(employee.total_hours())       	# 27
print(employee.calculate_salary())  	# 540.0 (27 * 20)

employee.reset_hours()
print(employee.total_hours())       	# 0
print(employee.calculate_salary())  	# 0.0