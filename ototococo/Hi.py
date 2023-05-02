파이썬의 기본적인 자료형은 다음과 같습니다.

-숫자(Number): 정수(Integer), 실수(Floating point), 복소수(Complex number)
-문자열(String): 문자열(str)
-시퀀스(Sequence): 리스트(List), 튜플(Tuple), 레인지(Range)
-집합(Set): 집합(Set), frozenset
-매핑(Mapping): 딕셔너리(Dictionary)
-부울(Boolean): 참(True), 거짓(False)
-널(Null): None
이 외에도 다양한 자료형이 있지만, 이들은 위의 기본적인 자료형을 조합하여 만들어지는 파생 자료형입니다. 예를 들어, 리스트와 딕셔너리를 조합한 딕셔너리의 리스트(List of dictionaries) 등이 있습니다.



자료형
숫자(number)
숫자 자료형은 정수(int), 실수(float), 복소수(complex)로 나누어집니다.

python
Copy code
x = 3      # 정수(int)
y = 3.14   # 실수(float)
z = 2 + 3j # 복소수(complex)
문자열(string)
문자열 자료형은 작은따옴표(')나 큰따옴표(")로 둘러싸인 문자열입니다.

python
Copy code
a = "Hello, world!"  # 큰따옴표로 둘러싼 문자열
b = 'Python is fun!' # 작은따옴표로 둘러싼 문자열
리스트(list)
리스트 자료형은 여러 개의 값을 저장하는 자료형입니다. 대괄호([])로 둘러싸며, 각 값은 쉼표(,)로 구분합니다.

python
Copy code
a = [1, 2, 3, 4, 5]    # 정수를 저장하는 리스트
b = ["apple", "banana", "cherry"]  # 문자열을 저장하는 리스트
c = [1, "apple", True] # 여러 자료형을 혼합하여 저장하는 리스트
튜플(tuple)
튜플 자료형은 리스트와 비슷하지만, 한 번 생성된 값을 변경할 수 없습니다. 소괄호(())로 둘러싸며, 각 값은 쉼표(,)로 구분합니다.

python
Copy code
a = (1, 2, 3)         # 정수를 저장하는 튜플
b = ("apple", "banana", "cherry")  # 문자열을 저장하는 튜플
c = (1, "apple", True) # 여러 자료형을 혼합하여 저장하는 튜플
세트(set)
세트 자료형은 중복되지 않는 값을 저장하는 자료형입니다. 중괄호({})로 둘러싸며, 각 값은 쉼표(,)로 구분합니다.

python
Copy code
a = {1, 2, 3, 4, 5}    # 정수를 저장하는 세트
b = {"apple", "banana", "cherry"}  # 문자열을 저장하는 세트
c = {1, "apple", True} # 여러 자료형을 혼합하여 저장하는 세트
딕셔너리(dictionary)
딕셔너리(dictionary) 자료형은 키(key)와 값(value)을 한 쌍으로 저장하는 자료형입니다. 딕셔너리는 중괄호({})로 둘러싸며, 각 키와 값은 콜론(:)으로 구분하고, 각 쌍은 쉼표(,)로 구분합니다.

python
Copy code
dict1 = {'name': 'Alice', 'age': 25, 'gender': 'female'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}

print(dict1)  # {'name': 'Alice', 'age': 25, 'gender': 'female'}
print(dict2)  # {1: 'one', 2: 'two', 3: 'three'}
딕셔너리에서는 키를 사용하여 값을 조회할 수 있습니다.

python
Copy code
print(dict1['name'])  # 'Alice'
print(dict1['age'])   # 25
딕셔너리에 존재하지 않는 키를 조회하면 KeyError가 발생합니다.

딕셔너리에서는 키와 값 모두 변경 가능합니다.

python
Copy code
dict1['age'] = 30
print(dict1)  # {'name': 'Alice', 'age': 30, 'gender': 'female'}

dict1['city'] = 'Seoul'
print(dict1)  # {'name': 'Alice', 'age': 30, 'gender': 'female', 'city': 'Seoul'}
딕셔너리에서는 keys(), values(), items() 메서드를 사용하여 각각 키, 값, 키-값 쌍을 조회할 수 있습니다.

python
Copy code
print(dict1.keys())   # dict_keys(['name', 'age', 'gender', 'city'])
print(dict1.values()) # dict_values(['Alice', 30, 'female', 'Seoul'])
print(dict1.items())  # dict_items([('name', 'Alice'), ('age', 30), ('gender', 'female'), ('city',
