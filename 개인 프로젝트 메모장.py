경로="C:/Users/ingul/OneDrive/바탕 화면/대회/data.txt" #이 프로그램이 실행되기 위해서는 경로가 제대로 지정이 되야 합니다 함께 첨부된 메모장 경로 설정법 한글 파일을 열어서 설정해주세요

def write(x):
    w = open(경로, "w")
    w.write(x)
    w.close()

def read():
    r = open(경로, "r")
    data=r.read()
    r.close()
    print(data)

def plus_jump(x):
    pj = open(경로, "a")
    pj.write("\n")
    pj.write(x)
    pj.close

def plus(x):
    p = open(경로, "a")
    p.write(x)
    p.close

def clean():
    c = open(경로,"w")
    c.write("")
    c.close

while True:
    y=input("메모를 하시기를 원하십니까 기록한걸 확인하시기를 원하십니까?  쓰기를 원하시면 '쓰기'를 읽기를 원하시면 '읽기'를 내용 추가를 원하시면 '추가'를 내용을 삭제하시기를 원하시면 '삭제'를 입력해주세요 그만하고 싶으시면 정지를 입력해주세요.")
    if y=="정지":
        print("이용해 주셔서 감사합니다")
        break

    if y=="쓰기":
        input_value=input("쓰기를 선택하셨습니다 어떤 내용을 쓸지 작성해주세요")
        write(input_value)
        print("쓰기가 완료되었습니다.")

    elif y=="읽기":
        print("읽기를 선택하셨습니다.쓰여진 내용은 다음과 같습니다.")
        read()
        print("읽기가 완료되었습니다")

    elif y=="추가":
        true_false=input("문단을 바꿔서 내용을 추가하고 싶으시면 '바꾸기'를 그대로 내용을 추가만 하고 싶으시면 '그대로'를 입력해 주세요")
        if true_false=="바꾸기":
            input_value=input("문단 바꾸기를 선택하셨습니다 추가하고 싶은 내용을 입력해주세요")
            plus_jump(input_value)
            print("내용 추가가 완료되었습니다")
        elif true_false=="그대로":
            input_value=input("그대로 작성하시기를 선택하셨습니다 추가하고 싶은 내용을 입력해주세요")
            plus(input_value)
            print("내용 추가가 완료 되었습니다")
        else:
            print("잘못된 명령을 입력하셨습니다 처음부터 다시 입력해주세요")
        
            
    elif y=="삭제":
        clean()
        print("삭제가 완료 되었습니다")
    else:
        print("잘못된 명령을 입력하셨습니다 다시 입력해주세요")

            