import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
         
    def display(self):
        print('name :',self.name)
        print('username :', self.username)
        
class Post:
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.author = username

def member_input(total_member_ls,total_id_ls):
    name = input('name을 입력하세요 : ')
    username = input('username을 입력하세요 : ')
    while username in total_id_ls:
        username = input('username을 다시 입력하세요 : ')
        if not username:
            break
    password = input('password를 입력하세요 : ')
    hashed_password = hashlib.sha256(password.encode())
    hex_dig = hashed_password.hexdigest()
    
    my_instance = Member(name,username,hex_dig)
    
    total_id_ls.append(username)
    total_member_ls.append(my_instance)
    
    return total_member_ls, total_id_ls

def post_input(total_post_ls,total_id_ls):
    title = input('title을 입력하세요 : ')
    content = input('content을 입력하세요 : ')
    author = input('author(ID)을 입력하세요 : ')
    while author not in total_id_ls:
        username = input('author(ID)을 다시 입력하세요 : ')
        if not username:
            break 
    
    my_instance = Post(title,content,author)
    
    total_post_ls.append(my_instance)
    
    return total_post_ls

if __name__ == "__main__":
    total_member_ls = []
    total_id_ls = []
    total_post_ls = []
    
    while True:
        print('1: 회원가입\n2: 게시글 작성\n3: 검색\n4: 작성된 게시글 목록 확인\n5: 중단')
        print()
        init_input = input('입력 : ')
        if init_input == '1':
            total_member_ls, total_id_ls = member_input(total_member_ls,total_id_ls)
            print('회원가입 완료! 가입된 ID :',total_id_ls[-1])
            print()
        elif init_input == '2':
            if total_member_ls:
                total_post_ls = post_input(total_post_ls,total_id_ls)
                print('게시글 등록 완료! 등록된 게시글 제목 :',total_post_ls[-1].title)
                print('등록된 게시글 수 :', len(total_post_ls),'개')
                print()
            else:
                print('회원가입 먼저 진행하세요(작성 가능한 ID 없음)')
                print()
        elif init_input =='3':
            if not total_post_ls:
                print('작성된 게시글이 없습니다.')
                print()   
            else:
                print('1: ID로 검색\n2: 키워드로 검색')
                print()
                find_input = input('입력 : ')
                if find_input =='1':
                    
                    possible_username = [member.username for member in total_member_ls]
                    print('검색 가능한 id 목록 :',possible_username)
                    
                    find_keyword = input('검색할 ID를 입력하세요 : ')
                    print('검색한 Id :',find_keyword)
                    for post in total_post_ls:
                        if post.author == find_keyword:     
                            print('검색결과 title :', post.title)
                            print()
                elif find_input =='2':
                    find_keyword = input('검색할 키워드를 입력하세요 : ')
                    print('검색한 키워드 :',find_keyword)
                    for post in total_post_ls:
                        if find_keyword in post.content:
                            print('검색결과 title :', post.title)
                            print()
        elif init_input == '4':
            if not total_post_ls:
                print('작성된 게시글이 없습니다.')
                print()
            else:
                for post in total_post_ls:
                    print('title :', post.title)
            
        elif init_input == '5':
            print('중단합니다')
            print()
            break