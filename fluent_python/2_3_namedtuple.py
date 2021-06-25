from collections import namedtuple

# 일종의 간단한 클래스 정의
# 여기서 City가 타입명, 그 뒤의 문자열이 해당 클래스의 어트리뷰트, city는 일종의 클래스 객체로 보는 것이 맞을 것 같다...
city = namedtuple('City', 'name country population')

seoul = city(name='seoul', country='korea', population=5000)  # city('seoul', 'korea', 5000)와 같이 쓸 수도 있음.

print(type(seoul))  # <class '__main__.City'>

# namedtuple -> dict
print(seoul._asdict(), type(seoul._asdict()))  # {'name': 'seoul', 'country': 'korea', 'population': 5000}, <class 'dict'>