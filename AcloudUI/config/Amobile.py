import random
'''生成手机号码'''
def generate_phone_number2():
    first_three_digits = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                          "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                          "166", "173", "175", "176", "177", "178", "180", "181", "182", "183",
                          "184", "185", "186", "187", "188", "189", "199"]

    prefix = random.choice(first_three_digits)
    suffix = ''.join(random.choice('0123456789') for _ in range(8))
    return prefix + suffix
