var reverse = function (x) {
  let reverseno = 0;

  let sign = x < 0 ? -1 : 1;
  x = Math.abs(x);

  while (x > 0) {
    let last = x % 10;
    x = Math.floor(x / 10); // FIXED
    reverseno = reverseno * 10 + last;
  }

  return sign * reverseno;
};
