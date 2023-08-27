import re
import json

# 문자메시지 저장된 파일 불러오기
filename = "message.txt"

def extract_info(text_block):
    pin_number_match = re.search(r"핀번호:\s*(\d{4}-\d{4}-\d{4}-\d{4})", text_block)
    issue_date_match = re.search(r"발행일자:\s*(\d{8})", text_block)

    if pin_number_match and issue_date_match:
        pin_number = pin_number_match.group(1)
        issue_date = issue_date_match.group(1)
        return f"{pin_number}-{issue_date}"
    else:
        return None

with open(filename, 'r', encoding='utf-8') as file:
    text_block = ""
    results = []

    for line in file:
        text_block += line

        # 발행일자를 찾았을 때 블록이 완성된 것으로 간주
        if "발행일자:" in line:
            result = extract_info(text_block)
            if result:
                results.append(result)
            text_block = ""  # 블록 초기화

# JS 코드 템플릿

js_code_template = """
// 핀 번호 리스트
const pinNumbers = [
{pin_data_entries}
];

// "더 충전하기" 버튼 클릭
const addButton = document.getElementById("addTen");
if (addButton) {{
    addButton.click();
}}

// 최대 10개의 핀 번호만 입력하도록 제한
const maxPins = Math.min(pinNumbers.length, 10);

// 핀 번호를 입력 필드에 설정
for (let index = 0; index < maxPins; index++) {{
    const pinNumber = pinNumbers[index];
    const actualIndex = index + 1;  // 인덱스를 1부터 시작하도록 조정
    const pinParts = pinNumber.split('-');

    // 핀 번호의 각 부분을 입력
    document.getElementById(`pinNo1_${{actualIndex}}`).value = pinParts[0];
    document.getElementById(`pinNo2_${{actualIndex}}`).value = pinParts[1];
    document.getElementById(`pinNo3_${{actualIndex}}`).value = pinParts[2];
    document.getElementById(`pinNo4_${{actualIndex}}`).value = pinParts[3];
    document.getElementById(`issuedDate_${{actualIndex}}`).value = pinParts[4];
}}
"""


# 각 핀 번호를 별도의 줄에 위치하도록 포맷팅
formatted_pin_data = ',\n'.join(['    "{}"'.format(pin) for pin in results])

# JS 코드 생성
js_code = js_code_template.format(pin_data_entries=formatted_pin_data)

# pin_input.js 파일에 저장
with open('pin_input.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_code)