# CH4. Operator

**4.1 산술 연산자**

**4.1.1 산술 연산자의 종류**

| 연산자 | 의미                                                 |
| ------ | ---------------------------------------------------- |
| =      | 대입 연산자                                          |
| +      | 더하기                                               |
| -      | 빼기                                                 |
| *      | 곱하기                                               |
| /      | 나누기(결과는 실수)                                  |
| //     | 나누기(소수점을 버림, 결과는 정수, 즉 **몫**을 구함) |
| %      | 나머지값                                             |
| **     | 제곱                                                 |



**4.1.2 문자열로 산술 연산하기**

- 문자열을 `float()`,  `int()` 함수를 사용하여 실수나 정수로 변환

```python
s1 = "100"
s2 = "100.123"
print(int(s1), float(100.123))
# 100 100.123
```

- 숫자를 문자열로 변환하려면 `str()` 함수를 사용한다.

```python
s1 = 100
s2 = 100.123
print(str(100) + str(100.123))
# 100100.123
```



**4.1.3 대입 연산자의 종류**

| 연산자 | 의미       |
| ------ | ---------- |
| +=     | a = a + 3  |
| -=     | a = a - 3  |
| *=     | a = a * 3  |
| /=     | a = a / 3  |
| //=    | a = a // 3 |
| %=     | a = a % 3  |
| **=    | a = a ** 3 |

- 증감(`++`, `--`) 연산자는 없다.



**4.3 관계 연산자**

- 관계 연산의 결과값(반환값)은 `True` 혹은 `False`이다.

**4.3.1 관계 연산자의 종류**

| 연산자 | 의미        | 설명                       |
| ------ | ----------- | -------------------------- |
| ==     | 같다        | 두 값이 동일하면 참        |
| !=     | 같지 않다   | 두 값이 동일하지 않으면 참 |
| >      | 크다        | 왼쪽이 크면 참             |
| <      | 작다        | 왼쪽이 작으면 참           |
| >=     | 크거나 같다 | 왼쪽이 더 크거나 같다      |
| <=     | 작거나 같다 | 왼쪽이 더 작거나 같다      |



**4.4 논리 연산자**

| 연산자 | 의미       | 설명                                |
| ------ | ---------- | ----------------------------------- |
| `and`  | 그리고     | 피연산자 모두가 참이어야 참         |
| `or`   | 또는       | 피연산자 둘 중 하나라도 참이어야 참 |
| `not`  | ~이 아니다 | 피연산자의 논리값을 뒤집음          |



**4.5 연산자 우선순위**

| 우선순위 | 연산자                   | 의미                         |
| -------- | ------------------------ | ---------------------------- |
| 1        | () [] {}                 | 괄호, 리스트, 딕셔너리, 세트 |
| 2        | **                       | 지수                         |
| 3        | + - ~                    | 단항 연산자                  |
| 4        | * / % //                 | 산술 연산자                  |
| 5        | + -                      |                              |
| 6        | << >>                    | 비트 시프트 연산자           |
| 7        | &                        | 비트 AND                     |
| 8        | ^                        | 비트 XOR                     |
| 9        | \|                       | 비트 OR                      |
| 10       | < > >= <=                | 관계 연산자                  |
| 11       | == !=                    | 동등 연산자                  |
| 12       | = %= /= //= -= += *= **= | 대입 연산자                  |
| 13       | `not`                    | 논리 연산자                  |
| 14       | `and`                    |                              |
| 15       | `or`                     |                              |
| 16       | `if`~`else`              | 비교식                       |