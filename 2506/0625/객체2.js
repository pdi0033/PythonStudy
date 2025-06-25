let person = {
    name:'홍길동',
    age:23,
    // 키에 값만 저장이 아니라 함수도 저장할 수 있다.
    display:function() {
        console.log(`${this.name} ${this.age}`);
        // this: 객체 자신
        // this 생략 불가
    },
    setValue:function(name, age) {
        this.name = name;
        this.age = age;
    }
    // 화살표함수는 this를 접근할 수 없다. 그래서 람다는 불가능, 함수표현식만 가능하다.
};

person.setValue('임꺽정', 33);
person.display();




