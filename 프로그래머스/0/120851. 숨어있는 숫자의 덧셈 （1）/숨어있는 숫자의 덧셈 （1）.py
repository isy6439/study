def solution(my_string):
    answer = 0
    for letter in my_string : 
        if letter >= '0' and letter <= '9' :
            answer += int(letter)
    return answer