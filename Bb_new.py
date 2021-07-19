import turtle

saru_turtle = turtle.Turtle()
saru_turtle.speed(50)


def square():
    saru_turtle.forward(100)
    saru_turtle.right(90)
    saru_turtle.forward(100)
    saru_turtle.right(90)
    saru_turtle.forward(100)
    saru_turtle.right(90)
    saru_turtle.forward(100)


#square()

elephant_weight = 3000
ant_weight = 0.1

'''if elephant_weight > ant_weight:
    square()
else:
    saru_turtle.forward(200)'''

'''sarath = "happy"
while sarath == "happy":
    saru_turtle.forward(10)'''

for count in range(8):
    square()

