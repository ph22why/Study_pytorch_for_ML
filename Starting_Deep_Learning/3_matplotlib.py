import matplotlib.pyplot as plt
f'''
{print('맷플롯립(Matplotlib')}
맷플롯립(Matplotlib)
데이터를 차트(chart)나 플롯(plot)으로 시각화하는 패키지이다.
Matplotlib은 데이터 분석 이전에 데이터 이해를 위한 시각화,
데이터 분석 후에 결과를 시각화하기 위해서 사용된다.
'''

f'''
1) 라인 플롯 그리기
plopt()은 라인 플롯을 그리는 기능을 수행.
title('제목')을 사용해서 제목 지정 가능.
'''
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])   
plt.show()
print('\n')

f'''
축 레이블 삽입
xlabel('x축 이름')
ylabel('y축 이름')
'''
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.xlabel('hours')
plt.ylabel('score')  
plt.show()
print('\n')

f'''
라인 추가와 범례 삽입
다수의 plot()을 하나의 그래프에 나타낼 수 있다.
여러개의 라인 플롯을 동시에 사용할 경우, 어떤 데이터인지 보여주기위해
범례(legend)를 사용할 수 있다.
'''
plt.title('students')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student']) # 범례 삽입
plt.show()