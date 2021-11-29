import numpy as np
import datetime as dt

def gdp1(a,b): # GDP디플레이터 구하기
    if (b!=0):
        return (a/b) *100

def gdp2(a,b): #명목GDP 구하기
    return a*b 

def gdp3(a,b): #실질 GDP 구하기
    return a*b

def cpi1(a,b): #소비자물가지수 구하기
    return (a/b)*100

def cpi2(a,b): #실질 이자율 구하기
    return a-b 

def save1(a,b,c): #민간저축 구하기
    return a - b - c

def save2(a,b): #정부저축 구하기
    return a-b

def future1(a,b,c): #현재금액의 미래 가치 구하기
    return (1+a)*b*c   

def future2(a,b,c): #미래금액의 현재 가치 구하기
    return a/(1+b)**c

def unemploy1(a,b): #실업률 구하기
    return (b/a+b)*100

def unemploy2(a,b,c): #경제활동 참가율 구하기
    return ((a+b)/c)*100


print("안녕하세요, 경제금융학부 학생들을 위한 계산 프로그램입니다.")
print("원하시는 메뉴의 번호를 입력해주세요.")

while True :
    print(" 1. 오늘의 전공 수업 시간표 확인하기 \n 2. 전공 계산기 사용하기 \n 3. 오늘의 공부 시간 입력하기 \n 4. 프로그램 종료하기 ")  #메뉴의 번호를 입력 받는다. 
    menu = int(input(">"))

    if menu ==1:  #전공 시간표를 선택했을 경우 
        print ("오늘의 전공 시간표 입니다.")
        while True:
              date= input("요일을 입력하세요.(ex.월=1, 이전으로 돌아가고 싶다면 4을 누르세요.) >>")
              if date == "월":
                  print (" 1. 경제학원론: 서은숙 교수님 / T403 (1분반) \n 2. 경제학원론: 서은숙 교수님 / T201 (2분반)")  
              elif date == "화":
                  print (" 1. 경제통계의 이해 : 유경원 교수님 / T201 (1분반) \n 2. 경제통계의 이해 : 유경원 교수님 / T201 (2분반) ")
              elif date == "수":
                  print (" 1.경제통계의 이해 : 유경원 교수님 / N505 (1분반) \n 2.경제통계의 이해 : 유경원 교수님 / N505 (2분반) \n 3. 경제학원론: 서은숙 교수님 / T403 (1분반)")
                  print (" 4. 경제학원론: 서은숙 교수님 / T201 (2분반) \n 5. 경제학원론: 유만식 교수님 / T101")
              elif date == "목":
                  print ("해당 전공이 존재하지 않습니다.")
              elif date == "금":
                  print (" 1. 경제학원론 : 손규현 교수님 / N405")
              elif date == "토":
                  print (" 1. 경제학원론 : 김윤희 교수님 / R203")
              elif date == "4":
                  break
              else:
                  print(" 다시 요일을 입력해주세요.")

    elif menu == 2:  #전공 계산기를 선택했을 경우 
        print("전공 계산기 사용하기 입니다.")
        while True:
            print("원하는 전공의 번호를 입력하세요")
            print (" 1. 경제학원론 \n 2. 경제통계의 이해 \n 3. 이전으로 돌아가기")
            sub = int(input(">>"))
            if sub ==1:  #경제학원론을 선택 할 경우 
                while True:
                    print("단원을 입력해주세요.(ex.23, 4. 이전으로 돌아가기):")  #단원을 숫자로 받는다.
                    unit = int(input(">"))
                    if unit == 23:
                        print ("23장 - 국민소득의 측정")
                        
                        while True:
                             print (" 1. GDP 디플레이터 계산하기 \n 2. 명목 GDP 구하기 \n 3. 실질 GDP 구하기 \n 4. 이전으로 돌아가기")
                             print("원하는 계산의 번호를 입력해주세요.")
                             math = int(input(">>"))
                             if math == 1:
                                 a = float(input("명목 GDP값을 입력하세요.>>"))
                                 b = float(input("실질 GDP값을 입력하세요>>"))
                                 print ("GDP 디플레이터 값은 %.2f 입니다." %gdp1(a,b))
                             elif math == 2:
                                 a = float(input(" 한 나라의 생산량을 입력하세요.>>"))
                                 b = float(input(" 당해 연도의 시장가격을 입력하세요. >> "))
                                 print("명목 GDP의 값은 %.2f 입니다." %gdp2(a,b))
                             elif math == 3:
                                 a= float(input("한 나라의 생산량을 입력하세요.>>"))
                                 b= float(input(" 당해 연도의 시장가격을 입력하세요. >> "))
                                 print("실질 GDP의 값은 %.2f 입니다." %gdp3(a,b))
                             elif math == 4:
                                 break
                             else:
                                 print("다시 번호를 입력해주세요.")
                                    

                    elif unit == 24:
                        print ("24장 - 생계비의 측정")
                        while True:
                            print (" 1. CPI 계산하기 \n 2.실질 이자율 구하기 \n 3. 이전으로 돌아가기")
                            print ("원하는 계산의 번호를 입력해주세요.")
                            math = int(input(">>"))
                            if math == 1:
                                 a = float(input("재화묶음 비용을 입력하세요.>>"))
                                 b = float(input("기준연도 재화묶음 비용을 입력하세요>>"))
                                 print ("CPI 값은 %.2f 입니다." %cpi1(a,b))
                            elif math == 2:
                                 a = float(input(" 명목 이자율을 입력하세요.>>"))
                                 b = float(input(" 인플레이션율을 입력하세요. >> "))
                                 print("실질 이자율의 값은 %.2f 입니다." %cpi2(a,b))
                            elif math == 3:
                                 break
                            else:
                                 print("다시 번호를 입력해주세요.")
                                    

                    elif unit == 26:
                        print ("26장 - 저축,투자와 금융제도")
                        while True:
                            print (" 1. 민간저축 계산하기 \n 2. 정부저축 구하기 \n 3. 이전으로 돌아가기")
                            print ("원하는 계산의 번호를 입력해주세요.")
                            math = int(input(">>"))
                            if math == 1:
                                 a = float(input("가계소득을 입력하세요.>>"))
                                 b = float(input("세금을 입력 하세요.>>"))
                                 c = float(input("소비를 입력하세요.>>"))
                                 print ("민간저축 값은 %.2f 입니다." %save1(a,b,c))
                            elif math == 2:
                                 a = float(input(" 조세 수입을 입력하세요.>>"))
                                 b = float(input(" 정부지출을 입력하세요. >> "))
                                 print("정부저축의 값은 %.2f 입니다." %save2(a,b))
                            elif math == 3:
                                 break
                            else:
                                 print("다시 번호를 입력해주세요.")

                                    
                    elif unit == 27:
                        print ("27장 - 재무이론의 기초")
                        while True:
                            print (" 1. 현재금액의 미래 가치 구하기 \n 2. 미래금액의 현재 가치 구하기 \n 3. 이전으로 돌아가기")
                            print ("원하는 계산의 번호를 입력해주세요.")
                            math = int(input(">>"))
                            if math == 1:
                                 a = float(input("이자율을 입력하세요.>>"))
                                 b = float(input("몇년 뒤의 미래가치를 계산할지 입력하세요(ex. 2년후 -> 2)>>"))
                                 c = int(input("현재가치를 입력하세요.>>"))
                                 print ("현재금액의 %d 년 후 미래가치 값은 %.2f 입니다." %(b,future1(a,b,c)))
                            elif math == 2:
                                 a = float(input("미래가치를 입력하세요..>>"))
                                 b = float(input("이자율을 입력하세요 >> "))
                                 c = int(input("몇 년 후의 금액인지 입력하세요.(ex. 2년후 -> 2)>>"))
                                 print("%d 년 후 미래금액의 현재가치는 의 값은 %.2f 입니다." %(b,future2(a,b,c)))
                            elif math == 3:
                                 break
                            else:
                                 print("다시 번호를 입력해주세요.")
                                 

                        

                    elif unit == 28:
                        print ("28장 - 실업")
                        while True:
                            print(" 1. 실업률 구하기 /n 2. 경제활동 참가율 구하기 \n 3. 이전으로 돌아가기")
                            print ("원하는 계산의 번호를 입력해주세요.")
                            math = int(input(">>"))
                            if math == 1:
                                 a = float(input("취업자의 수를 입력하세요>>"))
                                 b = float(input("실업자의 수를 입력하세요>>"))
                                 print ("실업률은 %.2f 입니다." %unemploy1(a,b))
                            elif math ==2:
                                 a = float(input(" 취업자의 수를 입력하세요.>>"))
                                 b = float(input("실업자의 수를 입력하세요. >> "))
                                 c = float(input("성인 인구수를 입력하세요. >>"))
                                 print("경제활동 참가율은 %.2f 입니다." %unemploy2(a,b,c))
                            elif math == 3:
                                 break
                            else:
                                 print("다시 번호를 입력해주세요.")
                                 
                    elif unit == 4:
                        break

                    else:
                        print("단원을 다시 입력해주세요")

            elif sub == 2:   #경제통계의 이해를 선택 했을 경우
                while True:
                    print("필요한 계산 식의 번호를 입력해주세요. >>")
                    print(" 1. 모평균 구하기 \n 2. 모분산 구하기 \n 3. 모표준편차 구하기 \n 4. 이전으로 돌아가기 ")
                    math = int(input(">"))
                    
                    if math == 1:
                        print("이산확률변수에서 모평균을 구합니다.")
                        num_list= list(map(int, input("표본을 입력하세요.(스페이스로 표본 구분)>>").split()))
                        np.mean (num_list)
                        print("모평균은 %.2f 입니다." % np.mean(num_list))

                    elif math == 2:
                        print ("이산확률변수에서 모분산를 구합니다.")
                        num_list= list(map(int, input("표본을 입력하세요.(스페이스로 표본 구분)>>").split()))
                        np.var(num_list)
                        print("모분산은 %.2f 입니다." % np.var(num_list))

                    elif math == 3:
                        print ("이산확률변수에서 모표준편차를 구합니다.")
                        num_list= list(map(int, input("표본을 입력하세요.(스페이스로 표본 구분)>>").split()))
                        np.std(num_list)
                        print("모표준편차는 %.2f입니다." %np.std(num_list))
                    
                    elif math == 4:
                        break

                    else:
                        print("다시 입력해주세요.")



            elif sub == 3:
                break

            else:
                print("다시 번호를 입력해주세요.:")

    elif menu == 3:  #공부 시간 계산을 선택했을 경우 
        print ("공부 시간 계산기 입니다.")
        print ("공부를 시작한 시간을 입력하세요.")
        cur_time = dt.datetime.today()
        study_time = cur_time.replace(hour= int(input("시간을 입력하세요.>>")), minute=int(input("분을 입력하세요>>")))  #공부를 시작한 시간을 입력 받는다
        diffsec = (cur_time-study_time).seconds //3600     #현재 시간을 받아서 입력 받은 시간과 뺀다. 
        print(f"오늘의 공부시간은 %.2f 시간 입니다." %diffsec)  
  
    elif menu == 4:  #프로그램 종료를 선택했을 경우 
        print("프로그램을 종료합니다.")
        break

    else:
        print("번호를 다시 입력해주세요.")


        



