# 정리 목적

- 면접에서 대답할 수 있게!
- 최대한 수식 없이 말로 설명할 수 있을 정도
- 많은 양을 공부해야 하기때문에 간결하게!
- 한번 다 공부 후에는 깊은 공부 후 정리 할 것!

# 2022.01.13 공부 리스트

1. Loss Surface란?
2. Attention이란?
3. Transformer란?
4. Collaborative filtering이란?
5. Few-Shot Learning이란?
6. Federated Learning이란?
7. SVD란?
8. 중심극한정리란?

- reference : [보이저 엑스 개발자 질문 리스트](https://v6xcareer.notion.site/v6xcareer/500ba3f2fc1448be904ca0f9347ae50f)



# 1. Loss Surface

### 01. Loss Surface란?

- 고차원 목적 함수를 사람이 이해할 수 있도록 3차원 공간안에 표현하는 방법

### 02. 만드는 방법은?

- 먼저 두개의 가우시안 분포를 따르는 랜덤 방향 벡터를 만든다. 이때 두 벡터는 학습하고자 하는 파라미터와 같은 차원 벡터이다.
- 그 후 학습이 완료된 파라미터 $\theta$와 두 벡터에 $\alpha, \beta$를 곱한 파라미터를 더하고 Loss값을 구한다. 이 때 $\alpha,\beta$를 -1과 1사이의 값으로 설정한다.
- 3차원 공간상에 ($\alpha, \beta, L(\theta+\alpha*v_1+\beta*v_2)$) 표시함으로써 시각화를 진행한다.



# 2. Attention

### 01. 배경

- Seq2Seq의 문제점을 해결하기 위해서 나왔다.
- 즉, 고정된 크기의 벡터로 압축하는 방식에 문제가 있었다.
  - 정보 손실
  - Vanishing gradient

### 02. Attention이란?

- 출력단어를 예측할때 인코더 부분에서의 정보를 같이 본다. 이때 가중치를 두어 연관이 높으면 높은 가중치, 낮으면 낮은 가중치를 둔다.

### 03. 학습 방법

- Seq2Seq에서는 디코더 출력을 위해 입력하는 변수로 이전 시점의 은닉층과 이전 시점의 출력을 입력받았다. Attention을 사용하면 여기에 추가로 Attention Value를 받는다.
- Attention Value 얻기
  - 인코더에서의 은닉 벡터 $h_i$와 디코더에서의 은닉 벡터 $s_t$를 내적하여 하나의 실수 형태로 바꾸고, softmax를 사용하여 Attention 분포로 변환한다.
  - Attention 분포와 각 인코더의 은닉벡터를 곱하고 합하여 Attention Value를 얻는다. (인코더의 차원과 동일)
- 디코더에서의 은닉 벡터 $s_t$와 Attention Value $a_t$를 결합한다.
- tanh(w*v_t) = new s_t를 계산!
- ​







# 3. Transformer

# 4. Collaborative filtering

# 5. Few-Shot Learning

# 6. Federated Learning

# 7. SVD

# 8. 중심극한정리

