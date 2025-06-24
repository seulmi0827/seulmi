def solution(todo_list, finished):
    dict_ = dict(zip(todo_list,finished))
    return [i for i in dict_ if dict_[i] == False]
