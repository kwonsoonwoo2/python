def send_message():
    a = input('친구명을 입력해주세요: ')
    b = input('메시지를 입력해봐: ')
    print('{}에게 {}를 보냄'.format(a, b))

if __name__ == '__main__':
    send_message()
