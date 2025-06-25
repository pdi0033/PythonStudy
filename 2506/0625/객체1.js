let user = {'student-name': '홍길동', kor:90, eng:80, mat:80};
// 키값에 "" '' 사용해도 안 해도 된다.
// student-name     << 이 경우(특수문자)에는 해줘야 한다.
console.log(user.kor, user['student-name']);

// 새로운 필드 추가하기
user['total'] = user.kor + user.eng + user.mat;
user['avg'] = user.total / 3;
console.log(user);

let students = [
    {name:'A', kor:90, eng:80, mat:90},
    {name:'B', kor:70, eng:80, mat:70},
    {name:'C', kor:80, eng:80, mat:60},
    {name:'D', kor:100, eng:100, mat:100},
    {name:'E', kor:90, eng:80, mat:60}
];

students.forEach( s=> {
    s.total = s.kor + s.eng + s.mat
    s.avg = s.total / 3;
});

key = "B";
// 1. B학생 정보를 찾아서 출력하기
students.filter(s=> s.name==key)
        .forEach(item=> console.log(item));
// console.log(result);

// 2. reduce 사용해서 학생들 전체 평균 구하기
avg_all = students.reduce((pre, current)=> {
    if (pre == students[0])
        return pre.avg + current.avg;
    else
        return pre + current.avg;
}) / students.length;
console.log(avg_all);

// initValue = {name:'', kor:0, eng:0, mat:0, avg:0};
// e = students.reduce((item, initValue)=> {
//     item.avg += initValue.avg;
//     return item;   // 누적시킨 객체 반환
// });
// console.log("***", e);

// 3. 총점으로 내림차순해서 출력하기
sorted_s = students.toSorted((a, b)=> b.total - a.total)
sorted_s.forEach(s=> {
    console.log(s.name, s.total);
});

