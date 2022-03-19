# 오토인코더의 모든 것

- 오토인코더의 모든것 강의를 보고 정리하는 문서
- Link: [오토인코더의 모든 것](https://d2.naver.com/news/0956269)

# 강의 목표

- Chapter 1. Revisit Deep Neural Networks
  - Deep Learning의 기본 지식 돌아보기
  - Loss Function의 2가지 해석 방법 (Back-Propagation, **Maximum Likelihood**)


# AE의 4가지 Keyword

1. Unsupervised Learning $\rightarrow$ 학습 방법
2. Nonlinear Dimensionality Reduction (~ **Manifold Learning**) $\rightarrow$ 인코더 네트워크
3. Generative Model Learning $\rightarrow$ 디코더 네트워크
4. Maximum Likelihood Density Estimation (VAE) $\rightarrow$ Loss가 Negative ML로 해석됨

# Machine Learning Problem (Classic)

1. Collect training data
2. Define function
   - 모델 종류
   - Loss Function
3. Learning / Training
   - 주어진 데이터를 제일 잘 설명하는 모델 찾기, 최적 파라미터 찾기
4. Predicting / Testing
   - 고정 입력 $\rightarrow$ 고정 출력







# 01. Revisit Deep Neural Network

- 챕터의 목적: DNN 해석을 ML density estimation으로 볼 수 있어야 한다.
- 전통적인 Machine Learning
  - 데이터 수집
  - 모델 정의 (모델 종류, Loss Function)
  - 모델 학습 (모델의 파라미터)
  - 모델 테스트 (고정 입력 $\rightarrow$ 고정 출력)
- Deep Learning
  - 전통적인 ML과 다른 점
  - 네트워크 구조를 정한다.
  - Loss Function 정의 (MSE, Cross Entropy - API)
    - Assumption 1. 학습 데이터의 모든 로스는 각 샘플의 로스들의 합으로 나와야한다.
    - Assumption 2. 로스는 네트워크의 출력과 정답 레이블만을 가지고 한다. 중간 레이어의 출력을 이용하여 로스를 구하면 안된다.
    - GoogleNet 은 중간 네트워크에서 로스를 구하는 것처럼 보이지만 종단 네트워크의 출력을 이용한다.
  - 모델 학습 $\rightarrow$ Gradient Descent
    - 목적: L($\theta + \Delta\theta$) 이 L($\theta$) 보다 작아지도록 $\Delta\theta$를 찾는것
    - L($\theta + \Delta\theta$)는 테일러 공식에 의해 $L(\theta + \Delta\theta)=L(\theta)+\nabla L*\Delta\theta+2derivative + 3der+ ...$ 으로 쓸 수 있다.
    - 1차 derivative를 사용하여 추정할 수 있고, 이를 이용하여 변화량을 계산할 수 있다.
    - $L(\theta + \Delta\theta) - L(\theta)=\Delta L = \nabla L * \Delta\theta$
    - IF $\Delta\theta=-\eta\nabla L$ , Then $\Delta L = -\eta||\nabla L||^2 < 0$ 로 할 수 있다.
    - **즉, 1차 미분계수를 이용하여 Learning Rate만큼 파라미터를 이동 시킨다면 Loss Function을 작아지도록 학습 할 수 있다.**
    - 그러나 계속 작아지지는 않는 경우도 있는데 이유는 1차 미분계수를 이용한 추정 때문이다. 그래서 최대한 작은 Learning rate를 이용하여야 비슷한 추정값을 얻을 수 있다.

# Reference

- [오토인코더의 모든것](https://www.youtube.com/watch?v=o_peo6U7IRM&t=493s)