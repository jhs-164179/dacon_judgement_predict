def preprocessing(df, cols, shortword, tokenizer, stopword, lemmatizer):
    import numpy as np
    import re
    
    first_party_lst = []
    second_party_lst = []
    facts_lst = []
    for col in cols:
        # 좌우 공백 제거
        df[col] = df[col].str.strip()
        # 두 칸 이상의 공백 한 칸으로 변경
        df[col] = df[col].str.replace('  ', ' ')
        # 소문자로 변경
        df[col] = df[col].str.lower()
        # ",", "." 제거
        df[col] = df[col].str.replace(',','')
        df[col] = df[col].str.replace('.','')

        if col == 'first_party':
            for sample in df[col]:
                # 한글자 단어 제거
                sample = shortword.sub('', sample)
                # 특수문자 제거
                sample = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", sample)
                # tokenzier를 이용한 단어 토큰화
                token = tokenizer.tokenize(sample)
                # 불용어 제거
                new_token = []
                for tok in token:
                    if tok not in stopword:
                        # 표제어 추출
                        new_token.append(lemmatizer.lemmatize(tok, 'n'))
                first_party_lst.append(new_token)
            # sklearn.feature_extraction 변환을 위해 단어들을 결합
            for i in range(len(first_party_lst)):
                first_party_lst[i] = ' '.join(first_party_lst[i])

        elif col == 'second_party':
            for sample in df[col]:
                # 한글자 단어 제거
                sample = shortword.sub('', sample)
                # 특수문자 제거
                sample = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", sample)
                # tokenzier를 이용한 단어 토큰화
                token = tokenizer.tokenize(sample)
                # 불용어 제거
                new_token = []
                for tok in token:
                    if tok not in stopword:
                        # 표제어 추출
                        new_token.append(lemmatizer.lemmatize(tok, 'n'))
                second_party_lst.append(new_token)
            # sklearn.feature_extraction 변환을 위해 단어들을 결합
            for i in range(len(second_party_lst)):
                second_party_lst[i] = ' '.join(second_party_lst[i])

        elif col=='facts':
            for sample in df[col]:
                # 한글자 단어 제거
                sample = shortword.sub('', sample)
                # 특수문자 제거
                sample = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", sample)
                # tokenzier를 이용한 단어 토큰화
                token = tokenizer.tokenize(sample)
                # 불용어 제거
                new_token = []
                for tok in token:
                    if tok not in stopword:
                        new_token.append(tok)
                facts_lst.append(new_token)
            # sklearn.feature_extraction 변환을 위해 단어들을 결합
            for i in range(len(facts_lst)):
                facts_lst[i] = ' '.join(facts_lst[i])

        else:
            print('컬럼이름을 변경하지 말아주세요!')

    return first_party_lst, second_party_lst, facts_lst
                
def preprocessing_2(first, second, facts, vec, vec_facts, train=True):
    import numpy as np
    if train:
        vec.fit(first + second)
        vec_facts.fit(facts)

    X1 = vec.transform(first).toarray()
    X2 = vec.transform(second).toarray()
    X3 = vec_facts.transform(facts).toarray()

    return np.concatenate([X1, X2, X3], axis=1)
