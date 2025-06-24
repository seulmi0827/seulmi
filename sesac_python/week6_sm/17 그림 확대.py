def solution(picture, k):
    result = []
    for pixel in picture:
        str_ = ''
        for pix in pixel:
            str_ += pix * k
        result.extend([str_]*k)
    return result
