"""
week3_quiz.py
"""
def eval_bool(p, q): 
    """
    Takes boolean p and q and returns the values
    """
    answer = not(p or not q)
    return answer
    
print("answer 1:", eval_bool(True, True))
print("answer 2:", eval_bool(True, False))
print("answer 3:", eval_bool(False, True))
print("answer 4:", eval_bool(False, False))

bool1 = True
bool2 = False
answer2 = not not bool1
print("First answer", answer2)
answer2 = (True == False)
print("First answer", answer2)
answer2 = (bool2 == (not bool1))
print("First answer", answer2)
answer2 = (not bool2)
print("First answer", answer2)

num1 = 10
num2 = 10
if num1 >= num2: 
    print("correct answer1")
if not(num1 < num2): 
    print("Correct answer2")
if not(num1 <= num2): 
    print("correct answer3")
if num2 < num1: 
    print("correct answer4")
if (num1 > num1) and (num1 != num2):
    print("correct answer5")


if num1 >= num2: 
    print("correct answera")
elif not(num1 < num2): 
    print("Correct answerb")
elif not(num1 <= num2): 
    print("correct answerc")
elif num2 < num1: 
    print("correct answerd")
elif (num1 > num1) and (num1 != num2):
    print("correct answere")
    
def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """
    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True
        
print("evaluated", nand(True, True))

def f(number): 
    if number % 2 == 0: 
        print("even number")
        new_number = int(number / 2)
    else:
        print("odd number")
        new_number = int(3*number + 1)
    return new_number

print("collatz", f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))) 

        
    