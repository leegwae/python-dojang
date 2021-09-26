# heapq

```python
import heapq
```

- `heapq`는 우선순위 큐 알고리즘, 곧 힙 큐 알고리즘의 구현을 제공한다.
- 힙은 이진 트리이며, `heapq`는 모든 `k`가 다음을 만족하는 배열을 사용한다.

```python
heap[k] <= heap[(2 * k)+1] and heap[k] <= heap[(2 * k) +2]
```



## 원소 추가하기

| 함수                     | 인자     | 반환   | 설명                                                         |
| ------------------------ | -------- | ------ | ------------------------------------------------------------ |
| `heappush(리스트, 항목)` | `리스트` | `None` | `리스트`에 `항목`을 추가한다.<br />`O(logN)`의 시간복잡도를 가진다. |

```python
heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heapq)		// [1, 3, 7, 4]
```



## 원소 삭제하기

| 함수              | 인자     | 반환   | 설명                                                         |
| ----------------- | -------- | ------ | ------------------------------------------------------------ |
| `heappop(리스트)` | `리스트` | `요소` | `리스트`에서 가장 작은 `요소`를 삭제하고 그 값을 반환한다.<br />리스트에 요소가 없으면 `IndexError`가 발생한다. |

```python
minitem = heapq.heqppop(heap)
print(minitem)		// 1
print(heap)			// [3, 4, 7]
```



## 최솟값 얻기

```python
print(heap[0])
```



## 리스트를 힙으로 변환하기

| 함수              | 인자     | 반환   | 설명                                                         |
| ----------------- | -------- | ------ | ------------------------------------------------------------ |
| `heapify(리스트)` | `리스트` | `None` | `리스트`의 원소들을 힙 구조로 재배열한다.<br />`O(n)`만큼의 시간복잡도를 가진다. |



## 우선순위 지정하기

- `(우선순위, 요소)` 구조의 튜플을 `heappush`의 두번째 인자로 전달하면 우선순위를 의도대로 지정할 수 있다.



### 최대 힙 만들기

```python
nums = list(range(10))
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))

print(nums)		// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x[1] for x in heap])		// [9, 8, 5, 6, 7, 1, 4, 0, 3, 2]
```



## 참고

- [python docs - heapq](https://docs.python.org/ko/3/library/heapq.html)
- [python-heapq](https://www.daleseo.com/python-heapq/)

