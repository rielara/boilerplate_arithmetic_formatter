
def arithmetic_arranger(problems, ariA = False):
  # Returns error message if number of problems bigger than 5
  if len(problems) > 5:
      return('Error: Too many problems.')

  line_1 = ''
  line_2 = ''
  line_3 = ''
  line_4 = ''


  for problem in problems:
    problem = problem.split()
    firstNum = problem[0]
    secondNum = problem[2]
    operator = problem[1]


    if not firstNum.isdigit() or not secondNum.isdigit():
      return('Error: Numbers must only contain digits.') 

    if len(firstNum) > 4 or len(secondNum) > 4:
      return('Error: Numbers cannot be more than four digits.')

    if '*' in problem or '/' in problem:
      return("Error: Operator must be '+' or '-'.")

    if operator == '+' :
      sum = int(firstNum) + int(secondNum)
    else : 
      sum = int(firstNum) - int(secondNum)

      
    line_length = max(len(firstNum), len(secondNum)) + 2 
    line_1 += str(firstNum).rjust(line_length) + '    '
    line_2 += str(operator + secondNum.rjust(line_length-1)) + '    ' 
    line_3 += str("-" * line_length) + '    '
    line_4 += str(sum).rjust(line_length) + '    '
    

  if ariA == True:  
    arranged_numbers = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip() + "\n" + line_4.rstrip()
  else: 
    arranged_numbers = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip()

  
 
  return arranged_numbers

