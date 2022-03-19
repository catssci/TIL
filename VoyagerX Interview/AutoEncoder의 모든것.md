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

