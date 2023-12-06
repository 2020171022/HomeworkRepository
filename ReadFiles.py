def readTouristFiles(file):
    """
    관광 인구 분석 파일을 한 줄씩 전체를 읽어 리스트로 저장.
    total tourists column의 값들을 float로 변환하여 리스트로 저장.
    위의 두 리스트를 return.
 
    """
    #관광 인구 분석 파일을 한 줄씩 전체를 읽어 리스트로 저장
    data=file.readlines()
    
    #total tourists column의 값들을 float로 변환하여 리스트로 저장.
    total_tourists=[]
    for line in data[1:]:
        line=line.strip()
        line_lst=line.split(',')
        total_tourists.append(line_lst[3])

    float_total_tourists = [float(value) for value in total_tourists]

    return data,float_total_tourists
        
        
def readSNSFiles(file):
    """
    SNS 분석 파일을 한 줄씩 전체를 읽어 리스트로 저장.
    SNS 게시글에서 긍정어의 비율을 리스트로 저장.
    """

    #SNS 분석 파일을 한 줄씩 전체를 읽어 리스트로 저장.
    data=file.readlines()

    #SNS 게시글에서 긍정어의 비율을 리스트로 저장.
    ratio_positive_lst=[]

    for line in data[1:]:
        line=line.strip()
        line_lst=list(map(int,line.split(',')[1:])) #긍정어,부정어,중립어의 리스트
        if sum(line_lst)==0:
            continue
        ratio_positive=line_lst[0]/sum(line_lst)
        ratio_positive_lst.append(ratio_positive)

    return data,ratio_positive_lst
