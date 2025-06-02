
import pygame
import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

questions_data = [
    ("Какая самая большая по площади страна в мире?",
     ["Канада", "Россия", "Китай"], 1),
    ("На каком континенте находится пустыня Сахара?",
     ["Африка", "Азия", "Австралия"], 0),
    ("Какая река является самой длинной в мире?",
     ["Амазонка", "Нил", "Миссисипи"], 1),
    ("В какой стране находится город Токио?",
     ["Китай", "Южная Корея", "Япония"], 2),
    ("Какая гора считается самой высокой в мире?",
     ["Эверест", "Килиманджаро", "Аконкагуа"], 0)
]

questions = []
for qd in questions_data:
    questions.append(Question(qd[0], qd[1], qd[2]))
random.shuffle(questions) 

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 50
MARGIN = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Урок Географии: Контрольная за 3 класс")
clock = pygame.time.Clock()

def draw_text(surface, size, color, text, x, y):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    rect = label.get_rect(center=(x, y))
    surface.blit(label, rect)

def draw_button(surface, x, y, width, height, text):
    pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)
    draw_text(surface, FONT_SIZE - 4, BLACK, text, x + width // 2, y + height // 2)

def show_question(question):
    global current_question_idx, score, correct_answers
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in range(len(question.options)):
                    x = WIDTH // 2 - BUTTON_WIDTH // 2
                    y = HEIGHT // 2 + i * (BUTTON_HEIGHT + MARGIN)
                    button_rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
                    if button_rect.collidepoint(pos):
                        selected_answer = i
                        if selected_answer == question.correct_answer:
                            score += 1
                            correct_answers[current_question_idx] = True
                        else:
                            correct_answers[current_question_idx] = False
                        return 'next'

        screen.fill(WHITE)
        draw_text(screen, FONT_SIZE + 4 , BLACK, question.question , WIDTH//2 , HEIGHT//4)
        for i , option in enumerate(question.options):
            x= WIDTH//2 - BUTTON_WIDTH//2
            y= HEIGHT//2 + i*(BUTTON_HEIGHT+MARGIN)
            draw_button(screen,x,y,BUTTON_WIDTH,BUTTON_HEIGHT , option )
        pygame.display.update()
        clock.tick(60)

current_question_idx=0
score=0
correct_answers={}

state='question' 
running=True

while running:
    if state=='question':
        result=show_question(questions[current_question_idx])
        if result=='quit':
            break
        elif result=='next':
            current_question_idx+=1
            if current_question_idx>=len(questions):
                state='result'
    
    elif state=='result':
                total_questions = len(questions)
                final_score = f"Ваш результат: {score}/{total_questions}"
                 

                if score >= 5:
                    message = "Молодец!!"
                elif score >= 4:
                    message = "Чуствуешь покалывания."
                elif score >= 3:
                    message = "Это СТЫД."
                else:
                    message = "Иди Учи Уроки."

                screen.fill(WHITE)
                draw_text(screen, FONT_SIZE*2 , BLACK , final_score , WIDTH//2 , HEIGHT//2 - 100)
                draw_text(screen, FONT_SIZE , BLACK , message , WIDTH//2 , HEIGHT//2 + 50)
                pygame.display.update()
                waiting_for_exit=True
                while waiting_for_exit:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT or event.type==pygame.KEYDOWN:
                            waiting_for_exit=False
                            running=False
                            clock.tick(60)
                            pygame.quit()
