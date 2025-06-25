// let jsondata = "{bad json}";
// 
let jsondata = '{"name":"홍길동", "age":23}';

try {
    // 데이터 송수신할 때 실제로는 json객체를 주고 받는게 아니고 
    // json 형태의 문자열을 주고 받는다.
    // 그래서 파싱을 해줘야 한다.
    let user = JSON.parse(jsondata);
    console.log(user.name);
}
catch(e) {
    console.log("에러");
}

