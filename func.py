import RPi.GPIO as GPIO
import time


# #x轴发送脉冲的函数，参数时间
# def move_x(time,count):
#     "x轴运动"
#     count_x = 0
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setwarnings(False)
#     GPIO.setup(11, GPIO.OUT)#方向
#     GPIO.setup(12, GPIO.OUT)#PWM
#     while count_x < count:
#         time.sleep(time)
#         GPIO.output(12, GPIO.HIGH)
#         time.sleep(time)
#         GPIO.output(12, GPIO.LOW)
#         count += 1


def start(gpio):#gpio是指控制pwm输出的gpio口
    "时间从0.0006到0.0003，发送1600个脉冲，运动四圈,距离是20mm"
    a = [0.0003,0.0004,0.0005,0.0006]
    for i in a:
        count = 0
        while count < 400:
            GPIO.output(gpio, GPIO.HIGH)
            time.sleep(i)
            GPIO.output(gpio, GPIO.LOW)
            time.sleep(i)
            count += 1
            print("in the start-----")

def mid_run(gpio,num):#num是指脉冲个数，可以通过距离换算
    count = 0
    while count < num:
        GPIO.output(gpio, GPIO.HIGH)
        time.sleep(0.0003)
        GPIO.output(gpio, GPIO.LOW)
        time.sleep(0.0003)
        count += 1
        print("in the mid_run")

def stop(gpio):
    "停止"
    a = [0.0003,0.0004,0.0005,0.0006]
    for i in a:
        count = 0
        while count <400 :
            GPIO.output(gpio, GPIO.HIGH)
            time.sleep(i)
            GPIO.output(gpio, GPIO.LOW)
            time.sleep(i)
            count += 1
            print("in the stop")

def move(l):#l指运动的距离
    pass
def move_all(x,y,z):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT)  # 控制z轴方向 竖直方向
    GPIO.setup(12, GPIO.OUT)  # 控制x轴方向 水平方向
    GPIO.setup(7, GPIO.OUT)  # 控制y轴运动

    GPIO.setup(13, GPIO.OUT)  # 控制y轴方向
    GPIO.setup(15, GPIO.OUT)  # 控制z轴运动
    GPIO.setup(16, GPIO.OUT)  # 控制x轴运动
    #判断x,y,z正负来确认方向
    if x < 0:
        x = abs(x)
        GPIO.output(12, GPIO.LOW)
    else:
        GPIO.output(12, GPIO.HIGH)


    if y < 0:
        y = abs(y)
        GPIO.output(13, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)

    if z < 0:
        z = abs(z)
        GPIO.output(11, GPIO.LOW)
    else:
        GPIO.output(11, GPIO.HIGH)
    print(x, y, z)

    if x >= 40:
        num_x =( (x - 40) / 5 )*400
        print(num_x)  # x轴匀速运动x距离匀速运动的脉冲数
    if y >= 40:
        num_y =((y - 40) / 5)*400
        print(num_y) # y轴匀速运动y距离匀速运动的脉冲数
    if z >= 40:
        num_z = ((z - 40) / 5)*400  # z轴匀速运动z距离匀速运动的脉冲数
        print(num_z)
        # 先运动z轴


    start(15)
    mid_run(15, num_z)
    stop(15)
    # 再运动x轴
    start(16)
    mid_run(16, num_x)
    stop(16)
    # 最后运动y轴
    start(7)
    mid_run(7, num_y)
    stop(7)


