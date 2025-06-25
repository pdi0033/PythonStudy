let fs = require('fs');
// 비동기 - 함수가 시작을 하자마자 바로 리턴을 한다.

fs.readFile('./동기식1.js', 'utf-8', function(error, data) {
    // 첫번째 매개변수는 혹시나 파일을 못 찾거나, 파일을 읽으려고 했는데 권한이 없거나 등 오류가 전달됨
    // 두번째 매개변수는 읽어온 파일 내용이다.
    console.log(data);
});
console.log('completed');


