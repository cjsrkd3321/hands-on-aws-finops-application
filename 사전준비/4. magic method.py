class Test:
    def __init__(self, number):
        self.number = number

    def __eq__(self, value):
        return False

    def __str__(self):
        return "REX_TEST"

    def __len__(self):
        return 10


print(dir(list))
a = Test(10)
print(a == 10)
print(a)
print(len(a))
