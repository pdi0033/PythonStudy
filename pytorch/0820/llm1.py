# 1. 라이브러리 설치 (처음 한 번만 실행)
# pip install transformers torch
# pip install --upgrade transformers

# 2. 필요한 모듈 임포트
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# --- IMPORTANT ---
# export HF_TOKEN="hf_your_token_here"  (Linux/macOS)
# set HF_TOKEN="hf_your_token_here"    (Windows CMD)

# huggingface_token을 직접 코드에 입력하거나, 환경 변수에서 가져올 수 있습니다.
# 코드에 직접 입력하는 경우 보안에 유의하세요.
# jwt 방식
# 아래의 토큰은 허깅 페이스 access token이다. 위험하니 push할 때는 지우자.
# hf_token = "asdf"  # read d이상으로 토큰을 만들자
#hf_token = os.environ.get("HF_TOKEN")

if not hf_token:
    print("오류: 환경 변수 'HF_TOKEN'이 설정되지 않았습니다.")
    print("터미널에서 'export HF_TOKEN=\"YOUR_TOKEN\"' (Linux/macOS) 또는 'set HF_TOKEN=\"YOUR_TOKEN\"' (Windows)를 실행하세요.")
    exit()
"""
gemma와 같은 일부 모델은 사용하기 전에 Hugging Face 계정에서 접근 권한을 받아야 합니다. 이 코드는 토큰을 환경 변수(HF_TOKEN)에서 불러오거나, 코드 내에 직접 입력(hf_FKSbHM...)하도록 설정되어 있습니다.

보안상의 이유로 토큰을 코드에 직접 넣는 것은 권장되지 않습니다. 대신, 터미널에 export나 set 명령어를 사용하여 환경 변수로 설정하는 것이 더 안전합니다.

if not hf_token:은 토큰이 제대로 설정되었는지 확인하고, 설정되지 않았다면 사용자에게 안내 메시지를 출력하고 프로그램을 종료합니다.
"""
# 모델 이름 설정
model_name = "google/gemma-2b"  # 7기가바이트

print(f"--- CPU로 LLM 불러오기: {model_name} ---")

# CPU에서 사용할 장치 설정
device = "cpu"
print(f"사용 장치: {device}")

try:
    print("토크나이저를 로드하는 중...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)

    print("모델을 로드하는 중...")
    # BitsAndBytesConfig를 제거하고, device_map을 'auto' 대신 'cpu'로 설정합니다.
    # 또한, torch.dtype을 설정하여 메모리 사용량을 줄일 수 있습니다 (선택 사항).
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map=device,
        token=hf_token,
        torch_dtype=torch.bfloat16 # CPU에서도 지원되는 데이터 타입
    )

    print("\n모델 로딩 완료!")

    """
    model_name = "google/gemma-2b": 사용할 모델의 이름을 Hugging Face Hub에서 가져와서 변수에 저장합니다.

    device = "cpu": 이 부분이 가장 중요한 변경점입니다. 이 줄은 모델을 CPU에서 실행하도록 명시적으로 설정합니다. 이전 GPU 버전에서는 torch.cuda.is_available()을 사용해 GPU 존재 여부를 확인했지만, 이 코드에서는 오직 CPU만 사용합니다.

    AutoTokenizer.from_pretrained(...): 모델 이름과 토큰을 사용하여 토크나이저를 로드합니다. 토크나이저는 인간의 언어(텍스트)를 모델이 이해할 수 있는 숫자(토큰 ID)로 변환하는 역할을 합니다.

    AutoModelForCausalLM.from_pretrained(...): 모델의 가중치를 불러옵니다.

    device_map=device: 모델의 모든 가중치를 device 변수("cpu")로 지정된 장치에 로드하라는 명령입니다.

    token=hf_token: 모델을 다운로드하고 접근하기 위해 필요한 토큰을 전달합니다.

    torch_dtype=torch.bfloat16: 모델의 가중치를 bfloat16이라는 데이터 타입으로 로드합니다. bfloat16은 일반적인 float32보다 메모리 사용량이 절반이므로, RAM 사용량을 크게 줄여줍니다. 이는 GPU 없이 큰 모델을 CPU에서 실행할 때 매우 유용합니다.

    4. 텍스트 생성
    """
    # 텍스트 생성 프롬프트
    prompt_text = "대한민국의 수도는 어디야?"
    # prompt_text = input("질문을 하세요")
   
    print(f"\n입력 프롬프트: {prompt_text}")

    # 토크나이징 및 장치 설정
    input_ids = tokenizer(prompt_text, return_tensors="pt").to(device)

    # 텍스트 생성
    with torch.no_grad():
        output = model.generate(
            **input_ids,
            max_new_tokens=50, # 최대 50개의 새로운 토큰 생성
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

    # 생성된 텍스트 디코딩
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    print("\n생성된 답변:")
    print(decoded_output)

except Exception as e:
    print(f"오류가 발생했습니다: {e}")
    print("\n모델 이름, 라이브러리 설치 상태, 그리고 허깅페이스 토큰을 다시 확인해 주세요.")