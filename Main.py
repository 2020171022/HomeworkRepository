import OpenFiles
import ReadFiles
import Calculate
import count
import numpy


#program greeting
print("This program will determine the correlation between")
print("the ratio of positive words about certain place on SNS and actual number of tourists.")

#SNS 분석 파일들과 관광인구 분석 파일들을 입력받음.
"""
입력받는 SNS 분석파일과 관광 인구 분석 파일들의 장소 순서가 일치해야함.
경의선 책거리 SNS, 망리단길 SNS 순으로 입력했다면 경의선 책거리 관광인구, 망리단길 관광인구 순서로 입력
"""
print("SNS 분석 파일들을 입력하세요. 파일이 여러개라면 파일명을 사전식 순서로 입력하세요.")
sns_files=OpenFiles.openfiles_cp949()
print("관광인구 분석 파일들을 입력하세요. 파일이 여러개라면 파일명을 사전식 순서로 입력하세요.")
tourist_files=OpenFiles.openfiles()

#Read SNS Files. 각 장소별 긍정어 비율의 평균을 구해 리스트로 저장
sns_positive_ratio=[]
for file in sns_files:
    sns_data,ratio_positive_lst=ReadFiles.readSNSFiles(file)
    mean=numpy.mean(ratio_positive_lst)
    sns_positive_ratio.append(mean)
    
#Read Number of tourists Files. 각 장소별 관광객수의 평균을 구해 리스트로 저장.
total_tourists=[]
for file in tourist_files:
    tourist_data,total=ReadFiles.readTouristFiles(file)
    mean=numpy.mean(total)
    total_tourists.append(mean)

#Calculate Correlation
correlation=Calculate.calculateCorrelation(sns_positive_ratio,total_tourists)
print("SNS 긍정어의 비율과 실제 관광객 수의 상관계수는",correlation,"입니다.")
Calculate.analysis(correlation)

#모범 음식점 자료 분석
'''
sns와 관광인구 자료가 대상으로 하는 장소들의 도로명을 리스트에 저장함.
모범 음식점 자료에서 해당 도로명이 나오는 횟수를 구해 장소 주변의 모범 음식점 수를 구하고
리스트에 저장함.
'''
road=['와우산로','포은로','월드컵로','양화로','토정로','월드컵로','월드컵로','어울마당로','어울마당로']
num_restaurants=[]

csv_file_path = '서울특별시 마포구_모범음식점 목록.csv'
column_to_search = '소재지(도로명)'

for word in road:
    word_to_find = word
    result = count.count_word_in_column(csv_file_path, column_to_search, word_to_find)
    num_restaurants.append(result)

#SNS 긍정어 비율과 모범 음식점 수의 상관계수 계산
new_sns_data=sns_positive_ratio[:8]+sns_positive_ratio[9]    #홍대 주차장 골목 제거
correlation_sns_restaurant=Calculate.calculateCorrelation(new_sns_data,num_restaurants)
print("SNS게시물에서 긍정어의 비율과 해당 장소 주변 모범 음식점 수의 상관계수는",correlation_sns_restaurant,"입니다.")
Calculate.analysis(correlation_sns_restaurant)

#관광 인구와 모범 음식점 수의 상관계수 계산
new_tourist_data=total_tourists[:8]+total_tourists[9]      #홍대 주차장 골목 제거
correlation_tourist_restaurant=Calculate.calculateCorrelation(new_tourist_data,num_restaurants)
print("관광 인구와 해당 장소 주변 모범 음식점 수의 상관계수는",correlation_tourist_restaurant,"입니다.")
Calculate.analysis(correlation_tourist_restaurant)
