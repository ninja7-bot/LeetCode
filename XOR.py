def p(num1, num2):
    b2 = f'{num2:b}'
    target_count = b2.count('1')
    min_x = num1 ^ num2 
    result = None


    offset = 0
    while True:
        up = num1 + offset
        down = num1 - offset


        if up >= 0:
            b_up = f'{up:b}'
            if b_up.count('1') == target_count and up ^ num2 <= min_x:
                result = up
                min_x = up ^ num2 

        if down >= 0:
            b_down = f'{down:b}'
            if b_down.count('1') == target_count and down ^ num2 <= min_x:
                result = down
                min_x = down ^ num2 

        if result is not None:
            return result

        offset += 1


print(p(25, 72))
