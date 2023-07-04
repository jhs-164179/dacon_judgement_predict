대회 : 월간 데이콘 법원 판결 예측 AI 경진대회
링크 : https://dacon.io/competitions/official/236112/overview/description
Private 점수(Accuracy) : 0.54354(3rd)
1st 점수 : 0.57258

[Private 3rd] Downsampling + LogisticRegression

다양한 모델을 테스트해본 결과 학습시간 대비 score가 비슷해서 머신러닝 모델을 사용했습니다.

전처리를 위해 nltk와 re, imblearn의 NeighbourhoodCleaningRule을 사용했습니다.

first, second_party의 경우 CountVectorizer를, facts의 경우 TfidfVectorizer를 ngram_range=(1,2)로 설정하여 벡터화 후,
train_test_split함수를 이용하여 train데이터의 25%를 validation으로 설정하고 LogisticRegression모델로 학습진행하였습니다.

더 테스트해볼게 많았는데 다 해보지는 못해서 아쉽지만, 최선을 다한 결과에 만족스럽고 재밌었습니다.
다들 앞으로도 화이팅하시고 좋은 결과 있으시길 기원합니다! 감사합니다!!

점수 : 
[폴더 및 파일 설명]
data폴더 : 경진대회에 사용한 데이터 셋
old : 테스트해보면서 작성한 코드 및 결과파일
final_submission.ipynb : 최종적으로 작성한 제출 코드
logi__2.csv : 최종 결과파일
utils_two.py : 함수 import용 파일
(원래는 함수가 길어서 utils_two에서 import 해서 썼음)