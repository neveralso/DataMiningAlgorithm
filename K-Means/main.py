# encoding: utf-8
from random import randint
from math import sqrt
import pickle
import copy


def map_split(s):
    return list(s.split())


def calc_dist(a: list, b: list):
    # print(a,b)
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sqrt(sum)


def kmeans(x):
    kernel_pos = [copy.deepcopy(x[randint(0, 149)]) for i in range(3)]

    for i in range(100):
        last_kernel_pos = [[j for j in i] for i in kernel_pos]
        kernel_sum = [[0 for i in range(4)] for i in range(3)]
        kernel_num = [0 for i in range(3)]

        for j in range(len(x)):
            min_k, min_dist = 0, 0xFFFFFFFF
            for k in range(len(kernel_pos)):
                dist = calc_dist(x[j], kernel_pos[k])
                if dist < min_dist:
                    min_k, min_dist = k, dist
            # x[j][4] = min_k

            for t in range(4):
                kernel_sum[min_k][t] += x[j][t]
            kernel_num[min_k] += 1

        for k in range(len(kernel_pos)):
            for t in range(4):
                if kernel_num[k] != 0:
                    kernel_pos[k][t] = kernel_sum[k][t]/kernel_num[k]
            break

        if kernel_pos == last_kernel_pos:
            return kernel_pos


def cal_dist_sum(kernel_pos, x):
    result = 0
    for j in range(len(x)):
        min_k, min_dist = 0, 0xFFFFFFFF
        for k in range(len(kernel_pos)):
            dist = calc_dist(x[j], kernel_pos[k])
            if dist < min_dist:
                min_k, min_dist = k, dist
        result += min_dist
    return result


def cal_flag(kernel_pos, x):
    result = []
    for j in range(len(x)):
        min_k, min_dist = 0, 0xFFFFFFFF
        for k in range(len(kernel_pos)):
            dist = calc_dist(x[j], kernel_pos[k])
            if dist < min_dist:
                min_k, min_dist = k, dist
        result.append(min_k)
    return result


def init():
    origin_file = open('iris.txt', mode='r')
    origin_data = list(map(map_split, origin_file.readlines()))

    x = []
    y = []
    for i in origin_data:
        x.append(list(map(float, i[0:4])))
        y.append(i[4:5])

    kernel_pos = kmeans(x)
    print(x)
    print(kernel_pos)

    min_dist = 0xFFFFFFF
    best_kernel_pos = []
    for i in range(100):
        # if i % 100 == 0:
        #     print(min_dist)
        kernel_pos = kmeans(x)
        dist = cal_dist_sum(kernel_pos, x)
        print(dist,kernel_pos)
        if dist < min_dist:
            min_dist = dist
            best_kernel_pos = [[j for j in i] for i in kernel_pos]
    print('best')
    print(min_dist)
    print(best_kernel_pos)
    print(cal_dist_sum(best_kernel_pos, x))
    flag = cal_flag(best_kernel_pos, x)
    print(flag)
    print(x)
    return x, y, best_kernel_pos, flag, min_dist


if __name__ == '__main__':
    (x, y, best_kernel_pos, flag, best_dist) = init()