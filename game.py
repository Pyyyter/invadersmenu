from PPlay import sprite, mouse, window, keyboard

gamestate = 0
dificuldade = 2

mouse = mouse.Mouse()
keyboard = keyboard.Keyboard()
janela = window.Window(1000, 520)

background = sprite.Sprite("assets/Wall.png")

jogar = sprite.Sprite("assets/Jogar.png")
jogar.set_position(900-jogar.width/2, 25)
dificuldade_img = sprite.Sprite("assets/Dificuldade.png")
dificuldade_img.set_position(900-dificuldade_img.width/2, (50+jogar.height) + 25)
ranking = sprite.Sprite("assets/Ranking.png")
ranking.set_position(900-ranking.width/2, (50+jogar.height)*2 + 25)
sair_img = sprite.Sprite("assets/Sair.png")
sair_img.set_position(900-sair_img.width/2, (50+jogar.height)*3 + 25)

easy = sprite.Sprite("assets/Facil.png")
easy.set_position(900-easy.width/2, 25)
normal = sprite.Sprite("assets/Medio.png")
normal.set_position(900-normal.width/2, (50+jogar.height) + 25)
hard = sprite.Sprite("assets/Dificil.png")
hard.set_position(900-hard.width/2, (50+jogar.height)*2 + 25)

while True:
    click = mouse.is_button_pressed(1)
    background.draw()
    if gamestate == 0:
        jogar.draw()
        dificuldade_img.draw()
        ranking.draw()
        sair_img.draw()
        if mouse.is_over_object(jogar) and click:
            gamestate = 1
        if mouse.is_over_object(dificuldade_img) and click:
            gamestate = 2
        if mouse.is_over_object(sair_img) and click:
            janela.close()
    if gamestate == 1:
        if keyboard.key_pressed("esc"):
            gamestate = 0
    if gamestate == 2:
        easy.draw()
        normal.draw()
        hard.draw()
        if mouse.is_over_object(easy) and click:
            dificuldade = 1
        if mouse.is_over_object(normal) and click:
            dificuldade = 2
        if mouse.is_over_object(hard) and click:
            dificuldade = 3
        if keyboard.key_pressed("esc"):
            gamestate = 0


    click = False
    janela.update()