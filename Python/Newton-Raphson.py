from sympy import Derivative, Symbol

#written by Ricardo C. G. Mendonça Filho -> https://github.com/mendoncas

#store the function you want to work with on a string, like shown below
def function():
    return ("(x)**2+(x)")


#returns the derivative of a function 'f'
def derivative(f):
    x = Symbol('x')
    derivative = Derivative(f, x)
    return derivative.doit()


#converts a function 'f' to a string and solves it for a given 'x' value
def solve(f, x):
    f = '{}'.format(f)
    f = f.replace('x', '{}'.format(x))
    return eval(f)


#returns the root of a given function 'f', using its derivative 'der' and an initial 'guess'
def newton_raphson(f, der, guess):
    if(abs(0-solve(f, guess))>0.0):
        guess = guess - (solve(f, guess)/solve(der, guess)) 
        return newton_raphson(f, der, guess);
    
    else:
        return guess;


func   = function()
deriv  = derivative(function())
output = newton_raphson(func, deriv, -1)

print('function: {}'.format(func))
print('derivative: {}'.format(deriv))
print('root: {}'.format(output))
