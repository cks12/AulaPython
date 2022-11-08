class School:
    def __init__(self) -> None:
        self.peopleList = []
    
    def readGradeInFile(self, loc: str) -> None:
        '''
        Read file with Grade
        Set a location path with grade
        '''
        if not loc:
            return print("Err: file not found!")
        try:
            file = open(loc,'r')
            peoples = file.read().split("\n")
            self.peopleList = self.__setPeopleFromList(peoples)
        except Exception as e:
            return print(e)
        
    def __setPeopleFromList(self, peoples: list):
        people = []
        for element in peoples:
            temp = self.__people(element) if element else {}
            people.append(temp)
        return people
            
    def __people(self, string: str) -> dict:
        arr = string.split(";")
        people = {
            "ra": arr[0],
            "name":arr[1],
            "grade":[float(i) for i in arr[2:7]],
            "tests":[float(i) for i in arr[7:9]],
            "absence":float(arr[9:10][0] if arr[9:10][0] else 0)
        }
        return people
    
    def makeAprrovedStudentFile(self, loc):
        file = open(loc,'w')
        aprrovedList = self.__mapStudents()
        file.write(aprrovedList)
        try:
            pass
        except Exception as e:
            return print(e)
        
    def __mapStudents(self):
        for elemnet in self.peopleList:
            _student = self.__Student(elemnet) if elemnet else {}
        return '_aprovedList'
    
    def __Student(self, element):
        if(int(element["absence"]) > 20):
            return element["ra"], "disapproved"
        acs = element["grade"]
        acs.sort(reverse=True)
        acsMd = sum(acs[0:4]) / 4
        print(acsMd)
        return element ["ra"], "approved"

if __name__ == "__main__":
    school = School()
    school.readGradeInFile("notas.txt")
    school.makeAprrovedStudentFile("aprovados.txt")