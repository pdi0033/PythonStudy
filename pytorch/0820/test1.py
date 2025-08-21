from transformers import pipeline

# 텍스트 생성 모델 로드
classifier = pipeline("sentiment-analysis")
result = classifier("Hugging Face는 정말 멋진 라이브러리입니다!")
print(result)