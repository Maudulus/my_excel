This method, evaluate, is a spreadsheet calculator, which can perform the specified math functions contained in the cells and compute the final cell values.

The following code is an example of the spreadsheets that this method take in, and how you would print the final, computed spreadsheet to the console.

mini_spreadsheet = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 + B2"],
  ["A1", "=B1+A1", "C2 + B3", "= A3 + B3 + C3"]
]

mini_spreadsheet2 = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 * B2"],
  ["A1", "=B1+A1", "C2 + B3", "= A3 + B3 + C3"]
]

mini_spreadsheet3 = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 * B2"],
  ["A1", "=B1*A1", "C2 + B3", "= A3 * B3 * C3"]
]
print evaluate(mini_spreadsheet)
print evaluate(mini_spreadsheet2)
print evaluate(mini_spreadsheet3)

