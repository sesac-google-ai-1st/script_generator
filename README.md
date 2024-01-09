# script_generator

#### Youtube 영상 제작을 위한 AI 스크립트 생성기


# 📽️ Demo

![script generator](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/3d0448cc-7b7f-4502-9d65-f42b49c32b9f)


# 🧑‍💻 How to run

```python
!git clone https://github.com/sesac-google-ai-1st/script_generator.git
%cd script_generator
!pip install -r requirements.txt

# 환경변수 설정: openAI, Google의 API key 설정 
# Linux/Mac
!export OPENAI_API_KEY=YOUR_OPENAI_API_KEY
!export GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
# Windows
!set OPENAI_API_KEY=YOUR_OPENAI_API_KEY
!set GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

!flask run
```


<br>

# 📃 Contents

[1. 프로젝트 소개](#1-프로젝트-소개) <br>
  - [목표](#목표)
  - [수행 기간 및 팀원](#수행-기간-및-팀원)
  - [repo structure](#repo-structure)
  - [Project Workflow](#project-workflow)
  
[2. 상세 task](#2-상세-task) <br>
  - [LLM 모델 테스트](#llm-모델-테스트)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [LangChain](#langchain)


[3. 결과](#3-결과) <br>

[4. 프로젝트 회고](#4-프로젝트-회고) <br>
  - [어려웠던 점](#어려웠던-점)
  - [배운 점](#배운-점)


<br>

# 1. 프로젝트 소개

### Youtube 영상 제작을 위한 AI 스크립트 생성기 
#### : AI 영상 제작 도우미 서비스의 sub project
- 본업(유튜버), 마케팅(홍보), 부업(부수입) 등 다양한 목적으로 영상 제작에 대한 니즈가 있음 
- 최근 다양한 생성형 AI 툴을 활용해서 예전보다 훨씬 간단하게 영상을 제작할 수 있음 <br>
 → but, 대부분의 서비스가 1분 미만의 숏츠 영상에 최적화 되어 있거나, 각각의 서비스별로 부족한 부분 존재
<br>

- **스크립트 작성 단계에서의 Pain Point** 😠 (by 현 유튜버)
   - 1번의 프롬프트로 원하는 분량의 스크립트 작성이 어려움
   - 스크립트 분량 늘어날수록 내용의 짜임새가 부족
   - 채팅 방식이라서 이전에 생성한 내용 찾을 때 불편함

## 목표

#### 보다 간편하게 최종 영상 스크립트를 작성 할 수 있는 웹 서비스

![what we want1](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/b3472037-c162-40e7-92fb-4ebc0c98647a)

![what we want2](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/40e7b69b-4a11-46e2-ae89-7dda8d16884e)

![what we want3](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/dfc9830d-62d8-470b-abe2-69386fee56e7)

## 수행 기간 및 팀원

- 🗓️ 수행 기간 : 2023.12.29 ~ 2024.01.05 (5일)

- 👥 팀원 (4명)<br>

    |남경수|박영현|이철현|최지민|
    |:-:|:-:|:-:|:-:|
    |<img src='https://avatars.githubusercontent.com/u/147117427?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/72022988?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/126049851?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/97524127?v=4' height=80 width=80px></img>|
    |[Github](https://github.com/namchaos4809)|[Github](https://github.com/yhp2205)|[Github](https://github.com/collin421)|[Github](https://github.com/timmyeos)|

## repo structure

```
.
├── apps
│   └── aieditor
│       ├── app.py
│       ├── func
│       │   └── chain.py
│       ├── static
│       │   ├── css
│       │   │   └── style.css
│       │   ├── images
│       │   │   ├── 1.jpg
│       │   │   ├── 2.jfif
│       │   │   ├── 3.jfif
│       │   │   ├── 4.png
│       │   │   ├── arrow1.png
│       │   │   ├── arrow2.png
│       │   │   └── prom.png
│       │   └── js
│       │       └── script.js
│       └── templates
│           └── maintest.html
├── README.md
└── requirements.txt
```

## Project Workflow

메인 주제 입력 → 자동으로 서브 주제 생성 → 서브 주제 선택 → 최종 스크립트 생성 및 출력

# 2. 상세 task

## LLM 모델 테스트

- 목표
  - 원하는 내용/형태/충분한 분량이 생성 가능한 LLM 모델 선정
  - LLM 모델에 맞는 최적 프롬프트 도출
- 테스트 대상 모델
  -  gemini pro
  -  bard(palm2)
  -  gpt-3.5-turbo-1106 (이전 모델의 경우 답변 생성 시, 여러 요청 사항을 모두 반영 못함(영어/한글 모두))
  -  gpt 4
- 테스트 항목 
  - 영어 / 한글 프롬프트 별로 충분한 답변을, 원하는 형태로 생성해주는가

- 테스트 결과
  - 모든 모델들은 **영어 프롬프트** 입력 시, 여러 요청 사항을 반영하여 답변을 줌(원하는 형태로 답변)  👍
  - 일부 모델 **한글로 프롬프트** 입력 시, 여러 요청사항 반영 X 👎

-  선정한 모델
    - gpt-3.5-turbo-1106
    - gpt 4
    - gemini pro
- 최종 프롬프트
    <details>
      <summary>GPT 프롬프트 ( 버전 : gpt-3.5-turbo-1106 / gpt 4)</summary>

      I am planning to create a YouTube video with the main and detailed topics below.
      Write a video script
      First, please write only the script for detailed topic number 1.
      
      Video main topic
      : Interesting Behavior of Ancient Creatures: Interpretation of Unique Characteristics and Behaviors
      
      video details topic
      
      1. The struggle to live a long life
      2. Lightening the heavy body: The flight skills of ancient creatures
      3. From land to water: aquatic migration strategies of ancient organisms
      4. Surprising behavior of vegetarian dinosaurs: social structure and cooperation
      5. Scary Crowds in Fossils: Group Behavior in Ancient Creatures
      6. Come on! Master Hunter: Hunting Strategies of Ancient Creatures
      
      Writing guide
      
      1. Don't say hello to the channel
      2. Don’t distinguish between scenes (don’t even write scene distinction phrases)
      3. I also distinguish between intro and body text (don’t even write the text).
      4. Just write the script
      5. Please write as long as possible
    </details>
    <details>
      <summary>Gemini 프롬프트</summary>
      
      1. The difficult terminology is written as follows: \
      - "Aseptic reproduction" => "The ability to create offspring on one's own without any other individual" \
      2. Long and detailed description. \
      3. According to Tone and Manner, a script for knowledge transfer is written mainly by stories. \
      4. Focusing on stories and narratives, the contents are richly written, including historical backgrounds, events, etc. \
      5. Channel introduction and greetings are omitted at the start, and greetings are omitted at the end. \
      6. Exclude narrator and commentator phrases. \
      7. Do not write " and () and - and special characters. \
      8. Do not distinguish between scenes. \
      9. I don't even write anything that describes the scene. \
      10. Do not separate chapters. \
      11. no : do not ask questions \
      12. Write a paragraph by sub-title. \
      13. Run a line change after each sentence.    \
      14. Even clauses or examples are not presented as a list, but are written in a tightrope.  
    </details>

[LLM 모델 테스트 정리 문서](https://docs.google.com/document/d/1Yv2JaJCO3OmEA-WzO4s8CPJEp5NpK2eQoaiPQ9AAFpA/edit?usp=sharing)

## Frontend
→ UI 기획

→ HTML 코딩
## Backend 

→ Flask로 구현
## LangChain

→ 스크립트 생성 랭체인 구축

![LangChain](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/f33f8319-637b-46f5-843d-a55ebc95b8f9)
