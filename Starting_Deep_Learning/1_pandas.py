import pandas as pd

print('\n')
f'''
{print('시리즈(Series)')}
시리즈(Series)
1차원 배열 값(values)와 각 값에 대응되는 인덱스(index)를 부여하는 구조
'''
# 시리즈 선언
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])    

# 시리즈(Series) 출력
print("시리즈 출력 :")
print('-'*15)
print(sr)

# 값(values)과 인덱스(index) 출력 
print('-'*20)
print(f'시리즈의 값 : {sr.values}')
print(f'시리즈의 인덱스 : {sr.index}')

print('\n')
f'''
{print('데이터프레임(DataFrame)')}
데이터프레임(DataFrame)
2차원 리스트를 매개변수로 전달.
    2차원 : 행방향 인덱스(index), 열방향 인덱스(column)
행과 열을 가지는 자료구조

시리즈 : 인덱스,값
데이터프레임 : 인덱스, 값, 열
'''
# 데이터프레임 선언
values = [[1,2,3,],[4,5,6],[7,8,9]]
index = ['one','two','three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)

print("데이터프레임 출력 :")
print("-"*18)
print(df)

# 인덱스, 값, 열 출력
print(f'데이터프레임의 인덱스: {df.index}')
print(f'데이터프레임의 열이름: {df.columns}')
print('데이터프레임의 값:')
print(df.values)

print('\n')
f'''
{print('데이터프레임의 생성')}
데이터프레임의 생성
리스트, 시리즈, 딕셔너리, Numpy의 ndarrays, 다른 데이터프레임
으로부터 생성가능
'''

# 리스트로 데이터프레임 생성
data = [
    ['1000','Steve',90.72],
    ['1001','James',78.09],
    ['1002','Doyeon',98.43],
    ['1003','Jane',64.19],
    ['1004','Pilwoong',81.30],
    ['1005','Tony',99.14],
]
df = pd.DataFrame(data)
print(f'list로 생성한 Dataframe:\n{df}')
print('-'*25)
# 열 지정
df = pd.DataFrame(data, columns=['학번','이름','점수'])
print(f'열 지정:\n{df}')
print('\n')

# 딕셔너리로 데이터프레임 생성
data = {
    '학번' : ['1000','1001','1002','1003','1004','1005'],
    '이름' : ['Steve','James','Doyeon','Jane','Pilwoong','Tony'],
    '점수' : [90.72,78.09,98.43,64.19,81.30,99.14]
}
df = pd.DataFrame(data)
print(f'dicionary로 생성한 Dataframe:\n{df}')

print('\n')
f'''
{print('데이터프레임 조회')}
데이터프레임 조회
df.head(n) - 앞 부분을 n개만 보기
df.tail(n) - 뒤 부분을 n개만 보기
df['열이름'] - 해당되는 열을 확인
'''
# 앞 부분을 3개만 보기
print(df.head(3))
print('-'*30)
# 뒷 부분을 3개만 보기
print(df.tail(3))
print('-'*30)
# 학번에 해당되는 열을 보기
print(df['학번'])

print('\n')
f'''
{print('외부 데이터 읽기')}
외부 데이터 읽기
.csv, .txt, .xls, .ssql, .json 등 다양한 파일 읽고 생성 가능
'''
# .csv
df=pd.read_csv('./src/1_example.csv')
print(df)
# 자동으로 부여된 index 출력
print(df.index)