import math

def calculateCorrelation(sns_data,tourist_data):
    """
    Calculates and returns the correlation value for the data
    provided in lists sns_data and tourist_data
    """

    #init
    sum_sns_vals=sum_tourist_vals=0
    sum_sns_sqrd=sum_tourist_sqrd=0
    sum_products = 0

    #calculate intermediate correlation values
    num_values= len(sns_data)

    for k in range(0,num_values):
        sum_sns_vals=sum_sns_vals+sns_data[k]
        sum_tourist_vals=sum_tourist_vals+tourist_data[k]

        sum_sns_sqrd=sum_sns_sqrd+sns_data[k]**2
        sum_tourist_sqrd=sum_tourist_sqrd+tourist_data[k]**2

        sum_products=sum_products + sns_data[k]*tourist_data[k]

    #calculate and display correlation value
    numer=(num_values*sum_products)-(sum_sns_vals*sum_tourist_vals)
    denom=math.sqrt(abs(\
        ((num_values*sum_sns_sqrd)-(sum_sns_vals**2))*\
        ((num_values*sum_tourist_sqrd)-(sum_tourist_vals**2)) ))

    return numer/denom

def analysis(correlation):
    if correlation>0:
        if correlation<=0.4:
            print("두 요소는 약한 양의 상관관계에 있습니다.")
        elif correlation<=0.8:
            print("두 요소는 중간 정도의 양의 상관관계에 있습니다.")
        elif correlation<1:
            print("두 요소는 강한 양의 상관관계에 있습니다.")
        elif correlation==1:
            print("두 요소는 완벽한 양의 상관관계에 있습니다.")

    elif correlation==0:
        print("두 요소는 상관관계가 없습니다.")

    elif correlation<0:
        if correlation>=-0.4:
            print("두 요소는 약한 음의 상관관계에 있습니다.")
        elif correlation>=-0.8:
            print("두 요소는 중간 정도의 음의 상관관계에 있습니다.")
        elif correlation>-1:
            print("두 요소는 강한 음의 상관관계에 있습니다.")
        elif correlation==-1:
            print("두 요소는 완벽한 음의 상관관계에 있습니다.")
