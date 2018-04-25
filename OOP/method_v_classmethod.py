class A(object):
    arg = 5000

    @classmethod
    def f1(cls, arg):
        i = 0
        for x in range(arg):
            i += x
        return i

    def f2(self, arg):
        i = 0
        for x in range(arg):
            i += x
        return i

    @classmethod
    def call1(cls, arg):
        return cls.f1(arg)

    def call2(self, arg):
        return self.f2(arg)


if __name__ == "__main__":
    a = A()
    a.f1(50000)
    a.call1(50000)
    a.call2(50000)
    a.f2(50000)
    A.f1(50000)
    # A.f2(5000.)  # won't work
