def solution(triangle):
    result_tri = [triangle[0]]

    for tri in triangle[1:]:
        preview_tri = result_tri[-1]
        # print('이전층:',preview_tri)
        # print('현재층:',tri)
        present_tri = []

        #맨 앞 처리
        present_tri.append(tri[0]+preview_tri[0])
        #중간 처리
        for idx in range(1,len(preview_tri)):
            if tri[idx]+preview_tri[idx-1] > tri[idx]+preview_tri[idx]:
                present_tri.append(tri[idx]+preview_tri[idx-1])
            else:
                present_tri.append(tri[idx]+preview_tri[idx])
        #맨 뒤
        present_tri.append(tri[-1]+preview_tri[-1])

        result_tri.append(present_tri)
        preview_tri = present_tri
    return max(result_tri[-1])
