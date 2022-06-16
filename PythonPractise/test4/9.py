# 素数判定函数
def judge_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
        else:
            return True


def main():
    s = int(input("请输入范围的起始值："))
    e = int(input("请输入范围的终止值："))
    if s % 2 == 0:
        for j in range(s, e + 1, 2):  # s是偶数，则从s开始判断
            for k in range(2, int(j / 2) + 1):  # 对每个偶数进行分解
                if judge_prime(k) and judge_prime(j - k):
                    print("%d=%d+%d" % (j, k, j - k))
                    break
    else:
        for j in range(s + 1, e + 1, 2):  # s是奇数，则从s+1开始判断
            for k in range(2, int(j / 2) + 1):  # 对每个偶数进行分解
                if judge_prime(k) and judge_prime(j - k):
                    print("%d=%d+%d" % (j, k, j - k))
                    break


if __name__ == '__main__':
    main()
