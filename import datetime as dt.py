import datetime as dt
def decorator(args):
    def internal(args):
        print(args+dt.timedelta(days=3))
        
    return internal
@decorator
def todayDate(args):
    print(args)
todayDate(dt.datetime.now())