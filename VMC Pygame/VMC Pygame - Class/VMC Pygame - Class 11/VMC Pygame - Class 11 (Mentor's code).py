import pygame, random
pygame.init()

screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption("TYPING SPEED CALCULATOR")
text_font = pygame.font.Font("freesansbold.ttf", 20)
heading_font = pygame.font.Font("freesansbold.ttf", 40)

def start_game():
    statements = [
        "Please take your dog, Cali, out for a walk – he really needs some exercise!",
        "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
        "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
        "Do you know why all those chemicals are so hazardous to the environment?",
        "You never did tell me how many copper pennies where in that jar; how come?",
        "Max Joykner sneakily drove his car around every corner looking for his dog.",
        "The two boys collected twigs outside, for over an hour, in the freezing cold!",
        "When do you think they will get back from their adventure in Cairo, Egypt?",
        "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
        "We climbed to the top of the mountain in just under two hours; isn’t that great?",
    ]

    def result(inp, statement, time_taken):
        c = 0
        C = 0
        inp_words = inp.split(" ")
        statement_words = statement.split(" ")

        wpm = (len(inp_words)/time_taken) * 60

        for i in range(len(inp_words)):
            for j in range(len(inp_words[i])):
                C += 1
                if inp_words[i][j] == statement_words[i][j]:
                    c += 1
        return((str(c/C*100)[:3]), str(wpm)[:3])

    statement = random.choice(statements)
    inp = ''
    enter = 0
    start = 0

    MainGame = True
    while MainGame:
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(50,100,900,40), 3)
        sentence = text_font.render(statement, True, (255,255,255))
        screen.blit(sentence, (60,110))

        pygame.draw.rect(screen, (0,255,0), pygame.Rect(50,200,900,40), 3)
        if start == 0:
            inp_sentence = text_font.render("(PRESS 1 TO START)", True, (128,128,128))
        else:
            inp_sentence = text_font.render(inp, True, (255,255,225))
        screen.blit(inp_sentence, (60,210))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainGame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start = 1
                    start_time = pygame.time.get_ticks()
                elif event.key == pygame.K_RETURN:
                    enter = 1
                    end_time = pygame.time.get_ticks()
                    accuracy, wpm = result(inp, statement, (end_time-start_time)/1000)
                
                elif event.key == pygame.K_ESCAPE:
                    Display_Page()

                elif event.key == pygame.K_BACKSPACE:
                    inp = inp[:-1]

                else:
                    inp += event.unicode

        if enter == 1:
            Accuracy_msg = text_font.render("ACCURACY: " + accuracy + "%", True, (255,255,255))
            screen.blit(Accuracy_msg, (400, 300))
            WPM_msg = text_font.render("WPM: " + wpm, True, (255,255,255))
            screen.blit(WPM_msg, (440,350))

        pygame.display.update()




def Display_Page():
    MainRun = True
    while MainRun:
        screen.fill((0,0,0))
        Game_msg = heading_font.render("TYPING SPEED CALCULATOR", True, (255,255,0))
        screen.blit(Game_msg, (240,100))

        Display_msg = text_font.render("PRESS SPACE TO START", True, (255,255,200))
        screen.blit(Display_msg, (380,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainRun = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    MainRun = False
                    start_game()

        pygame.display.update()


Display_Page()