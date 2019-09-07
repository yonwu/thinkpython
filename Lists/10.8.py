import random


def random_bd(n):
    l = []
    for i in range(n):
        t = random.randint(1,365)
        l.append(t)
    return l


def same_bd(l):
    k = l
    k.sort()
    for i in range(len(k)-1):
        if k[i] == k[i+1]:
            return True
    return False


def count_sam_bd(n, nums_simulation):
    count = 0
    for i in range(nums_simulation):
        t = random_bd(n)
        if same_bd(t):
            count = count + 1
    return count


def prob_same_bd(n, nums_simulation):
    count = count_sam_bd(n, nums_simulation)
    return float(count / nums_simulation)


if __name__ == "__main__":
    print(count_sam_bd(23, 1000))
