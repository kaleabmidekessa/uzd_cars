# def main():
#     student=get_student()
    
#     print(f'{student["name"]} from {student["house"]}')

# def get_student():
#     student = {}
#     student['name'] = input('Name:')
#     student['house'] = input('House: ')
#     return student


# if __name__=='__main__':
#     main()

# def main():
#     student=get_student()
    
#     print(f'{student["name"]} from {student["house"]}')

# def get_student():
#     student = {}
#     name = input('Name:')
#     house = input('House: ')
#     return {'name': name, 'house': house}


# if __name__=='__main__':
#     main()

class Student:
    def __init__(self, name, house, patronus ):
        if not name:
            raise ValueError('Missing name')
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house}'

    def house(self):
        return self.house

    def house(self,house):
        self.house = house
    
    def charm(self):
        match self.patronus:
            case 'shit':
                return 'F_ME'
def main():
    student=get_student()
    
    print('Expect the unexpected')
    print(student)
    print(student.charm())

def get_student():
    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name,house,patronus)
    
if __name__=='__main__':
    main()
