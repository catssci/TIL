# 정리 목적

- 면접에서 대답할 수 있게!
- 최대한 수식 없이 말로 설명할 수 있을 정도
- 많은 양을 공부해야 하기때문에 간결하게!
- 한번 다 공부 후에는 깊은 공부 후 정리 할 것!

# 2022.01.10 공부 리스트

1. ~~Gradient Descent~~
2. ~~Sigmoid~~
3. ~~Validation 세트, Test 세트~~
4. Auto Encoder
5. Dropout
6. CNN
7. Word2Vec
8. Adam Optimizer
9. Batch Normalization
10. CycleGAN

- reference : [보이저 엑스 개발자 질문 리스트](https://v6xcareer.notion.site/v6xcareer/500ba3f2fc1448be904ca0f9347ae50f)





# 1. Gradient Descent

### 00. Loss Function, Cost Function의 차이

- Loss Function : **개별 데이터 포인트**에 대한 예측값과 실제값의 오차를 의미한다.
- Cost Function : **모든 입력 데이터**에 대한 예측값과 실제값데 대한 오차를 의미한다.
- 즉, $Cost \ Function > Loss \ Function$

### 01. Gradient Descent가 뭔가요? , Gradient Descent를 설명해주세요.

- Cost Function이 minimization 될 때의 파라미터를 찾는 알고리즘이다.

### 02. Gradient Descent가 어떻게 동작하나요?

- Cost Function의 현재 위치하고 있는 지점에서 경사면을 따라 하강하는 과정을 반복한다.
- **더 자세히 말하면, Cost Function의 현재 위치 지점에서 각 파라미터의 Gradient를 구하고 Cost Function이 작아지는 방향으로 learning rate 만큼 이동하는 과정을 반복한다.**
- Gradient : 미분 값
- batch gradient descent와 혼용해서 사용한다.

### 03. Gradient Descent의 문제는 무엇인가요?

1. 우리가 목표로 하는 Global Minimum이 아닌 Local Minimum에 수렴할 수 있다.
2. Learning Rate가 작으면 학습 시간이 오래 걸리며 Local Minimum에 수렴 가능성이 커진다. 또한 Learning Rate가 커지면 수렴 방향에 멀어질 수 있다.
3. 모든 훈련 데이터를 사용하기 때문에 훈련 데이터의 크기가 커지면 계산 시간이 오래 걸린다.

### 04. 모든 훈련 데이터를 사용하여 계산 시간이 오래 걸리는 문제가 발생했으면 이를 해결하기 위해 어떤 방법을 사용하였나요? 

- 모든 훈련 데이터를 사용하지 않고 일정 데이터를 이용한 방법을 사용한다. 데이터의 사용 개수에 따라 다음과 같이 나눈다.
  1. 단일 훈련 데이터를 사용하는 Stochastic Gradient Descent (확률적 경사하강법)
  2. m개의 훈련 데이터를 사용하는 mini-batch Gradient Descent (미니배치 경사하강법)

### 05. 확률적 경사하강법, 미니 배치 경사하강법의 장단점은 뭔가요?

- 확률적 경사하강법
  - 장점
    1. 하나의 데이터에 대하여 최적화를 진행하기 때문에 계산 속도와 수렴 속도가 빠르다.
  - 단점
    1. 하나의 데이터만을 사용하기 때문에 전체적인 정보를 가지고 최적화를 진행하는 것이 아니기 때문에 수렴이 불안정하다. 그래서 Local Minimum에 빠질 확률이 높다.
    2. 컴퓨터의 성능을 모두 사용하지 못한다.
- 미니배치 경사하강법
  - 장점
    1. GD와 SGD 랑 비교하여 Local minimum에 빠질 확률이 적다.
    2. GD 보단 메모리 사용량이 낮다.
  - 단점
    1. batch size를 결정해야 한다.
    2. SGD보단 메모리 사용량이 높다.

### 06. Local Minimum에 수렴하는 문제를 어떻게 해결하고 있나요?

- 모멘텀 항을 추가한다.
  - 모멘텀은 이전 step에서의 gradient를 이용
  - 관성과 유사하다고 보면 된다.
- 학습률을 조정한다.
  - 많이 학습된 파라미터는 점점 갈수록 학습률을 작게 조정한다. 
  - AdaGrad $\rightarrow$ RMSProp (지수이동평균 적용, 학습률 0으로 수렴되는 것 방지 목적)
- 모멘텀 항과 학습률 조정하는 방법 모두 사용한다.
  - Adam



# 2. Sigmoid 

### 01. sigmoid란?

- 활성화 함수 중 하나로 0~1 사이의 값을 출력하는 비선형 활성화 함수이다.
- 수식은 $\frac{1}{1+e^{-f(x)}}$  와 같이 사용한다.
- Logistic Regression에서 클래스 확률값을 출력할 때 사용한다. (multi class 분류 문제에서는 나중에 softmax를 사용)

### 02. sigmoid 단점을 말해보세요.

- 역전파 방법으로 모델을 학습할 때, **Gradient Vanishing** 문제가 발생 할 수 있다.
- Gradient Vanishing : 역전파를 진행하며 gradient값이 소실되는 현상

### 03. sigmoid의 Gradient Vanishing 문제 해결법은?

- NN에서 hidden layer의 활성화 함수로 사용하지 않고, 출력층의 활성화 함수로 사용
- tanh or ReLU 사용, 그러나 ReLU를 더 많이 사용한다.
- tanh는 여전히 gradient vanishing 문제 발생

### 04. sigmoid를 활용하는 예시를 들어주세요.

- Logistic Regression에서 확률을 출력하기 위한 활성화 함수로 사용된다.
- RSTL 모델, GRU 모델에서 활성화 함수로 사용된다.



# 3. Validation, Test Data

### 01. Validation, Test 데이터의 역할은?

- Validation : 모델의 성능을 측정하기 위한 데이터, 적합한 파라미터를 찾기 위한 데이터로써 사용된다.
- Test : 최종 모델의 성능 측정하기 위한 데이터로써 사용된다.

### 02. Validation, Test 데이터를 나누는 방법

- 일반적으로 Train 60%, Validation 20%, Test 20%로 나눈다.
- 그러나 데이터양에 따라 위의 비율은 조정가능하다.

### 03. k-fold cross validation 사용하는 이유는?

- 확보된 데이터의 양이 충분치 않아 최대한 많은 데이터를 사용하기 위해

### 04. k-fold cross validation에서 모델 평가하는 방법은?

- k번의 평가 후 평균을 내어 최종 모델의 평가 지표로 사용된다.



# 04. Auto Encoder 



















### 00. 역전법

- neural network에서 gradient descent를 chain rule을 사용하여 단순화시킨 것

