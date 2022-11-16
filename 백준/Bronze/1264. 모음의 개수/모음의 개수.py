while True:
    line = input()
    if line == "#":
        break
    else:
        answer = 0
        for character in line.lower():
            if character in "aeiou":
                answer += 1
                
        print(answer)