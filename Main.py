"""
Привет! Перед запуском программы тебе придётся
установить библиотеку pygame. Ведь на её основе
и была сделана эта программа.
Чтобы это сделать пропиши в терминал pip install pygame.
Благодарю🙏

"""


import pygame
from Interface import ImageButton

pygame.init()
screen = pygame.display.set_mode((500, 900))    # само окошко, его размеры, название, иконка
pygame.display.set_caption("Шахматы")

# Когда переменная True, то выводятся шахматы

start_game = False


# создание кнопочек

gray_button_back = ImageButton(500/2 - (275/2), 700, 275, 90, "Назад" , True, True, 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
gray_button_play = ImageButton(500/2 - (275/2) , 275, 275 , 90, "Играть", True , True, 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png','sounds\click.mp3')
gray_button_base_knowledge = ImageButton(500/2 - (275/2) , 400, 275, 90, "База знаний" , True, True ,'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
gray_button_exit = ImageButton(500/2 - (275/2) , 625, 275, 90, "Выход" , True, True , 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
white_button_menu = ImageButton(15 , 10, 25, 25, " " , False, False,'images\menu_button.png', 'images\menu_button.png', 'sounds\click.mp3')
gray_button_create_game = ImageButton(500/2 - (275/2)  , 300, 275, 90, "На одном устройстве " , True, True ,'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')

 # Заранее скрываю кнопки, которые не должны быть в главном меню игры
gray_button_back.set_active(False)
gray_button_create_game.set_active(False)    

running = True  # Зачем эта переменная? Чтобы правильно завершать работу программы

while running:      # вывод объектов на экран, а также основные события

    screen.fill(( (34, 34, 34)))

    pygame.draw.rect(screen,(28, 28, 28) ,(0, 0, 500, 50) )
    pygame.draw.rect(screen,(28, 28, 28) ,(0, 825, 500, 75) )

    gray_button_play.draw(screen)
    gray_button_base_knowledge.draw(screen)      # вывод на экран созданных объектов
    gray_button_exit.draw(screen)
    gray_button_back.draw(screen)
    white_button_menu.draw(screen)
    gray_button_create_game.draw(screen)
    

    gray_button_play.check_hover(pygame.mouse.get_pos()) 
    gray_button_back.check_hover(pygame.mouse.get_pos())          # благодаря вызову этого метода, можно создать эффект подсвечивания кнопки ( проще говоря анимация )
    gray_button_base_knowledge.check_hover(pygame.mouse.get_pos())
    gray_button_exit.check_hover(pygame.mouse.get_pos())
    white_button_menu.check_hover(pygame.mouse.get_pos())
    gray_button_create_game.check_hover(pygame.mouse.get_pos())
    
    # переменная, отвечающая за то, какие клавиши нажимает пользователь.
    # На самом деле незнаю, буду я её использовать или нет, пускай будет :D

    keys = pygame.key.get_pressed()

    
    # Обновление экрана ( буквально оно )

    pygame.display.update()
   
    for event in pygame.event.get():    # просмотр всех возможных событий и манипуляции с ними

        if event.type == pygame.QUIT:   # условвия для корректного завершения программы, если кнопка закрытия окна нажата, то игра закрывается и прерывает свою работу
            running = False
            pygame.quit()


        elif  event.type == pygame.MOUSEBUTTONDOWN:
            if gray_button_exit.is_active and gray_button_exit.rect.collidepoint(event.pos):     # Также в главном меню игры присутсввует кнопка выхода, при нажатии на которую вы завершаете процесс игры
                pygame.quit()
            

                # Если кнопка играть нажата, то остальные кнопки исчезают ( как будто перешёл в раздел игры )

            if gray_button_play.rect.collidepoint(event.pos) and gray_button_play.is_active:

                gray_button_play.handle_event(event)
                gray_button_base_knowledge.set_active(False)
                gray_button_exit.set_active(False)
                gray_button_play.set_active(False)
                gray_button_back.set_active(True)
                gray_button_create_game.set_active(True)

            if gray_button_create_game.rect.collidepoint(event.pos) and gray_button_create_game.is_active:

                gray_button_create_game.handle_event(event)
                start_game = True

            
                
            # Если кнопка настройки нажата, то остальные кнопки исчезают ( как будто нажал на кнопку настроек и переместился в них )
            # кнопки менюшки исчезают, а кнопка возвращения в меню появляется ( дабы создать эффект того, что можно вернуться обратно в главное меню, что так и есть)
                
            if gray_button_base_knowledge.rect.collidepoint(event.pos) and gray_button_base_knowledge.is_active:

                gray_button_base_knowledge.handle_event(event)
                gray_button_play.set_active(False)
                gray_button_base_knowledge.set_active(False) 
                gray_button_exit.set_active(False)
                gray_button_back.set_active(True)
                gray_button_create_game.set_active(False)  

                                       
                # соответственно и с кнопкой назад
                # Таким образом, нажимая на кнопку назад, мы попадаем в главное меню игры, и кнопка должна исчезнуть, а кнопки главного меню должны появиться

            if gray_button_back.rect.collidepoint(event.pos) and gray_button_back.is_active:

                gray_button_back.handle_event(event)
                gray_button_play.set_active(True)
                gray_button_base_knowledge.set_active(True)
                gray_button_exit.set_active(True)
                gray_button_back.set_active(False)
                gray_button_create_game.set_active(False)  

                
    # Блок воспроизведения звуков нажатия на кнопку

    gray_button_exit.handle_event(event)
    gray_button_base_knowledge.handle_event(event)
    gray_button_play.handle_event(event)
    gray_button_back.handle_event(event)
    white_button_menu.handle_event(event)
    gray_button_create_game.handle_event(event)  



    # Проще говоря устанавливаю максимальный фпс игры, чтобы не нагружать цп

    pygame.time.Clock().tick(60)
        
    
        

    