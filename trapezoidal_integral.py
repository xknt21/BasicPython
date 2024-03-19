from math import sin
import math

def trapezoidal_integral(f, a = 0, b = 1, n = 100):

    h = (b - a) / n
    S = 0

    for i in range(1, n + 1):
        S += (h / 2) * (f(a + (i -1) * h) + f(a + i * h))
    return S

def question2_function(x):
    return 4/(1+x**2)

def question3_function(x):
    return((math.pi)**(1/2)) * (math.exp(-x**2))

question1 = trapezoidal_integral(sin, 0, (1/2)*(math.pi), 50)
question2 = trapezoidal_integral(question2_function, 0, 1, 100)
question3 = trapezoidal_integral(question3_function, -100, 100,100)

answer = [question1, question2, question3]
print(answer)

#他の人のコードから学んだprintの仕方(一部自分用に改変)
# for i in range(3):
#     print(関数のquestion{i+1}における積分値は、{answer[i]}です。')