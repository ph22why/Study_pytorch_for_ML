import numpy as np

f'''
{print('np.array()')}
np.array()
Numpy의 핵심은 ndarray다.
np.array()는 리스트, 튜플, 배열 로부터 ndarray를 생성한다.
'''
# 1차원 배열 생성
vec = np.array([1,2,3,4,5])
print(vec)
print('-'*15)
# 2차원 배열 생성
# array()안에는 하나의 리스트만 들어가므로 리스트의 리스트를 넣어줘야함.
mat = np.array([[10,20,30],[60,70,80]])
print(mat)
print('-'*15)
# 두 배열의 타입 확인
print(f'vec의 타입 :{type(vec)}')
print(f'vec의 타입 :{type(mat)}')
print('-'*15)
'''
축의 개수와 크기
Numpy배열에는 축의 개수(ndim)와 크기(shape)존재.
배열의 크기를 정확히 숙지하는 것은 딥 러닝에서 매우 중요하다.
축의 개수와 크기는 백터와 행렬 연산 때 언급
'''
print(f'vec의 축의 개수 :{vec.ndim}')
print(f'vec의 크기(shape) :{vec.shape}')
print(f'mat의 축의 개수 :{mat.ndim}')
print(f'mat의 크기(shape) :{mat.shape}')
print('\n')

f'''
{print('ndarray 초기화')}
ndarray 초기화
ndarray를 생성하는 방법에는 리스트외에 다양한 방법들이 존재한다.
'''
# np.zeros() : 배열의 모든 원소에 0을 삽입
# 2x3배열생성
zero_mat = np.zeros((2,3))
print(zero_mat)
print('-'*15)
# np.ones() : 배열의 모든 원소에 1을 삽입
# 2x3배열생성
one_mat = np.ones((2,3))
print(one_mat)
print('-'*15)
# np.full() : 배열에 지정한 값을 삽입
# 2x2배열생성
sample_value_mat = np.full((2,2), 7)
print(sample_value_mat)
print('-'*15)
# np.eye() : 대각선으로는 1, 나머지는 0인 2차원배열 생성
eye_mat = np.eye(3) 
print(eye_mat)
print('-'*15)
# np.random.random() : 임의의 값을 가지는 배열 생성
random_mat = np.random.random((2,2))
print(random_mat)
print('\n')

f'''
{print('np.arange()')}
np.arange()
np.arange(n) 0부터 n-1까지의 값을 가지는 배열을 생성
np.range(i,j,k) i부터 j-1까지 k씩 증가하는 배열을 생성
'''
# 0부터 9까지
range_vec = np.arange(10)
print(range_vec)
# 1부터 9까지 +2씩 적용되는 범위
n = 2
range_n_step_vec = np.arange(1,10,n)
print(range_n_step_vec)
print('\n')

f'''
{print('np.reshape()')}
np.reshape()
내부 데이터는 변경하지 않으면서 배열의 구조를 바꾼다.
- arange(30)으로 0부터 29까지 숫자 생성,
- 5행6열의 행령로 변경
'''
reshape_mat = np.array(np.arange(30)).reshape((5,6))
print(reshape_mat)
print('\n')

f'''
{(print('Numpy 슬라이싱'))}
Numpy 슬라이싱
ndarray를 통해 만든 다차원의 배열을 리스트처럼 슬라이싱(slicing)가능
특정 행이나 열들의 원소들 접근 가능
'''
print('-'*20)
print('ndarray 생성:')
mat = np.array([[1,2,3],[4,5,6]])
print(mat)
# 첫번째 행 출력
print('첫번째 행 출력:')
slicing_mat = mat[0, :]
print(slicing_mat)
# 두번째 열 출력
print('두번째 열 출력:')
slicing_mat = mat[:, 1]
print(slicing_mat)
print('\n')

f'''
{(print('Numpy 정수 인덱싱(integer indexing)'))}
Numpy 정수 인덱싱(integer indexing)
슬라이싱은 부분 배열을 추출 가능하지만, 특정 부분은 출력 안된다.
'''
print('배열 생성:')
mat = np.array([[1,2],[4,5],[7,8]])
print(mat)
print('특정 위치 원소 가져오기')
# 1행 0열의 원소
# => 0부터 카운트하므로 두번째 행 첫번째 열의 원소
print(mat[1,0])
print('특정 위치의 원소를 두개 가져와 새로운 배열 생성')
# mat[[2행, 1행],[0열, 1열]]
# 각 행과 열의 쌍을 매칭하면 2행 0열, 1행 1열의 두 개의 원소.
indexing_mat = mat[[2,1],[0,1]]
print(indexing_mat)
print('\n')

f'''
{(print('Numpy 연산'))}
Numpy 연산
배열간 연산을 쉽게 가능
+,-,*,/
np.add(), np.subtract(), np.multipy(), np.devide()
'''
print('요소별 셈')
x = np.array([1,2,3])
y = np.array([4,5,6])
# result = np.add(x, y)
result = x + y
print(result)

# result = np.subtract(x,y)
result= x - y
print(result)

# result = np..multipy(result, x)
result = result * x
print(result)

# result = np.divide(result, x)
result = result / x
print(result)
print('-'*20)
# 벡터와 행렬곱 || 행렬곱을 위해서는 dot()사용
print('행렬별 곱')
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)
print('\n')