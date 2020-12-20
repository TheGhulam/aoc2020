from aocd import get_data

def part1(data):
    for num in data:
        for num1 in data:
            if num + num1 == 2020:
                return num*num1
def part2(data):
    for num in data:
        for num1 in data:
            for num2 in data:
                if num + num1 + num2 == 2020:
                    return num*num1*num2

def main():
    data = get_data(day=1, year=2020)
    data = [int(line) for line in data.split('\n')]
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
