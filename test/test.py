#  Copyright (c) yibocat 2023 All Rights Reserved
#  Python: 3.10.9
#  Date: 2023/11/27 下午5:14
#  Author: yibow
#  Email: yibocat@yeah.net
#  Software: MohuPy

import mohupy as mp

if __name__ == "__main__":
    x = mp.fuzznum(3, 0.5, 0.2)
    print(x.prod())
