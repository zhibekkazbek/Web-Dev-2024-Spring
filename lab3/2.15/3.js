function min(a, b) {
  if (a < b) {
    return a;
  } else {
    return b;
  }
}

function min(a, b) {
  return a < b ? a : b;
}

min(2, 5) == 2
min(3, -1) == -1
min(1, 1) == 1