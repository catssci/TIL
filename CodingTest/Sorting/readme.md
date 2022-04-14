[6개 정렬 알고리즘의 간단 정리 표]

|  정렬   |     최선      |     평균      |     최악      | 특징                                       |  비고  |
| :---: | :---------: | :---------: | :---------: | ---------------------------------------- | :--: |
| [선택 정렬](https://github.com/catssci/TIL/blob/main/CodingTest/Sorting/Selection_Sort.ipynb) |  $O(n^2)$   |  $O(n^2)$   |  $O(n^2)$   | 최솟값만을 찾아 정렬                              | 불안정  |
| [버블 정렬](https://github.com/catssci/TIL/blob/main/CodingTest/Sorting/Bubble_Sort.ipynb) |  $O(n^2)$   |  $O(n^2)$   |  $O(n^2)$   | 인접 두 값을 교환하며 정렬                          |  안정  |
| [병합 정렬](https://github.com/catssci/TIL/blob/main/CodingTest/Sorting/Merge_Sort.ipynb) | $O(N*logN)$ | $O(N*logN)$ | $O(N*logN)$ | 하나로 나누고, 다시 뭉치며 정렬                       |  안정  |
| [삽입 정렬](https://github.com/catssci/TIL/blob/main/CodingTest/Sorting/Insert_Sort.ipynb) |   $O(N)$    |  $O(N^2)$   |  $O(N^2)$   | key를 기준으로 이전 값들을 비교하며 자리를 찾아 정렬 한다.<br />정렬된 상태 일때는 효율성이 가장 좋다. |  안정  |
| [퀵 정렬](https://github.com/catssci/TIL/blob/main/CodingTest/Sorting/Quick_Sort.ipynb)  | $O(N*logN)$ | $O(N*logN)$ |  $O(N^2)$   | 피봇값을 기준으로 작은, 큰 배열로 분리한다.<br />정렬된 경우 최악의 결과가 나온다.<br />피봇의 값이 중간값일 경우 가장 잘 분리 됨 | 불안정  |
| 힙 정렬  | $O(N*logN)$ | $O(N*logN)$ | $O(N*logN)$ | 힙 자료 구조를 이용하여 정렬                         | 불안정  |
