def my_range(*args):
    ''' Function for range generator implementation '''
    args = list(args)
    if all(type(item) == int for item in args) is False:
        raise TypeError("Object cannot be interpreted as an integer")
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1

    elif len(args) == 2:
        while args[0] < args[1]:
            yield args[0]
            args[0] += 1

    elif len(args) == 3:
        if args[2] == 0:
            raise ValueError("Range() arg 3 must not be zero")
        elif args[2] > 0:
            while args[0] < args[1]:
                yield args[0]
                args[0] += args[2]

        else:
            while args[0] > args[1]:
                yield args[0]
                args[0] += args[2]
    else:
        raise TypeError("Range expected at most 3 arguments, got 4")


class MyRange():
    ''' Class for range iterator implementation'''
    def __init__(self, *args):
        self.start = 0
        self.step = 1
        if all(type(item) == int for item in args) is False:
            raise TypeError("Object cannot be interpreted as an integer")
        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        elif len(args) == 3:
            if args[2] == 0:
                raise ValueError("Range() arg 3 must not be zero")
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("Range expected at most 3 arguments, got 4")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start < self.stop:
                el = self.start
                self.start += self.step
                return el
            else:
                raise StopIteration
        else:
            if self.start > self.stop:
                el = self.start
                self.start += self.step
                return el
            else:
                raise StopIteration
