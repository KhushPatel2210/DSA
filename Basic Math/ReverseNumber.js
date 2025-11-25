var reverse = function (x) {
  let reverseno = 0;

  // sign used to store whether the number is negative or positive
  let sign = x < 0 ? -1 : 1;

  //math.abs remove the negative sign
  x = Math.abs(x);

  while (x > 0) {
    // getting last digit
    let last = x % 10;
    // removing last digit from x
    x = Math.floor(x / 10); // FIXED
    // appending last digit to reverseno
    reverseno = reverseno * 10 + last;
  }
  // returning the reversed number with its sign
  return sign * reverseno;
};
