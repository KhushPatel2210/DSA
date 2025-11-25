// Count the number of digits in a given integer n

class Solution {
  countDigit(n) {
    let i = 0;
    while (n > 0) {
      n = Math.floor(n / 10);
      i++;
    }
    return i;
  }
}

//do not use % operator or convert to string
// we can use the logarithm base 10 to determine the number of digits
class Solution {
  countDigit(n) {
    return Math.floor(Math.log10(n) + 1);
  }
}

// for value 7789 the log10(7789) = 3.8915
// floor(3.8915 + 1) = floor(4.8915) = 4
// thus there are 4 digits in 7789

// time complexity: o(log n) base 10
// space complexity: o(1)

// if we divide input number with 10 then base of tc is 10 if we divide with 2 then base is 2 if we divide with 3 then base is 3 and so on. but in all cases time complexity is logarithmic.
