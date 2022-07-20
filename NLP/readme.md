1. Transformer 정리
  - 챗봇 구현
2. KoBERT
  - https://github.com/SKTBrain/KoBERT/tree/master/kobert_hf
  - KoBERT Tokenizer
  ```Python
  >>> from tokenization_kobert import KoBertTokenizer
  >>> tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert') # monologg/distilkobert도 동일
  >>> tokenizer.tokenize("[CLS] 한국어 모델을 공유합니다. [SEP]")
  >>> ['[CLS]', '▁한국', '어', '▁모델', '을', '▁공유', '합니다', '.', '[SEP]']
  >>> tokenizer.convert_tokens_to_ids(['[CLS]', '▁한국', '어', '▁모델', '을', '▁공유', '합니다', '.', '[SEP]'])
  >>> [2, 4958, 6855, 2046, 7088, 1050, 7843, 54, 3]
  ```
