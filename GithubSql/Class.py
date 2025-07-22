class Class:
    def __init__(self,Id,Name,TeacherId):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.name = Name
        self.teacherId = TeacherId
        
        
    @staticmethod
    def CreateClass(obj):
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))

        return list
