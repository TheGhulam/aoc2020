from aocd import get_data


def part1(data):
    count, master_count = 0, 0
    for line in data:
        count = 0
        lines = line.split(':')
        policy = lines[0]
        pword  = lines[1].strip()
        policies = policy.split(' ')
        policyword = policies[1]
        limits = policies[0].split('-')
        lower_bound, upper_bound = limits[0], limits[1]

        for letter in pword:
            if letter == policyword:
                count += 1
        if (count <= int(upper_bound)) and (count >= int(lower_bound)):
            master_count += 1
    return master_count


def part2(data):
    master_count = 0
    for line in data:
        lines = line.split(':')
        policy = lines[0]
        pword = lines[1].strip()
        policies = policy.split(' ')
        policyword = policies[1]
        limits = policies[0].split('-')
        lower_bound, upper_bound = int(limits[0]), int(limits[1])

        if (pword[lower_bound-1] == policyword) and (pword[upper_bound-1] == policyword):
            print('Rejected: '+ line + ' Why: ' + pword[lower_bound-1] + pword[upper_bound-1])
            continue
        elif (pword[lower_bound-1] == policyword) or (pword[upper_bound-1] == policyword):
            master_count += 1
            print('Accepted: ' + line)
    return master_count

# Rejected: 1-3 x: shxxx
def main():
    data = get_data(day=2, year=2020)
    data = [line for line in data.split('\n')]
    print(part1(data))
    print(part2(data))

if __name__ == '__main__': main()
