//simple recursion
//function calls it self until a condition is met

//here there is no condition so this is called as a infinite recursion
function r() {
  console.log("hello");
  r();
}

r();

//in this type f recursion there is stack in memory to store the data and when there is no specific condition it become the infinite recursion

// this will give you a stack overflow error after some time because the memory stack will be full segmentation fault

// to avoid this we need to put a condition to stop the recursion at some point this is called base condition

let a = 0;
function r() {
  if (a == 4) {
    return;
  } else {
    console.log(a);
    a++;
    r();
  }
}

r();

// here the function will call itself until a becomes 4 and then it will stop calling itself
// this is how we can avoid infinite recursion and stack overflow error

//recursion tree means visual representation of how the function calls itself

// for example in the above example the recursion tree will look like this
//                   r(0)
//                 /
//              r(1)
//            /
//         r(2)
//        /
//     r(3)
//    /
// r(4) -> base condition met return
