var isPalindrome = function (x) {
  if (x < 0) return false;

  let original = x;
  let reverseno = 0;

  while (x > 0) {
    let last = x % 10;
    x = Math.floor(x / 10);
    reverseno = reverseno * 10 + last;
  }

  return reverseno === original;
};
