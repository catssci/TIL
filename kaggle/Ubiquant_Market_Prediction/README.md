# 캐글 공모전

- 공모전 이름: [Ubiquant Market Prediction](https://www.kaggle.com/c/ubiquant-market-prediction)
- 기간: 2022.01.19 ~ 2022.04.12



# 공모전 정보

- Ubiquant: 중국의 해지펀드 회사
- 공모전 목적: 투자 수익률을 예측하는 모델 구축 (build a model that forecasts an investment's return rate)
- 평가 방법: Pearson correlation coefficient ?? 이게 맞나? (mean of the Pearson correlation coefficient for each time ID)



# 공모전 데이터

```bash
├── train.csv
├── example_test.csv
├── example_sample_submission.csv
└── ubiquant
    ├── __init__.py
    └── competition.cpython-37m-x86_64-linux-gnu.so
```
- train.csv
  - `row_id` : 각 행을 나타내는 인덱스 id
  - `time_id` : 데이터가 수집된 시간에 대한 id code, 시간 사이의 값이 일정하지 않는다. 테스트 데이터에서는 훈련 데이터보다 짧아질 것으로 예상된다.
  - `investment_id` : 투자 id code, 모든 투자가 모든 시간 Id를 가지는 것이 아니다?
  - `target` : target
  - `f_0 ~ f_299` : 암호화된 시장 데이터
- example_test.csv
- example_sample_submission.csv


# 정리
- [Fast Data from parquet](https://github.com/catssci/TIL/blob/main/kaggle/Ubiquant_Market_Prediction/fast-data-loading-from-parquet.ipynb)
    - parquet file data format 데이터 설명 (속도 및 메모리 최적화, 데이터 type)
    - train data Loading 속도 비교, `investment_id`별 데이터 Load 방법, 특정 열 Load 방법 정리
    - size 비교: 18GB >> 5.5GB >> **3.63GB**
    - time 비교: crash >> 56s >> **36s**
- [Understand on competition using sklearn Linear Regression](https://github.com/catssci/TIL/blob/main/kaggle/Ubiquant_Market_Prediction/linear-regression-using-sklearn.ipynb)
    - sklearn의 Linear Regression을 이용한 대회 이해 목적의 노트북
- [BaseLine](https://github.com/catssci/TIL/blob/main/kaggle/Ubiquant_Market_Prediction/baseline.ipynb)
    - 속도와 저장 공간을 절약한 데이터 불러오기
    - 각 피쳐별 분포, 상관관계 EDA
- [BaseModel](https://github.com/catssci/TIL/blob/main/kaggle/Ubiquant_Market_Prediction/base-model.ipynb)
    - lightgbm 모델을 사용한 model
    - **valid rmse: 0.897498, Public Score: 0.110**
- [simple dnn model using Pytorch]()
    - pytorch를 이용한 간단 dnn 모델
    - **valid rmse: --, Public Score: --**

# 참고 노트북

- [🛒 Ubiquant - Exploration+Baseline w\ SHAP🛒](https://www.kaggle.com/utcarshagrawal/ubiquant-exploration-baseline-w-shap)
- [⏫ Fast Data Loading and Low Mem with Parquet Files](https://www.kaggle.com/robikscube/fast-data-loading-and-low-mem-with-parquet-files)
- [👀✔WhyonlyKeras? Easy Pytorch Competitive DNN 💖](https://www.kaggle.com/sahil112/whyonlykeras-easy-pytorch-competitive-dnn)
