"""
伪随机数产生方法：
    线性同余方法
    平方取中方法
    梅森旋转随机生成法
    BOX-MULLER法

"""
# 经典的随机数产生方法为是线性同余法，即Linear Congruence Generator (LCG)，由Lehmer于1951年提出。（同余：对于两个整数A、B，
# 如果它们同时除以一个自然数M的余数相同，就说A、B对于模M同余，A≡B mod M。）
# 线性同余发生器是用不连续的、分段的线性方程产生伪随机数序列的算法
# 周期太短、如果被知道一定长度的序列就能破解出所有的随机数生成序列
# 线性同余法的公式： rNew=(a*rOld+b) % (end-start)
#  其中：
#  rNew为新种子，a成为乘数，b称为增量，（end-start）称为模数，他们均为常数，然后设置rOld = rNew ，
#  一般要求用户指定种子数rOld(也叫seed)，当然也可以自由选择a和b，但是这两个数字选的不好的话，会影响数字的随机性。
#  经过数学家的计算，a,b 最好的值是： a=32310901  ,b=1729
import time
from random import randint


def lcg(start, end, seed=999999999):
    a = 32310901
    b = 1729
    rOld = seed  # 将种子seed赋值给rOld
    m = end - start  # 得到m 模数
    while True:
        rNew = int((a * rOld + b) % m)  # 开始产生随机数
        yield rNew  # 遇到yield关键字暂时挂起后面的代码，等带next(r)的调用并返回 rNew
        rOld = rNew


# 模拟使用10个不同得时间种子来生成随机数
# for i in range(10):
#     now = int(time.time()) + randint(0, 99999)
#     r = lcg(1, 10, now)
#     print("种子", now, "生成的随机数:")
#     for j in range(10):
#         # 使用next()函数循环遍历r生成器对象来得到十个随机数
#         print(next(r), end=",")
#     print()

"""
1. 从一个4位数x0开始，称为种子.
2. 将它平方得到一个8位数（必要时在前面加0）.
3. 取中间的4位数作为下一个随机数.
按上述方式进行就能得到一个数列，它是从0到9999随机出现的整数，这些整数可以换算到任何从a到b的区间，例如，若想要从0到1的数，只需用10 000除这些4位数

优点

    计算速度快
缺点

    很难说明取什么样的种子值可保证有足够长的周期
    容易退化为0或常数
    进而导致数据分布不均匀
https://blog.wjinyu.top/post/20210421-RandomSample-1/

"""


def random_mid_square(n=1, seed=None, length=4):
    '''
    平方取中法 最早由冯·诺伊曼提出的一种产生均匀伪随机数的方法
    默认生成0-1区间的数值
    :param n: 随机数个数 默认一个
    :param seed: 种子 默认使用当前时间
    :param length: 取中间几位整数 默认4位
    :return:若干个随机数
    '''
    if not seed:
        seed = str(int(time.time() * 1000))[-length:]
    seed = int(seed)
    for i in range(n):
        seed = int(seed ** 2 // pow(10, length / 2) % pow(10, length))
        yield seed / pow(10, length)


"""
梅森旋转法
缺点:
从梅森算法的结构上说，其算法完全基于二进制的按位异或
而二进制按位异或是可逆的
故算法是可逆的
这就意味着
攻击者可以从梅森算法的输出
逆推出产生该输出的内部寄存器状态
从而能预测出接下来的随机数序列
"""


def random_MT(n=1, seed=None, digits=4):
    '''
    梅森算法(Mersenne Twister) 默认生成0-1区间的数值
    :param n:随机数个数 默认一个
    :param seed:种子 默认使用当前时间
    :param digits:小数点位数
    :return:
    '''

    def twister(mt):
        for i in range(1, 624):
            y = (mt[i] & 2147483648) + (mt[(i + 1) % 624] & 2147483647)
            mt[i] = mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2:
                mt[i] = mt[i] ^ 2567483615
        return mt

    if not seed and seed != 0:
        seed = int(time.time())
    seed = int(seed)
    mt = [seed] + [0] * 623

    for i in range(1, 624):
        mt[i] = 0xFFFFFFFF & (1812433253 * (mt[i - 1] ^ (mt[i - 1] >> 30)) + i)

    for index in range(n):
        if index % 624 == 0:
            twister(mt)
        y = mt[index % 624]
        y = y ^ (y >> 11)
        y = y ^ (y << 7) & 2636928640
        y = y ^ (y << 15) & 4022730752
        y = y ^ (y >> 18)
        yield round(y / 0xFFFFFFFF, digits)


if __name__ == '__main__':
    print(list(random_mid_square(15, 2041)))
    print(list(random_MT(15)))
