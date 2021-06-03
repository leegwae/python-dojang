# 0415_ CH7_List, Tuple, Dictionary

- 리스트는 배열과 달리 서로 다른 데이터형들을 요소로 가질 수 있다.



## 02. 리스트

## 리스트의 일반적인 사용

```python
a = []
for i in range(0, 4):
    a.append(0)

for i in range(0, 4):
    a[i] = i
```

- 하지만 다음 코드는 다음과 같은 에러를 일으킨다.

`IndexError: list assignment index out of range`

```python
a = []
a[0] = 1
```

- 즉, 리스트의 길이를 늘리기 위해(<u>리스트에 요소를 추가하기 위해서는) `append()` 메서드를 사용해야만 한다</u>. 하지만 이미 추가된 요소에 대해, 값을 변경하는 것은 가능하다.



## 음수 인덱스로 리스트 요소에 접근하기

```python
a = [10, 20, 30]
# a[-1] = 30 ... a[-3] = 10
```

- `-i` 인덱스는 역순으로 리스트 요소에 접근한다.
- `-리스트길이 ~ -1` 을 벗어난 음수 인덱스에 접근하면 다음과 같은 에러를 일으킨다.

`IndexError: list index out of range`



## 리스트의 요소 삭제하기

- `del(리스트(인덱스))`  : 리스트의 인덱스의 요소를 삭제한다.
- `del 리스트[인덱스]`: 위와 동일한 동작을 한다.



## 리스트 메서드

| function | 설명                                           |
| -------- | ---------------------------------------------- |
| `copy()` | 원본 리스트를 복사하여 새로운 객체로 반환한다. |



## 03. 2차원 리스트

- `리스트[행의개수][열의개수]`



## 04. 튜플

## 요소가 하나인 튜플 만들기

```python
a = (10,)
b = 10,
```



## 05. 딕셔너리

## 딕셔너리 키-값 삭제

- `del(딕셔너리[키])`



## 딕셔너리 메서드

| function   | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| `get(키)`  | 키에 대응하는 값을 반환<br />`lana.get('name') # lana`       |
| `keys()`   | `dict_keys`객체로 딕셔너리의 모든 키를 반환<br />`list(lana.keys()) # ['name', 'album']` |
| `values()` | `dict_values` 객체로 딕셔너리의 모든 값을 반환<br />`list(lana.values()) # ['lana', 'ultraviolence']` |
| `items()`  | `dict_items` 객체로 튜플 형태를 반환<br />`dict_items(['name', 'lana'], ['ablum', 'ultraviolence'])` |



## 딕셔너리 순회하기

```python
lana = { 'name': 'lana', 'album': 'utraviolence' }

for k in lana.keys():
    print("%s: %s" % (k, lana[k]))
```



## 딕셔너리 정렬하기

- 키로 정렬한다.

```python
import operator

poetDic, poetList = {}, []

poetList = sorted(poetDic.items, key = operator.itemgetter(0))
print(poetList)
```



## 06. 세트

- 키만 모아 놓은 딕셔너리의 특수한 형태
- 딕셔너리의 키는 중복되면 안되므로 세트에 들어있는 값들은 항상 유일하다.
- `세트 = {키1, 키2, 키3}`
- 중복된 키는 하나만 남는다.



**중복값 제거하기**

```python
tempList = ['lana', 'agnes', 'zitten', 'kard', 'lana']
set(tempList)		# {'lana', 'agnes', 'zitten', 'kard'}
```



## 교집합, 합집합, 차집합, 대칭 차집합

```python
a = { 1, 2, 3, 4 }
b = { 2, 3, 5 }

a & b	# 교집합	{ 2, 3 }
a | b	# 합집합	{ 1, 2, 3, 4, 5 }
a - b	# 차집합	{ 1, 4 }
a ^ b	# 대칭 차집합	{ 1, 4, 5 }

# 함수 사용하기
a.intersection(b)
a.union(b)
a.difference(b)
a.symmetric_difference(b)
```



## 컴프리헨션

```python
a = [num for num in range(1, 6)]
```

- `리스트 = [수식 for 항목 in range() if 조건식]`

```python
a = [num for num in range(0, 10) if num % 3 == 0 ]; print(a)
# [0, 3, 6, 9]
```



## 동시에 여러 리스트에 접근하기

- `zip()`으로 여러 리스트에 동시에 접근하기

```python
album = ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
song = ['born to die', 'radio', 'love']

for albumName, songName in zip(album, song):
    print("%s: %s" % (albumName, songName))
    
    
# ultraviolence: born to die
# honeymoon: radio
# born to die: love
```

- 요소가 더 적은 리스트의 개수만큼 접근할 수 있다. `print(albumName)`으로만 접근해도, `born to die`까지 3개만 출력된다.



## zip(리스트, 리스트)로 튜플이나 딕셔너리 만들기

```python
album = ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
song = ['born to die', 'radio', 'love']

tupList = list(zip(album, song))
dic = dict(zip(album, song))

tupList; dic;

# [('ultraviolence', 'born to die'), ('honeymoon', 'radio'), ('born to die', 'love')]
# {'ultraviolence': 'born to die', 'honeymoon': 'radio', 'born to die': 'love'}
```



## 리스트의 복사

- 얕은 복사: 동일한 메모리 공간 공유

```python
a = ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
b = a
print(a) # ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
b.append('lust for life')
print(a) # ['ultraviolence', 'honeymoon', 'born to die', 'paradise', 'lust for life']
```



- 깊은 복사: 새로 만들기

```python
a = ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
b = a[:]
print(a) # ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
b.append('lust for life')
print(a) # ['ultraviolence', 'honeymoon', 'born to die', 'paradise']
```



## 리스트로 스택 만들기

```python
a = ['ultraviolence', 'honeymoon', 'born to die' ,'paradise']
top = len(a)

a.append('lust for life')
top += 1

a.pop()
top -= 1
```

