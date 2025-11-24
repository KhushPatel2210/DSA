//print n time your name using recursion

function printName(i, n) {
  if (i > n) {
    return;
  }
  console.log("khush");
  printName(i + 1, 5);
}

printName(1, 5);

//time complexity is O(n)
//space complexity is O(n) due to recursion stack
