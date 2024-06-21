# class RemoteControl():
#     def __init__(self):
#         self.channels = ["sun","vijay","star","jio"]
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.channels):
#             raise StopIteration
#
#         return self.channels[self.index]
#
# r = RemoteControl()
# itr = iter(r)
#
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# class FibonacciSeries:
#     def __init__(self):
#         self.series = [0,1,1,2,3,5,8,13,21,34,55]
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index == len(self.series):
#             raise StopIteration
#
#         return self.series[self.index]
#
# f = FibonacciSeries(10)
# itr = iter(f)
#
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
#The above thing is correct but i have predefined the number but it has to generate automatically for the given number
class FibonacciSeries:
    def __init__(self,limit):
        self.limit = limit
        self.a, self.b = 0,1

    def __iter__(self):
        self.a, self.b = 0,1
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration

        fibonacci_number = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return fibonacci_number

f = FibonacciSeries(10)
itr = iter(f)

for number in itr:
    print(number)