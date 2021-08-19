import requests
import json
import os  # 검색 결과를 새로 생성한 폴더에 넣어주기 위해 os의 mkdir 명령어를 사용


# 이미지가 있는 image_url을 통해 file_name 파일로 저장하는 함수
def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    # 요청에 성공했다면
    if img_response.status_code == 200:
        # 파일 저장
        with open(path, "wb") as fp:
            fp.write(img_response.content)


# Initializing
print("무슨 이미지를 검색하실건가요? 미 입력시 고양이가 나옵니다 (귀여움)")
print("검색 : ", end='')
search = input()
print("최대 검색 수 : ", end='')
maximum = int(input())

if not search: search = "고양이"

# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization": "KakaoAK 25e4c5fa84ea6248331959b692f7cb1b"
}
data = {
    "query": search
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)

# 요청에 실패했다면
if response.status_code != 200:
    print("error! because ", response.json())

else:
    folder_name = search + "_" + str(maximum) + "_Images/"
    os.mkdir("/workspace/Tour_Of_Baekjoon/Python_Crawling_catImage/" + folder_name)  # mkdir(내용) , 내용의 이름을 가진 폴더를 생성
    count = 1

    for image_info in response.json()['documents']:
        # path 는 고정해두었으나, 배포한다면 os.getcwd()를 이용하여 가변적으로 사용
        path = '/workspace/Tour_Of_Baekjoon/Python_Crawling_catImage/'
        path = path + folder_name  # path = 결과 이미지를 저장할 폴더 경로

        if count == maximum + 1:
            print("지정된 검색 결과 수를 초과하여 중단합니다.")
            break

        # print(f"[{count}th] image_url =", image_info['image_url'])

        # 저장될 이미지 파일명 설정
        count = count + 1

        # 파일 명에 검색한 키워드가 들어가게 함
        file_name = "%s_%d.jpg" % (search, count - 1)
        path = path + file_name

        # 이미지 저장
        save_image(image_info['image_url'], file_name)

