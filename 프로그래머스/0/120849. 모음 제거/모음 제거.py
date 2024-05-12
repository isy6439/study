def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = [s for s in my_string if s not in vowel]
    # for v in vowel : 
    #     my_string.replace(v, '')
        
    return ''.join(answer)