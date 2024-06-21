import  multiprocessing

import  time

# def calc_square(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('square ' + str(n*n))
#
# def calc_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('cube ' + str(n*n*n))
#
#
# if __name__ == "__main__":
#     arr = [2,5,7,9]
#     p1 = multiprocessing.Process(target=calc_square, args=(arr,))
#     p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print("Done !!!")


square_result =[]

def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square' + str(n*n))
        square_result.append(n*n)
    print("within a process result: result" + str(square_result))

if __name__ == "__main__":
    arr = [2,5,7,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p1.join()

    print("result " + str(square_result))
    # print("within a process result: result" + str(square_result))

    print("Done!!")