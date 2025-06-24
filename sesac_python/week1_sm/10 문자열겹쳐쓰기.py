def solution(my_string, overwrite_string, s):
    if len(my_string) > len(overwrite_string) + s :
        return my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]
    elif len(my_string) <= len(overwrite_string) + s :
        return my_string[0:s] + overwrite_string
