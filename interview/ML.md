# 정리 목적

- 면접에서 대답할 수 있게!
- 최대한 수식 없이 말로 설명할 수 있을 정도
- 많은 양을 공부해야 하기때문에 간결하게!
- 한번 다 공부 후에는 깊은 공부 후 정리 할 것!

# 2022.01.10 공부 리스트

1. ~~Gradient Descent~~
2. ~~Sigmoid~~
3. ~~Validation 세트, Test 세트~~
4. ~~Auto Encoder~~
5. ~~Dropout~~
6. ~~CNN~~
7. ~~Word2Vec~~
8. ~~Adam Optimizer~~
9. ~~Batch Normalization~~
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




# 4. Auto Encoder 

### 01. Auto Encoder란?

- 입력과 출력이 같은 뉴럴네트워크 구조의 모델이다. 
- 구조는 Encoder단과 Decoder단으로 나누어져 부른다. 
- Encoder단은 뉴런의 수가 줄어드는 방향으로 구성되고, Decoder단은 뉴런의 수가 늘어나는 방향으로 구성되어 최종단에서는 입력뉴런의 수와 같아지게 된다.

### 02. 사용 목적은?

- Dimension Reduction

- Network 가중치 초기화 

  $\rightarrow $ Batch-Norm, Xavier Initialization

  마지막 출력단의 가중치는 random init

### 03. PCA와 차이점은?

- Activation Function 없이 사용하는 AutoEncoder는 PCA와 같은 manifold를 가진다.
- 일반적인 PCA는 선형적으로 차원을 줄인다. 그러나 AutoEncoder는 비선형으로 차원을 줄일수 있다.




# 5. Dropout 

### 01. Dropout이란?

- 히든레이어의 일부 뉴런을 일부 동작을 멈춰가면서 모델을 학습시키는 전략

### 02. 효과

- Overfitting 문제를 막기 위해 Regularization 효과를 준다.
- 여러 개의 모델을 학습하는 효과를 누릴 수 있다.

### 03. 비슷한 Regularization 효과를 주는 방법들은?

- L1 Regularization
- L2 Regularization

//max-norm regularization

//large decaying learning rates, high momentum

### 04. 유의할점은?

- 테스트 할 때에는 dropout을 끄고 테스트 진행한다. 더 확실한 결과를 얻기 위해!!




# 6. CNN 

### 01. CNN이란?

- convolution이라는 작업이 들어가는 NN

### 02. 왜 이미지 분야에서 많이 사용하는가?

- local information을 효율적으로 볼 수 있다. (일정 크기의 filter와 convolution 연산을 통해)

### 03. 장점은?

- 파라미터의 감소

### 04. 주어진 CNN과 똑같은 MLP를 만들 수 있나?

- 네 만들수 있습니다. MLP를 구성할때 다음 뉴런의 출력을 계산할 때 이전 레이어의 모든 뉴런과 연결하지 않고 일정 영역의 뉴런만을 연결한 모델을 구성할 수 있다면, Convolution 효과를 똑같이 구성 할 수 있다.

### 05. Pooling의 장점

- 데이터의 사이즈가 줄어들기 때문에 연산에 들어가는 컴퓨팅 연산량이 줄어든다.
- 데이터의 크기를 줄이면서 소실이 발생하기 때문에, 오버피팅을 방지할 수 있다.

### 06. 풀링시에 만약 Max를 사용한다면 그 이유는?

- Average Pooling : 이미지를 부드럽게 만든다. 
- Max Pooling : 선명한 특징을 식별하게 한다. 
- MNIST를 예를 들때, Max Pooling을 사용한다면 흰색 부분을 강조하여 Pooling을 실시한다. 결국 이때에는 숫자 영역에 집중하겠다는 뜻으로 볼 수 있다.

### 06. 시퀀스 데이터에 CNN을 적용하는 것이 가능할까?

- Conv1D를 사용하여 충분히 만들 수 있다.
- 이때의 Convolution 연산은 1차원으로 움직인다.
- 또는 시퀀스 데이터를 이미지로 변환하여 사용할 수 있다.




# 7. Word2Vec 

### 01. Word2Vec이란?

- 단어를 벡터로 변환하는 임베딩의 한종류이다.
- 단어간의 유사도를 반영하여 벡터화한다.
- 3개의 레이어를 가지는 NN 모델이다.

### 02. 원리는?

- "비슷한 위치에서 등장하는 단어들은 비슷한 의미를 가진다" 가정하에 중심단어, 주변단어로 나누어 모델을 학습한다. 그래서 특정 단어 주위에 비슷한 단어가 많이 나오게 되면 유사도가 높다고 판단할 수 있게된다.

### 03. 왼쪽 파라메터들을 임베딩으로 쓰는 이유?

- 입력 데이터는 원핫 인코딩이 되어 있고, 왼쪽 weight matrix와 곱하게 되면 해당 weight matrix의 행 벡터가 나오게 된다. 따라서 이를 학습이 완료된 모델에서의 weight matrix는 임베딩한 결과를 차곡차곡 쌓아놓은 모습으로 볼 수 있게된다.

### 04. 오른쪽 파라메터들의 의미는 무엇일까?

- 임베딩한 벡터를 원 핫 벡터의 차원으로 돌려주는 역할을 하고, softmax과정을 거쳐 준변 단어의 확률 벡터를 출력하게 된다.

### 05. 남자와 여자가 가까울까? 남자와 자동차가 가까울까?

- word2vec의 기본 가정이 "비슷한 위치에서 등장하는 단어는 비슷한 의미를 가진다"는 가정하에 출발하였기 때문에 남자와 여자가 가깝게 나올 것이다. 일반적으로 남자 또는 여자, 자동차가 같이 나오는 빈도수가 남자 여자 빈도수가 더 많을 듯 싶다.

### 06. 번역을 Unsupervised로 할 수 있을까?

- 할 수 있다.
- 두 언어의 embedding을 한다.
- 대역 샘플 목록을 구성하고, 공유 임베딩 공간에 매핑하는 변환 네트워크를 학습한다.
- 나머지 단어들도 자동으로 비슷한 위치에 매핑되게 되고, 이를 이용하여 번역을 한다.

### 07. Skip gram, CBOW란?

- CBOW : 주변 단어로부터 중심 단어를 예측하는 word2vec 모델
- skip-gram : 중심 단어로부터 주번 단어를 예측하는 word2vec 모델

### 08. skip gram이 왜 더 많이 사용되어지나?

- 중신 단어에 대해서 주변 단어를 예측하며 Update하기 때문에 CBOW모델보다 각 단어에 대해서 update 기회가 더 많다.

### 09. 네거티브 샘플링이란?

- 단어의 개수가 많아지면, softmax 함수를 계산할때 계산량이 커지게 된다. (분모의 sum)
- 이를 해결하기 위해 모든 단어의 weight를 학습하는 것이 아닌 목표단어(주변 단어)와 목표단어와 동떨어져있는 몇개의 단어만을 선택하여 weight를 업데이트한다.
- **더 공부필요....**

### 10. 계층적 소프트맥스란?

- softmax 함수로 확률을 계산하는 것 대신, binary tree를 이용하여 값을 얻는다.
- root에서 leaf까지 가는 길의 확률을 모두 곱하여 출력값을 계산한다.




# 8. Optimizer 발전 과정 (SGD, RMSprop, Adam)

### 01. SGD

- 경사 하강법과 다르게 한번 학습할 때 모든 데이터에 대해 가중치를 조절하는 것이 아니라, 램덤하게 추출한 일부 데이터에 대해 가중치를 조절한다.

### 02. SGD에서 Stochastic의 의미는?

- 전체를 한번에 계산하지 않고 확률적으로 일부 샘플을 구해서 조금씩 나눠서 계산하겠다는 뜻이다.

### 03. 미니배치를 작게 할때의 장단점은?

- batch size가 작아지면 한번에 계산하는 데이터의 양이 작아져 다소 부정확한 gradient를 계산하게 된다. 따라서 각 단계별 계산량은 줄어들지만 학습 시간이 오래 걸리게 된다.

### 04. 모멘텀의 수식을 적어 본다면?

- momentum rate * 이전 업데이트 - learning rate * 현재 gradient
- V(1) = -learning rate * 현재 gradient, V(2) = m * V(1) - learning rate * 현재 gradient, V(3) = m * V(2) - learning rate * 현재 gradient

### 05. RMSprop

- 학습 할수록 learning rate를 줄여 나가면서 최적화하는 알고리즘인 Adagrad의 수정 버전이다.
- Adagrad에서는 현재부터 이전까지의 gradient 제곱 합만큼 learning rate를 줄여나가다 보니 learning rate가 너무 작아지는 문제가 발생하여 이를 해결하기 위해 RMSprop를 만들었다.
- 지수이동평균 적용을 적용하여 과거일수록 gradient를 적게 반영하여 learning rate가 0으로 수렴하는 것을 방지하였다. 
- 즉, learning rate에  v_t = decay factor * v_t-1 + (1 - decay factor) * 현재 gradient

### 06. Adam

- RMSprop와 momentum을 합친 최적화 알고리즘이다.
- 즉, learning rate를 decay하면서 이전  gradient 정보들을 기억하여 업데이트에 반영하는 모멘텀을 동시에 업데이트한다.

![optimizer](https://t1.daumcdn.net/cfile/tistory/9906BE3D5A3A642E06)



# 9. Batch Normalization

### 01. Batch Normalization의 동작은?

- 네트워크 사이의 데이터 분포를 변화시키기 위한 layer를 추가한다.
- 이때 입력 레이어의 출력에 평균, 분산을 구하고 normalization 한다. 그 후 beta, lambda 변수를 추가하여 scale과 shift 연산을 추가한다.
- 즉, 이전 레이어의 mini-batch 데이터에서 평균과 분산을 구하고 평균이 0, 분산이 1인 데이터 분포를 만들고, lambda를 곱하여 scale를 조정한다. 그리고 beta를 더하여 shift 해준다.

### 02. 효과는?

- Covariate Shift (현재 layer의 입력 분포가 바뀌어 버리는 현상)을 해결
- Overfitting 문제 완화

### 03. Dropout의 효과는?

- Overfitting 문제를 막기 위해 Regularization 효과를 준다.
- 여러 개의 모델을 학습하는 효과를 누릴 수 있다.

### 04. BN 적용해서 학습 이후 실제 사용시에 주의할 점은? 코드로는?

- 학습시 batch별 평균, 분산을 저장하고 beta와 lambda를 학습한 다음, 테스트에서는 batch별 평균과 분산에서의 이동 평균 또는 지수 평균을 사용하여 고정하고, beta와 lambda를 이용하여 적용한다.

### 05. GAN에서 Generator 쪽에도 BN을 적용해도 될까?

- discriminator의 input과 generator output에 batch norm을 적용하는 것은  피해야 한다. 더 자세히 공부할것....

### 06. Whitening은 왜 사용하면 안되는가?

- Whitening은 입력 데이터의 표준편차를 1로 평균을 0으로 만드는 정규화방법이다.
- 만약 z = wx + b라는 결과를 출력하는 네트워크에서 whitening을 사용하면 z에 E(z)를 빼주는 작업을 진행 할 것이다. 이때 bias인 b값은 없어지게 되고 b의 영향이 사라지게 된다. 즉, 학습이 가능한 파라미터를 무시해버린다. (z - E(z) = wx + b - wE(x) - b = wx - wE(x))
- 또한 다음 레이어에서 활성화 함수로 sigmoid를 사용하게 된다면 비선형성의 특징을 사라지게 만든다. (sigmoid는 [-2, 2] 구간에서 선형성을 가진다.)



# 10. CycleGAN

### 01. CycleGAN이란?

- ​















### 00. 역전법

- neural network에서 gradient descent를 chain rule을 사용하여 단순화시킨 것

