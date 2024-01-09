# script_generator
Youtube 영상 제작을 위한 AI 스크립트 생성기

README 계속 수정 중..

# 📽️ Demo

![image](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/4e7249e6-9e6e-448e-aea8-e1f46c7cefe3)



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
  - [Project Workflow]()
  
[2. 코드 설명](#2-코드-설명) <br>
  - [Flask](#Flask)
  - [LangChain](#LangChain)


[4. 결과](#4-결과) <br>

[5. 프로젝트 회고](#5-프로젝트-회고) <br>
  - [어려웠던 점](#어려웠던-점)
  - [배운 점](#배운-점)


<br>

# 1. 프로젝트 소개

Youtube 영상 제작을 위한 AI 스크립트 생성기
: AI 영상 제작 도우미 서비스의 mini project
- 본업(유튜버), 마케팅(홍보), 부업(부수입) 다양한 목적으로 영상 제작에 대한 니즈가 있음 
- 최근 다양한 생성형 AI 툴을 활용해서 예전 보다 훨씬 간단하게 영상을 제작할 수 있음
  - → but 대부분의 서비스가 1분 미만의 숏츠 영상에 최적화 되어 있거나, 각각의 서비스별로 부족한 부분 존재

## 목표

![what we want1](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/b3472037-c162-40e7-92fb-4ebc0c98647a)

![what we want2](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/40e7b69b-4a11-46e2-ae89-7dda8d16884e)

![what we want3](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/dfc9830d-62d8-470b-abe2-69386fee56e7)



# 2. 코드 설명

## Flask

## LangChain

![LangChain](https://github.com/sesac-google-ai-1st/script_generator/assets/97524127/f33f8319-637b-46f5-843d-a55ebc95b8f9)
