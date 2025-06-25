let promise = new Promise(function(resolve, reject) {
    sum = 0;
    for(i=1; i<=10; i++) {
        sum += i;
    }

    resolve(sum);   // return 못 쓴다.
    //reject('fail');     // catch구문으로 간다.
});     // 리턴 받는 건 값 55가 아니라 Promise 객체다.

promise.then((response)=> {
    console.log(response);
    response = response*100;
    return response;
})
.then((response)=> {
    console.log('프라미스체인', response);
})
.catch(e=> {
    console.log(e);
})
.finally(()=> {
    console.log('completed');
});

promise.then((response)=> {
console.log('프라미스체인11111111', response);
});

console.log(promise);

// 일반함수 앞에 async를 붙이면 비동기개체로 전환시켜라
async function sigma(limit=10) {
    s=0;
    for(i=1; i<=limit; i++) {
        s+=i;
    }
    return s;
}

console.log("***", sigma(100));
sigma(1000)
.then((r)=> {
    console.log('async', r);
})

// await
async function main() {
    let result = await sigma(100);
    // 버전따라 에러남
    console.log('결과', result);
    console.log('ending ..................');
}
main();

