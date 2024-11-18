import tkinter as tk # GUI 라이브러리

"""
pyinstaller --onefile --windowed soongong.py
명령어로 exe파일을 만들 수 있음
"""

class StudyTimerApp:
    def __init__(self, root):
        self.root = root # 최상위 윈도우
        self.root.title("soongong") # 윈도우 이름 설정
        self.time = 0 # 타이머 시간 저장(초)
        self.running = False # 타이머 실행 여부

        # 타이머 표시
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48)) # 타이머 시간이 표시될 라벨
        self.label.pack(pady=20) # 라벨을 윈도우에 추가, 상하 패딩 20

        # 시작/일시정지 버튼
        self.start_button = tk.Button(root, text="Start", command=self.start_pause) # 클릭 시 self.start_pause 메서드 호출
        self.start_button.pack(side="left", padx=10), # 버튼을 윈도우에 추가, 좌측 정렬, 좌우패딩 10

        # 종료 버튼
        self.reset_button = tk.Button(root, text="reset", command=self.reset)
        self.reset_button.pack(side="right", padx=10)

    # 타이머 시간 업데이트
    def update_timer(self):
        if self.running: # init에 있는 running에 따라 타이머 작동/중지
            self.time += 1 # 시간 1초 증가
            minutes, seconds = divmod(self.time, 60) # self.time에서 초를 받아와서 60으로 나눠 몫과 나머지 반환
            hours, minutes = divmod(minutes, 60) # minutes을 다시 받아와서 60으로 나눠 몫과 나머지 반환
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}") # self.label.config 메서드를 사용하여 self.label의 텍스트 업데이트, 두자릿수로 분, 초 표시
            self.root.after(1000, self.update_timer) # 1000밀리초마다 update_timer를 호출하여 타이머를 업데이트함

    def start_pause(self):
        if self.running: # 타이머가 실행중이었던 경우
            self.running = False # 실행중지
            self.start_button.config(text="Start") # 버튼 텍스트 변경
        else:
            self.running = True
            self.start_button.config(text="Pause")
            self.root.after(1000, self.update_timer)

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")
        self.start_button.config(text="Start")

if __name__ == "__main__":
    root = tk.Tk() # 최상위 윈도우 생성
    app = StudyTimerApp(root)
    root.mainloop() # GUI 실행





