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
- new s_t는 다음 시점의 입력으로 다시 사용!

### 04. Attention Value

- Attention Value를 계산하는 다양한 방법 존재
- 위에서는 Dot Product 방법을 사용하여 소개한다.




# 3. Transformer

### 01. Transformer란? 

- 인코더-디코더 구성을 따르면서, Attention만을 이용하여 구성한 모델이다.

### 02. 왜 나왔나?

- Attention이 나왔을 때와 같이 고정된 크기의 벡터로 압축을 하면서 1. 정보 손실, 2. Vanishing gradient 문제가 나왔다.
- 이를 해결하기 위해 Attention을 사용하였고, RNN구조에서 이를 바꿔 Attention만을 이용해보자는 아이디어에서 나왔다.

### 03. Positional Encoding

- 기존의 RNN 모델의 장점은 단어의 위치 정보를 같이 학습할 수 있다는 것이었다.
- 그러나 Transformer에서는 RNN 모델을 사용하지 않기 때문에 위치 정보를 같이 추가 할 수 있는 방법을 강구해왔고, 그 방법이 Positional Encoding이다.
- 단어의 Embedding 결과에서 Positional Encoding을 더한 벡터를 입력으로 사용한다.
- 더 자세한 설명 : [Positional Encoding](https://skyjwoo.tistory.com/entry/positional-encoding%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)

### 04. Encoder 

- 크게 두 네트워크로 이루어져 있다.
  - Self Attention
  - Feed Forward Neural Network
- 그리고 각 네트워크 출력에서 Add & Norm 과정이 포함되어 있다. (총 2개)

### 05. Self Attention

- 현재 문장 안에서 각 단어들 사이의 관계가 얼마나 연관있는지 Attention 방법을 통하여 추출한다.

- 현재 단어 임베딩 벡터 $x_i$를 Self Attention을 통해 $z_i$로 변환한다.

   	1. Query, Key, Value 벡터를 생성한다.
   	2. 현재 Query와 각 단어의 Key 벡터의 내적과 key 벡터 크기의 루트 값으로 나누어 Score 벡터를 계산한다.
   	3. Softmax를 취하고 Value 벡터들을 곱한다.
   	4. 그리고 합하여 최종 벡터 $z_i$를 출력한다.
   	5. 위 과정을 모든 단어 시점마다 반복한다.

- 위 과정은 행렬로 표현함으로써 한번에 계산할 수 있다.

  - $W_q, W_k, W_v$ : word num * 출력 z 로 표현

  ![img](https://nlpinkorean.github.io/images/transformer/self-attention-matrix-calculation-2.png)

- 위의 과정을 n번 반복하여 서로 다른 z행렬을 n개 만들고 합쳐서 W_0 행렬을 곱하여 최종 Z 행렬을 구한다.

![img](https://nlpinkorean.github.io/images/transformer/transformer_multi-headed_self-attention-recap.png)

### 06. Position-wise FFNN

- 하나의 히든 레이어를 가지는 Fully Connected NN

- 히든 레이어의 출력의 활성화 함수를 ReLU 사용

  ![img](https://wikidocs.net/images/page/31379/positionwiseffnn.PNG)

- 이때 $W_1, b_1, W_2, b_2$는 같은 인코더 층에서는 공유하지만 다른 층과는 다르다.!

### 07. Add & Norm

- Residual Connection

  - 멀티 헤드 어텐션의 입력(X)과 멀티 헤드 어텐션의 결과(Z)가 더해지는 과정
  - X+Z

- Layer Normalization

  - 각 단어 행의 평균과 분산을 구하여 정규화 한다.

  ![img](https://wikidocs.net/images/page/31379/layer_norm_new_2_final.PNG)

### 08. Decoder

- 크게 세 네트워크로 이루어져 있다.
  - Self Attention & look-ahead mask
  - 인코더-디코더 어텐션
  - Feed Forward Neural Network
- 그리고 각 네트워크 출력에서 Add & Norm 과정이 포함되어 있다. (총 3개)

### 09. Self Attention and Look Ahead Mask

- 목적 : 현재 시점의 예측에서 현재 시점보다 미래에 있는 단어들을 참고하지 못하도록 하기 위한 방법
- 즉, Attention Score 행렬을 계산 할 때 Mask 를 씌워 미래 단어를 참고하지 못하도록 만든다.![img](https://wikidocs.net/images/page/31379/decoder_attention_score_matrix.PNG)        $\rightarrow$       ![img](https://wikidocs.net/images/page/31379/%EB%A3%A9%EC%96%B4%ED%97%A4%EB%93%9C%EB%A7%88%EC%8A%A4%ED%81%AC.PNG)
- 이를 제외하고는 Encoder의 Self Attention 과 같다.

### 10. 인코더-디코더 어텐션

- Query는 디코더의 행렬, Key, Value는 인코더에서 마지막 행렬을 가져온다.

![img](https://wikidocs.net/images/page/31379/%EB%94%94%EC%BD%94%EB%8D%94%EB%91%90%EB%B2%88%EC%A7%B8%EC%84%9C%EB%B8%8C%EC%B8%B5%EC%9D%98%EC%96%B4%ED%85%90%EC%85%98%EC%8A%A4%EC%BD%94%EC%96%B4%ED%96%89%EB%A0%AC_final.PNG)

- 이후의 과정은 Self Attention과 같다.

### 11. Feed Forward Neural Network 

- 인코더에서의 FFNN과 같다.

### 12. 주의점

- Encoder과 Decoder의 층은 똑같이 구현한다.
- 각 Decoder 층에 Encoder의 출력을 모두 입력해준다.
- 출력은 어떻게 하는거지???



# 4. Collaborative filtering

### 01. Collaborative Filtering

- 추천 시스템의 한 종류
- 유사한 성향의 User를 찾아 User의 컨텐츠를 추천한다.

### 02. Content-based

- 추천 시스템의 한 종류
- 유사한 컨텐츠를 찾아 컨텐츠를 User에게 추천한다.

### 03. User Based

- User Based Collaborative Filtering

- 유사도 : 두 사용자가 얼마나 유사한 아이템을 선호했는지를 기준

- 공통으로 평가한 아이템들을 두 벡터로 만든 후 코싸인 유사도를 계산한다.

- 특정 아이템의 선호도 예측 : 다른 사람들의 아이템 선호도와 다른 사람들과의 유사도를 곱하고 유사도 합을 나눈다.

  ![img](https://scvgoe.github.io/img/4ZjwdolVv0C4U.png)

### 04. Item Based

- Item Based Collaborative Filtering
- 유사도 : 두 아이템에서 얼마나 유사한 유저가 선호했는지를 기준
- 공통으로 평가한 유저 선호도를 두 벡터로 만든 후 코싸인 유사도를 계산한다.

### 05. 코싸인 유사도의 단점

- 두 아이템(1, 1, 1, 1), (5, 5, 5, 5)의 코싸인 유사도를 구하면 1로 유사하게 나온다. 그러나 실상은 두 아이템의 평가는 극명하게 갈린다.
  - 이를 해결하는 방법으로 피어슨 유사도 또는 보정된 코싸인 유사도를 사용한다.
- 두 아이템을 평가한 사람이 1명이라면 이때에도 유사도가 1이 나온다. 
  - 이를 해결하기 위해 최소평가 인원수를 정한다. 최소평가 인원수보다 작으면 0으로 결정한다.

### 06. 아마존, 넷플릭스에서는?

- 아이템 기반의 추천 시스템을 사용한다.
  - 일반적으로 유저보다는 아이템의 크기가 작다.



# 5. Few-Shot Learning

### 01. Few-Shot Learning이란?

- ​









# 6. Federated Learning

# 7. SVD

# 8. 중심극한정리

