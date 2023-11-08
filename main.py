def collatz_sequence(n):
    collatz_list = list()
    steps = 0
    while n != 1:
        collatz_list.append(n)
        if n % 2 == 0:
            n = n//2
        else:
            n = (3*n)+1
        steps += 1
    l = len(collatz_list)
    return l


num_numbers = int(input())

for i in range(num_numbers):

    input_number = int(input())
    sequence_lenght = collatz_sequence(input_number)
    print(
        f"{sequence_lenght}")
