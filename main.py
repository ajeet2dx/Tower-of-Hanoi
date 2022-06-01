# Tower of Hanoi
def tower_of_hanoi(n,A,B,C):
    if n == 1:
        print(A,'->',B)
        return
    tower_of_hanoi(n-1,A,C,B)
    tower_of_hanoi(1,A,B,C)
    tower_of_hanoi(n-1,C,B,A)

def main():
    n = int(input('Enter number of disk '))
    tower_of_hanoi(n,'A','B','C')

if __name__ == '__main__':
    main()