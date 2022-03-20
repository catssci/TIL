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

# Machine Learning Problem (DNN)

1. Collect training data
2. **Define function**
   - 모델 종류: DNN 구조 결정 (FN, CNN, RNN, ...)
   - Loss Function: MSE, Cross Entropy (두개의 Loss만 정의 가능?)
   - Loss Function의 가정 (Back-Propagation을 사용해야 하기 때문)
     - Assumption 1. 학습 데이터의 모든 로스는 각 샘플의 로스들의 합으로 나와야한다.
     - Assumption 2. 로스는 네트워크의 출력과 정답 레이블만을 가지고 한다. 중간 레이어의 출력을 이용하여 로스를 구하면 안된다.
     - Google-Net 은 중간 네트워크에서 로스를 구하는 것처럼 보이지만 종단 네트워크의 출력을 이용한다.
     - $L(f_{\theta}(x), y) = \sum_{i}L(f_{\theta}(x_i), y_i)$
3. **Learning / Training**
   - 최적 파라미터 찾기 $\rightarrow$ Gradient Descent
   - Gradient Descent는 Iterative Method로 다음 3가지 질문을 답할 수 있어야 함
     1. How to Update? $\rightarrow$ Only if $L(\theta + \Delta\theta) < L(\theta)$

     2. When we stop to search? $\rightarrow$ If $L(\theta + \Delta\theta) == L(\theta)$

     3. How to find $\Delta\theta$ so that $L(\theta + \Delta\theta) < L(\theta)$? $\rightarrow$ **$\Delta\theta = -\eta\nabla L$**, where $\eta > 0$

        - $L(\theta + \Delta\theta) = L(\theta) + \nabla L * \Delta\theta$ + second derivative + ...   by Taylor Expansion

        - $L(\theta + \Delta\theta) \sim L(\theta) + \nabla L * \Delta\theta$

          $L(\theta + \Delta\theta) - L(\theta)= \Delta L =\nabla L * \Delta\theta$

          If $\Delta\theta = -\eta\nabla L$, then $\Delta L = -\eta {||\nabla L||}^2 < 0$, where $\eta > 0$ and called learning rate

        - 위와 같은 접근 방법을 통해서 $-\eta\nabla L$ 만큼 $\theta$를 업데이트함으로써 Loss 값을 작게 할 수 있다. 테일러 항에서 1차 미분항까지만을 사용했기에 아주 좁은 영역에서만 감소 방향을 정확히 알 수 있다. 그래서 Learning rate의 값은 매우 작게 설정하여야 한다.

        - $\nabla L$를 구할 때에는 모든 training data를 통해 구해야 한다. $\nabla L(\theta_k, D)\sim \sum_{i}\nabla L(\theta_k, D_i) / N$

          그러나 샘플의 수가 커지면 계산 시간이 너무 오래 걸리므로 SGD 방법 (mini-batch)이 개발 되었다. $\nabla L(\theta_k, D)\sim \sum_{i}\nabla L(\theta_k, D_i) / M$, where $M < N$

     - 결론적으로 Gradient Descent 방법을 통해 모델의 파라미터를 업데이트하고, 이때의 gradient는 back-propagation을 적용하여 모든 네트워크의 gradient를 쉽게 구할 수 있다.

4. Predicting / Testing

   - 고정 입력 $\rightarrow$ 고정 출력


# Loss Function의 2가지 관점으로 해석하기

### View Point 1. Back-Propagation

- MSE Loss 와 CE Loss 를 Back-Propagation의 관점으로 비교한다면 다음과 같다.
- MSE Loss
  - output layer의 출력: $a, a = \sigma(z), z = \displaystyle \sum_i{w_i*x_i}+b$ 라 한다면 다음과 같이 그레디언트를 구할 수 있다.
  - $C = \displaystyle \frac{(a- y)^2}{2}$
  - $\displaystyle \frac{\partial C}{\partial a} = (a - y),  \ \ \frac{\partial C}{\partial z}=\frac{\partial C}{\partial a}*\frac{\partial a}{\partial z} = (a - y)*(1 - \sigma(z))*\sigma(z) = (a - y)*(1 - a)*a$
  - $\displaystyle \frac{\partial C}{\partial w} =  \frac{\partial C}{\partial a} *  \frac{\partial a}{\partial z}*  \frac{\partial z}{\partial w} = (a-y)*(1-a)*a*x$
  - $\displaystyle \frac{\partial C}{\partial b} =  \frac{\partial C}{\partial a} *  \frac{\partial a}{\partial z}*  \frac{\partial z}{\partial b} = (a-y)*(1-a)*a$
  - **(1-a)*a**는 activation function의 미분값이다. 이때 a는 w,b에 의해 결정되고, sigmoid의 경우 미분값의 최댓값이 0.25이고 일정 범위를 벗어나면 급격히 작아져 계산되는 그레디언트 결과도 작아진다. 결국 activation function 선택으로 gradient vanishing 문제가 발생할 수 있고, 초기 w, b의 선택으로 a의 값이 0.5와 멀어지는 경우 학습 속도가 굉장히 작아지게 된다.
- CE Loss
  - output layer의 출력: $a, a = \sigma(z), z = \displaystyle \sum_i{w_i*x_i}+b$ 라 한다면 다음과 같이 그레디언트를 구할 수 있다.
  - $C = -[y * ln(a) + (1-y)*ln(1 - a)]$
  - $\displaystyle \frac{\partial C}{\partial a} = \frac{a-y}{(1-a)*a},  \ \ \frac{\partial C}{\partial z}=\frac{\partial C}{\partial a}*\frac{\partial a}{\partial z} = \frac{a-y}{(1-a)*a}*(1 - \sigma(z))*\sigma(z) = \frac{a-y}{(1-a)*a}*(1 - a)*a = a-y$
  - $\displaystyle \frac{\partial C}{\partial w} =  \frac{\partial C}{\partial a} *  \frac{\partial a}{\partial z}*  \frac{\partial z}{\partial w} = (a-y)*x$
  - $\displaystyle \frac{\partial C}{\partial b} =  \frac{\partial C}{\partial a} *  \frac{\partial a}{\partial z}*  \frac{\partial z}{\partial b} = (a-y)$
  - CE Loss를 사용한 출력 레이어에서는 activation function의 미분값이 곱해지지 않으며 (sigmoid 경우), 이때문에 gradient vanishing 문제에 강건할 수 있다. 그러나 여러 레이어가 쌓이고 그에 따른 activation function을 사용한다면 마찬가지로 gradient vanishing 문제가 발생할 가능성이 있다.
- 결론: Back-Propagation의 관점에서 본다면 CE Loss 사용이 더 좋은 경향을 보인다.

### View Point 2. Maximum Likelihood

- 네트워크 출력을 **정해진 확률분포에서 출력이 나올 확률** 이라고 해석한다. 확률 분포를 선택하고 출력 $f_{\theta}(x)$는 확률분포의 파라미터로 해석이 가능해진다.
- 그럼 결국 $p(y\mid f_{\theta}(x))$에서 likelihood가 최대가 되는 $f_{\theta}$를 찾는 것으로 해석된다. (likelihood가 최대 일때 = $f_{\theta}(x) = y$)
- 확률 분포 모델을 찾는 것으로 생각하면 Sampling을 할 수 있고, 그러면 고정 입력을 통해 다른 출력 값을 가지게 될 수 있다.
- ​