import requests
import json


# 이미지가 있는 image_url을 통해 file_name 파일로 저장하는 함수
def save_image(image_url, file_name, maximum):
    img_response = requests.get(image_url)
    # 요청에 성공했다면
    if img_response.status_code == 200:
        # 파일 저장
        for i in range(maximum):
            with open(file_name, "wb") as fp:
                fp.write(img_response.content)


print("최대 검색 수 : ", end='')
maximum = int(input())

# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization": "KakaoAK 25e4c5fa84ea6248331959b692f7cb1b"
}
data = {
    "query": "고양이"
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
# 요청에 실패했다면
if response.status_code != 200:
    print("eror! because ", response.json())
else:
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        # 저장될 이미지 파일명 설정
        count = count + 1
        file_name = "test_%d.jpg" % (count)
        # 이미지 저장
        save_image(image_info['image_url'], file_name, maximum)

