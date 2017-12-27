
fi=open('/home/atmadeep/PycharmProjects/trials/input.txt','w+')
print(fi.read())
class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.

    """
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.")

    def print_details(self):
        """
        Prints the details of the student.
        """
        print self.name
        print self.branch
        print self.year
a=Student('Atmadeep', 'CSE', 2017)
a.print_details()