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
            people.append(temp) if temp else {}
            
        return sorted(people, key=lambda d:d["name"]) 
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
    
    def makeFile(self, aprovedFilePath: str, reprovedFilePath: str):
        try:
            __mapStudents = self.__mapStudents()
            aprovedFile = open(aprovedFilePath, "w")
            reprovedFile = open(reprovedFilePath, "w")
            aprovedFile.write(__mapStudents[1]) 
            reprovedFile.write(__mapStudents[0]) 
            
        except Exception as e:
            return print(e)
        
    def __mapStudents(self):
        reprovedBuffer = ""
        aprovedBuffer = ""
        for element in self.peopleList:
            _student = self.__Student(element) if element else {}
            
            if _student[1] == "approved":
                aprovedBuffer += f'''{str(_student[0])}\n'''
            
            if _student[1] == "disapproved":
                reprovedBuffer += f'''{str(_student[0])}\n'''
                
        return reprovedBuffer, aprovedBuffer
    
    def __Student(self, element):
        if(int(element["absence"]) > 20):
            return element["name"], "disapproved"
        
        acs = element["grade"]
        test = element["tests"]
        acs.sort( reverse=True )
        test.sort(reverse=True)
        test = test[0]
        acsMd = sum(acs[0:4]) / 4
        md = (acsMd + test) / 2
        if(md < 6):
            return element["name"], "disapproved"
        return element ["name"], "approved"

if __name__ == "__main__":
    school = School()
    school.readGradeInFile("notas.txt")
    school.makeFile("aprovados.txt","reprovados.txt")