def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(gameDisplay, green,(150,450,100,50)) #play
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            menu_rodando = True

            
