class Employee:
    employees = []

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    def print_info(self):
        print('Employee info: {} - {} - {}'.format(self.id, self.name, self.salary))    
    
    @classmethod
    def add_employee(cls, e):
        cls.employees.append(e)

    @classmethod
    def remove_employee(cls, id):
        cls.employees = [ee for ee in cls.employees if ee.id != id]

    @classmethod
    def list_employees(cls):
        for ee in cls.employees:
            print('---------- Employee infomation -----------')
            print('name: {}'.format(ee.name))
            print('id: {}'.format(ee.id)) 
            print('salary: {}'.format(ee.salary))
            print('------------------------------------------')



def print_menu():
    print('---------------------')
    print('1 - list employees')
    print('2 - add employee')
    print('3 - remove employee')
    print('4 - exit')


if __name__ == '__main__':
    while True:
        print_menu()
        
        option = int(input('Select an option: '))
	
        if option == 1:
            Employee.list_employees()
        elif option == 2:
            name = input('Introduce the name of the new employee: ')
            id = input('Introduce the id of the new employee: ')
            salary = input('Introduce the salary: ')

            ee = Employee(id,name, salary)
            Employee.add_employee(ee)
        elif option == 3:
            id = input('Introduce employee id: ')
            ee = [item for item in Employee.employees if item.id == id][0]
            ee.print_info()
            option = input('are you sue you want to remove the employee? (y/n)')
            if option == 'y':
                Employee.remove_employee(id)
        else:
            break
