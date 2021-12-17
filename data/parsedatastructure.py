from construct import *

dataStruct = Struct("C" / Struct(
    "Program" / Int8ub,
),
                    "D" / Struct(
                        "Data" / Int16ub,
                        "Something" / Struct(
                            "containing Something" / Int16ub
                        ),
                        "NewFolder" / Int32ub,
                    )
                    )


class Parsedata():

    def parse(data):
        return dataStruct.parse(data)
