class luxw:
    watches_created=0
    def __init__(self,engraving) -> None:
        luxw.watches_created+=1
    @classmethod
    def get_number_of_created(cls):
        return'{} '.format(cls.watches_created)
engr=luxw('ff')
engr=luxw('ff44')
print(luxw.get_number_of_created())
