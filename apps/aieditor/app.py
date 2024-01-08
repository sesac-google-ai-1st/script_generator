from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def maintest():
    subtopics = ["소주제 1", "소주제 2", "소주제 3", "소주제 4", "소주제 5", "소주제 6", "소주제 7", "소주제 8", "소주제 9", "소주제 10"]
    
    # 사용자 입력을 저장할 변수 초기화
    user_input = ''
    
    # 소주제 표시 여부를 결정하는 플래그
    display_subtopics = False
    
    # 체크박스 상태를 저장하는 딕셔너리
    checkbox_states = {}
    
    # 체크박스로 선택된 스크립트를 저장할 리스트
    selected_scripts = []

    # POST 요청 처리
    if request.method == 'POST':
        # "소주제 표시" 버튼이 눌렸는지 확인
        if 'button1' in request.form:
            user_input = request.form.get('user_input')
            display_subtopics = True if user_input.strip() else False

        # "스크립트 생성" 버튼이 눌린 경우
        if 'button2' in request.form:
            # 선택된 소주제에 대한 스크립트 생성
            display_subtopics = True
            user_input = request.form.get('user_input')
            selected_scripts = [f"{subtopics[i-1]}와 관련된 스크립트" for i in range(1, 11) if request.form.get(f'subtopic{i}')]

        # 체크박스 상태를 업데이트
        checkbox_states = {f'subtopic{i}': 'checked' if request.form.get(f'subtopic{i}') else '' for i in range(1, 11)}

    # 템플릿 렌더링. 변수들을 템플릿으로 전달
    return render_template('maintest.html', subtopics=subtopics, user_input=user_input, display_subtopics=display_subtopics, checkbox_states=checkbox_states, selected_scripts=selected_scripts)



if __name__ == '__main__':
    app.run(debug=True)
