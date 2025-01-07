# defaultdict와 lambda를 활용한 문제 2개 (상세 문제 예시)
# 기본값이 0인 defaultdict를 활용한 문제

# 문제: 주어진 숫자 리스트에서 각 숫자의 빈도를 계산하세요.
# 예:
# python
# 코드 복사
# from collections import defaultdict
# freq_dict = defaultdict(lambda: 0)
# nums = [1, 2, 2, 3, 3, 3]
# # 여기에 nums 리스트의 빈도를 계산하도록 코드를 작성하세요.
# print(freq_dict)  # 출력: {1: 1, 2: 2, 3: 3}

# 단어의 첫 글자를 기준으로 단어를 그룹화
# 주어진 단어 리스트를 첫 글자별로 그룹화하세요.
# 예:

# python
# 코드 복사
# from collections import defaultdict
# words = ["apple", "banana", "apricot", "blueberry", "cherry"]
# # 결과: {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
# 숫자 리스트를 짝수와 홀수로 분리
# 숫자 리스트를 짝수와 홀수로 분리하여 defaultdict에 저장하세요.
# 예:

# python
# 코드 복사
# from collections import defaultdict
# nums = [1, 2, 3, 4, 5, 6]
# # 결과: {"even": [2, 4, 6], "odd": [1, 3, 5]}
