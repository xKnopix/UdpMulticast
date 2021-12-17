from construct import * #https://construct.readthedocs.io/en/latest/basics.html

dataStruct = Struct("Program" / Int8ub,
                    "Data" / Int16ub,
                    "containingSomething" / Int16ub,
                    "NewFolder" / Int32ub,
                    )
class Builddata():

    def build(self, fProgram, fData, fcontainingSomething, fNewFolder):
        return dataStruct.build(dict(Program=fProgram,Data=fData,containingSomething=fcontainingSomething, NewFolder=fNewFolder))