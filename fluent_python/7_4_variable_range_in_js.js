// 파이썬과 js 변수 범위 비교... 이게 왜 이런 결과가 나오나...?? --> 아래 링크 참조
// http://chanlee.github.io/2013/12/10/javascript-variable-scope-and-hoisting/

function k1(){
    console.log(a);
    a = 3;
    console.log(a);
    // 1) a라는 이름의 변수가 전역 콘텍스트에 존재할 경우
    // 1
    // 3
    // 2) a라는 이름의 변수가 전역 콘텍스트에 존재하지 않는 경우
    // Uncaught ReferenceError: a is not defined
    return "return k1()"
}

function k2(){
    // 파이썬에서는 이 위치에서 에러가 찍힘. UnboundLocalError: local variable 'a' referenced before assignment
    console.log("11111", a);
    var a = 5;
    console.log("22222", a);
    // 여기서 에러가 나지 않고, undefined가 찍히는 이유는 호이스팅으로 인해 위 코드가 아래와 같이 바뀌기 때문.
    // var a;
    // console.log("11111", a);
    // a = 5;
    // console.log("22222", a);
    return "return k2()"
}

// 예시1
var a = 1;

console.log(a)  // 1

console.log(k1())
// 3
// 5

console.log(a)  // 3

console.log(k2())
// 11111 undefined
// 22222 5

console.log(a) // 3