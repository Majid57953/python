class newm:
    internal_count=0
    def __init__(self,mmm) :
        newm.internal_count+=1
    @classmethod
    def get_internal(cls):
        print("{} count".format(cls.internal_count))
print(newm.get_internal())
exma=newm(10)
print(newm.get_internal())
exma=newm(12)
print(newm.get_internal())