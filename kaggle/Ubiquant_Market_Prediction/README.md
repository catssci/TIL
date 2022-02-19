# 캐글 공모전

- 공모전 이름: Ubiquant Market Prediction
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



# 참고 노트북

- [🛒 Ubiquant - Exploration+Baseline w\ SHAP🛒](https://www.kaggle.com/utcarshagrawal/ubiquant-exploration-baseline-w-shap)
- ​
