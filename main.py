import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((590, 750))
pygame.display.set_caption('Calculadora')
display = ''


def load():
    global t, t2, t3, t4, t5, t6, t7, t8, t9, t0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10

    #Texto
    font = pygame.font.Font('SedgwickAveDisplay-Regular.ttf', 78)
    t = font.render(" 7", False, (240, 240, 240))
    t2 = font.render(" 4", False, (240, 240, 240))
    t3 = font.render(" 1", False, (240, 240, 240))
    t4 = font.render(" 8", False, (240, 240, 240))
    t5 = font.render(" 5", False, (240, 240, 240))
    t6 = font.render(" 2", False, (240, 240, 240))
    t7 = font.render(" 9", False, (240, 240, 240))
    t8 = font.render(" 6", False, (240, 240, 240))
    t9 = font.render(" 3", False, (240, 240, 240))
    t0 = font.render(" 0", False, (240, 240, 240))
    m1 = font.render(" Ce ", False, (240, 240, 240))
    m2 = font.render(" + ", False, (240, 240, 240))
    m3 = font.render(" - ", False, (240, 240, 240))
    m4 = font.render(" = ", False, (240, 240, 240))
    m5 = font.render("  * ", False, (240, 240, 240))
    m6 = font.render(" / ", False, (240, 240, 240))
    m7 = font.render(" ( ", False, (240, 240, 240))
    m8 = font.render("   ) ", False, (240, 240, 240))
    m9 = font.render(" . ", False, (240, 240, 240))
    m10 = font.render(" % ", False, (240, 240, 240))


load()


def draw():
    global click1, click2, click3, click4, click5, click6, click7, click8, click9, tt, display, click10, click11, click12, click13, click14, click15, click16, click17, click18, click19, click20
    #Fundo
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 550, 600))
    pygame.draw.rect(screen, (45, 45, 45), (40, 30, 500, 90))

    #Armação
    pygame.draw.rect(screen, (255, 255, 255), (60, 350, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (50, 150, 10, 500))
    pygame.draw.rect(screen, (255, 255, 255), (520, 150, 10, 500))
    pygame.draw.rect(screen, (255, 255, 255), (60, 250, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (170, 150, 10, 500))
    pygame.draw.rect(screen, (255, 255, 255), (280, 150, 10, 500))
    pygame.draw.rect(screen, (255, 255, 255), (400, 150, 10, 500))
    pygame.draw.rect(screen, (255, 255, 255), (60, 450, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (50, 550, 480, 10))
    pygame.draw.rect(screen, (255, 255, 255), (50, 140, 480, 10))
    pygame.draw.rect(screen, (255, 255, 255), (50, 650, 480, 10))
    #Borda
    pygame.draw.rect(screen, (48, 166, 180), (0, 0, 575, 10))
    pygame.draw.rect(screen, (48, 166, 180), (0, 740, 575, 10))
    pygame.draw.rect(screen, (48, 166, 180), (575, 0, 10, 750))
    pygame.draw.rect(screen, (48, 166, 180), (0, 0, 10, 750))

    # Calculadora
    click1 = pygame.draw.rect(screen, (82, 179, 135), (59, 360, 112, 90))
    click2 = pygame.draw.rect(screen, (82, 179, 135), (59, 260, 112, 90))
    click3 = pygame.draw.rect(screen, (82, 179, 135), (59, 150, 112, 100))

    click4 = pygame.draw.rect(screen, (82, 179, 135), (180, 360, 100, 90))
    click5 = pygame.draw.rect(screen, (82, 179, 135), (180, 260, 100, 90))
    click6 = pygame.draw.rect(screen, (82, 179, 135), (180, 150, 100, 100))

    click7 = pygame.draw.rect(screen, (82, 179, 135), (290, 360, 110, 90))
    click8 = pygame.draw.rect(screen, (82, 179, 135), (290, 260, 110, 90))
    click9 = pygame.draw.rect(screen, (82, 179, 135), (290, 150, 110, 100))

    click16 = pygame.draw.rect(screen, (161, 14, 3), (410, 150, 110, 100))
    click11 = pygame.draw.rect(screen, (0, 0, 0), (410, 260, 110, 90))
    click12 = pygame.draw.rect(screen, (0, 0, 0), (410, 360, 110, 90))
    click13 = pygame.draw.rect(screen, (4, 169, 201), (290, 460, 110, 90))
    click14 = pygame.draw.rect(screen, (0, 0, 0), (410, 460, 110, 90))
    click15 = pygame.draw.rect(screen, (82, 179, 135), (60, 460, 110, 90))
    click10 = pygame.draw.rect(screen, (0, 0, 0), (420, 560, 100, 90))
    click17 = pygame.draw.rect(screen, (0, 0, 0), (65, 560, 100, 90))
    click18 = pygame.draw.rect(screen, (0, 0, 0), (180, 560, 100, 90))
    click19 = pygame.draw.rect(screen, (0, 0, 0), (180, 460, 100, 90))
    click20 = pygame.draw.rect(screen, (0, 0, 0), (290, 560, 110, 90))

    font = pygame.font.Font('SedgwickAveDisplay-Regular.ttf', 78)
    tt = font.render(display, False, (240, 240, 240))


while running:
    draw()
    screen.blit(t, t.get_rect(top=160, left=59))
    screen.blit(t2, t.get_rect(top=260, left=59))
    screen.blit(t3, t.get_rect(top=360, left=59))
    screen.blit(t4, t.get_rect(top=160, left=180))
    screen.blit(t5, t.get_rect(top=260, left=180))
    screen.blit(t6, t.get_rect(top=360, left=180))
    screen.blit(t7, t.get_rect(top=160, left=290))
    screen.blit(t8, t.get_rect(top=260, left=290))
    screen.blit(t9, t.get_rect(top=360, left=290))
    screen.blit(t0, t.get_rect(top=460, left=59))
    screen.blit(m1, t.get_rect(top=160, left=405))
    screen.blit(m2, t.get_rect(top=260, left=420))
    screen.blit(m3, t.get_rect(top=360, left=420))
    screen.blit(m4, t.get_rect(top=460, left=290))
    screen.blit(m5, t.get_rect(top=480, left=400))
    screen.blit(tt, t.get_rect(top=40, left=70))
    screen.blit(m6, t.get_rect(top=560, left=430))
    screen.blit(m7, t.get_rect(top=565, left=60))
    screen.blit(m8, t.get_rect(top=565, left=160))
    screen.blit(m9, t.get_rect(top=455, left=200))
    screen.blit(m10, t.get_rect(top=555, left=290))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if len(display) <= 8:
                if click1.collidepoint(pygame.mouse.get_pos()):
                    display += '1'
                if click2.collidepoint(pygame.mouse.get_pos()):
                    display += '4'
                if click3.collidepoint(pygame.mouse.get_pos()):
                    display += '7'
                if click4.collidepoint(pygame.mouse.get_pos()):
                    display += '2'
                if click5.collidepoint(pygame.mouse.get_pos()):
                    display += '5'
                if click6.collidepoint(pygame.mouse.get_pos()):
                    display += '8'
                if click7.collidepoint(pygame.mouse.get_pos()):
                    display += '3'
                if click8.collidepoint(pygame.mouse.get_pos()):
                    display += '6'
                if click9.collidepoint(pygame.mouse.get_pos()):
                    display += '9'

                if click10.collidepoint(pygame.mouse.get_pos()):
                    display += '/'

                if click11.collidepoint(pygame.mouse.get_pos()):
                    display += '+'

                if click12.collidepoint(pygame.mouse.get_pos()):
                    display += '-'

                if click14.collidepoint(pygame.mouse.get_pos()):
                    display += '*'

                if click15.collidepoint(pygame.mouse.get_pos()):
                    display += '0'

                if click17.collidepoint(pygame.mouse.get_pos()):
                    display += '('

                if click18.collidepoint(pygame.mouse.get_pos()):
                    display += ')'

                if click19.collidepoint(pygame.mouse.get_pos()):
                    display += '.'

                if click20.collidepoint(pygame.mouse.get_pos()):
                    display += '%'

            if click13.collidepoint(pygame.mouse.get_pos()):
                if display[0] == '=':
                    display = display[1:]
                if display[0] != '*' or display[0] != '/' or display[
                        0] != '.' or display[0] != '%':
                    try:
                        if type(eval(display)) == float:
                            display = str('%.4f' % eval(display))
                        else:
                            display = str(eval(display))
                    except:
                        display = 'ERRO'

            if click16.collidepoint(pygame.mouse.get_pos()):
                display = ''

    pygame.display.update()
pygame.quit()
