
// 핀 번호 리스트
const pinNumbers = [
    "5249-5790-4334-0701-20210701",
    "5249-5790-4334-0701-20210701",
    "5249-5790-4334-0701-20210701"
];

// "더 충전하기" 버튼 클릭
const addButton = document.getElementById("addTen");
if (addButton) {
    addButton.click();
}

// 최대 10개의 핀 번호만 입력하도록 제한
const maxPins = Math.min(pinNumbers.length, 10);

// 핀 번호를 입력 필드에 설정
for (let index = 0; index < maxPins; index++) {
    const pinNumber = pinNumbers[index];
    const actualIndex = index + 1;  // 인덱스를 1부터 시작하도록 조정
    const pinParts = pinNumber.split('-');

    // 핀 번호의 각 부분을 입력
    document.getElementById(`pinNo1_${actualIndex}`).value = pinParts[0];
    document.getElementById(`pinNo2_${actualIndex}`).value = pinParts[1];
    document.getElementById(`pinNo3_${actualIndex}`).value = pinParts[2];
    document.getElementById(`pinNo4_${actualIndex}`).value = pinParts[3];
    document.getElementById(`issuedDate_${actualIndex}`).value = pinParts[4];
}
