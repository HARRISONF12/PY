import pgzrun

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box_1 = Rect(0, 0, 495, 165)
answer_box_2 = Rect(0, 0, 495, 165)
answer_box_3 = Rect(0, 0, 495, 165)
answer_box_4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box_1.move_ip(50, 358)
answer_box_2.move_ip(735, 358)
answer_box_3.move_ip(50, 538)
answer_box_4.move_ip(735, 538)
answer_boxes = [answer_box_1, answer_box_2, answer_box_3, answer_box_4]

score = 0
timeleft = 10

q1 = ["What is the capital city of france?", "london", "paris", "tokyo", 2]
q2 = ["What is the capital city of france?", "london", "paris", "tokyo", 1]
q3 = ["What is the capital city of france?", "london", "paris", "tokyo", 3]

questions = [q1, q2, q3]
question = questions.pop(0)


def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer, "sky blue")

for box in answer_boxes:
    screen.draw.filled_rect(box, "orange")

screen.draw.textbox

def draw():
    pass

def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass

pgzrun.go()
