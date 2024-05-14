import pygame
from Interface import ImageButton


pygame.init()

icon = pygame.image.load('images\icon_display.png')
screen = pygame.display.set_mode((1000, 800))    # само окошко, его размеры, название, иконка
pygame.display.set_caption("Шахматы")
Font = pygame.font.Font(None, 24)
Font_winner = pygame.font.Font(None, 30)
pygame.display.set_icon(icon)

# Когда переменная True, то выводятся шахматы

start_game = False

captured_pieces_white = []
captured_pieces_black = []

# создание кнопок

gray_button_back = ImageButton(1000/2 - (275/2), 625, 275, 90, "Назад" , True, True, 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
gray_button_play = ImageButton(1000/2 - (275/2) , 275, 275 , 90, "Играть", True , True, 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png','sounds\click.mp3')
gray_button_exit = ImageButton(1000/2 - (275/2) , 625, 275, 90, "Выход" , True, True , 'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
gray_button_create_game = ImageButton(1000/2 - (275/2)  , 400, 275, 90, "На одном устройстве " , True, True ,'images\Button_play_gray.png', 'images\Button_play_gray_hovered.png', 'sounds\click.mp3')
gray_button_back_from_game = ImageButton(920, 90, 70, 45, "" , True, False, 'images\White_button_back.png', 'images\White_button_back.png', 'sounds\click.mp3')

gray_button_back.set_active(False)
gray_button_create_game.set_active(False)
gray_button_back_from_game.set_active(False)

# Названия и позиции фигур
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (4, 0), (3, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (4, 7), (3, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

move_sound = pygame.mixer.Sound('sounds\move.mp3')
turn_step = 3
selection = 100
valid_moves = []
image_urls = ['images\Black_queen.png','images\Black_king.png','images\Black_rook.png',
              'images\Black_bishop.png','images\Black_knight.png','images\pawn_black.png',
              'images\white_queen.png','images\white_king.png','images\white_rook.png',
              'images\white_bishop.png','images\white_knight.png','images\white_pawn.png']

# Загрузка изображений
black_queen = pygame.image.load(image_urls[6])
black_queen = pygame.transform.scale(black_queen, (90, 90))
black_king = pygame.image.load(
   image_urls[7])
black_king = pygame.transform.scale(black_king, (90, 90))
black_rook = pygame.image.load(
    image_urls[8])
black_rook = pygame.transform.scale(black_rook, (90, 90))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load(
    image_urls[9])
black_bishop = pygame.transform.scale(black_bishop, (90, 90))
black_knight = pygame.image.load(
    image_urls[10])
black_knight = pygame.transform.scale(black_knight, (90, 90))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(
    image_urls[11])
black_pawn = pygame.transform.scale(black_pawn, (90, 90))

white_queen = pygame.image.load(
    image_urls[0])
white_queen = pygame.transform.scale(white_queen, (90, 90))

white_king = pygame.image.load(
   image_urls[1])
white_king = pygame.transform.scale(white_king, (90, 90))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load(
    image_urls[2])
white_rook = pygame.transform.scale(white_rook, (90, 90))
white_bishop = pygame.image.load(
    image_urls[3])
white_bishop = pygame.transform.scale(white_bishop, (90, 90))

white_knight = pygame.image.load(
    image_urls[4])
white_knight = pygame.transform.scale(white_knight, (90, 90))

white_pawn = pygame.image.load(
   image_urls[5])
white_pawn = pygame.transform.scale(white_pawn, (90, 90))

board = pygame.image.load('images\Board.png')
board = pygame.transform.scale(board,(800,800))

white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
counter = 0
winner = ''
game_over = False
running = True

def draw_pieces():
    """Выводит все фигуры на экран"""
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(
                white_pawn, (white_locations[i][0] * 100 +5, white_locations[i][1] * 100+15))
        else:
            screen.blit(white_images[index], (white_locations[i]
                                              [0] * 100 + 5, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(
                black_pawn, (black_locations[i][0] * 100 + 5, black_locations[i][1] * 100 + 15))
        else:
            screen.blit(black_images[index], (black_locations[i]
                                              [0] * 100 + 5, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)
                
def check_options(pieces, locations, turn):
    """Функция проверяет допустимые ходы всех фигур"""
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_king(position, color):
    """Проверяет допустимые ходы короля"""
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
        # всего 8 вариантов, куда может пойти король
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# проверяет ходы королевы
def check_queen(position, color):
    """Проверяет допустимые ходы королевы"""
    # ход королевы это гибрид ходов ладьи и слона, поэтому можно сделать так:
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_bishop(position, color):
    """Проверяет допустимые ходы слона"""
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_rook(position, color):
    """Проверяет допустимые ходы ладьи"""
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # ввер вниз влево вправо - 4
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position, color):
    """Проверяет допустимые ходы пешки"""
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 1) not in white_locations and \
            (position[0], position[1] + 1) not in black_locations and (position[0], position[1] + 2) not in white_locations and \
            (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
            (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 1) not in white_locations and \
            (position[0], position[1] - 1) not in black_locations and (position[0], position[1] - 2) not in white_locations and \
            (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


def check_knight(position, color):
    """Проверяет допустимые ходы коня"""
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    # 8 вариантов хода коня
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_valid_moves():
    """Проверяет допустимые ходы для выбранной фигуры"""
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# отображает доступные ходы
def draw_valid(moves):
    """Отображает допустимые ходы на экран"""
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

# отображает шах
def draw_check():
    """Рисует мигающий квадрат возле короля, если тот находится под шахом"""
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

while running:      # вывод объектов на экран, а также основные события
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_pieces()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    screen.fill(( (34, 34, 34)))
    if not start_game:
        pygame.draw.rect(screen,(28, 28, 28) ,(0, 0, 1000, 50) )
        pygame.draw.rect(screen,(28, 28, 28) ,(0, 750, 1000, 50) )

    gray_button_play.draw(screen)
    gray_button_exit.draw(screen)
    gray_button_back.draw(screen)
    gray_button_create_game.draw(screen)
    gray_button_back_from_game.draw(screen)
    
    gray_button_exit.check_hover(pygame.mouse.get_pos()) 
    gray_button_play.check_hover(pygame.mouse.get_pos()) 
    gray_button_back.check_hover(pygame.mouse.get_pos())          # благодаря вызову этого метода, можно создать эффект подсвечивания кнопки ( проще говоря анимация )
    gray_button_create_game.check_hover(pygame.mouse.get_pos())
    gray_button_back_from_game.check_hover(pygame.mouse.get_pos())

    if start_game:
        screen.blit(board,(0,0))
        if counter < 30:
            counter += 1
        else:
            counter = 0
        draw_pieces()
        draw_check()
        if selection != 100:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves)
    
    if winner != '':
        game_over = True
        screen.blit(Font_winner.render(
        f'{winner} победили!', True, 'white'),(807, 500))

    # Обновление экрана

    pygame.display.update()
   
    for event in pygame.event.get():    # просмотр всех возможных событий и манипуляции с ними
        if start_game:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                    x_coord = event.pos[0] // 100
                    y_coord = event.pos[1] // 100
                    click_coords = (x_coord, y_coord)
                    if turn_step <= 1:
                        if click_coords == (8, 8) or click_coords == (9, 8):
                           winner = 'Белые'
                        if click_coords in white_locations:
                            selection = white_locations.index(click_coords)
                            if turn_step == 0:
                                turn_step = 1
                        if click_coords in valid_moves and selection != 100:
                            white_locations[selection] = click_coords
                            if click_coords in black_locations:
                                black_piece = black_locations.index(click_coords)
                                captured_pieces_white.append(black_pieces[black_piece])
                                if black_pieces[black_piece] == 'king':
                                    winner = 'Чёрные'
                                black_pieces.pop(black_piece)
                                black_locations.pop(black_piece)
                            black_options = check_options(
                                black_pieces, black_locations, 'black')
                            white_options = check_options(
                                white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                    if turn_step > 1:
                        if click_coords == (8, 8) or click_coords == (9, 8):
                            winner = 'Чёрные'
                        if click_coords in black_locations:
                            selection = black_locations.index(click_coords)
                            if turn_step == 2:
                                turn_step = 3
                        if click_coords in valid_moves and selection != 100:
                            black_locations[selection] = click_coords
                            if click_coords in white_locations:
                                white_piece = white_locations.index(click_coords)
                                captured_pieces_black.append(white_pieces[white_piece])
                                if white_pieces[white_piece] == 'king':
                                    winner = 'Белые'
                                white_pieces.pop(white_piece)
                                white_locations.pop(white_piece)
                            black_options = check_options(
                                black_pieces, black_locations, 'black')
                            white_options = check_options(
                                white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
                    # воспроизведение звука фигур
                    if selection == 100 and (click_coords in white_locations and turn_step==2) or (click_coords in black_locations and turn_step == 0) and turn_step != 3:
                        move_sound.play()

                if event.type == pygame.MOUSEBUTTONDOWN and gray_button_back_from_game.rect.collidepoint(event.pos):
                        
                    game_over = False
                    start_game = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (4, 0), (3, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (4, 7), (3, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    captured_pieces_white = []
                    captured_pieces_black = []
                    turn_step = 3
                    selection = 100
                    valid_moves = []
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
                        
        if event.type == pygame.QUIT:   # условвия для корректного завершения программы, если кнопка закрытия окна нажата, то игра закрывается и прерывает свою работу
            running = False
            pygame.quit()

        elif  event.type == pygame.MOUSEBUTTONDOWN:
            if gray_button_exit.is_active and gray_button_exit.rect.collidepoint(event.pos):     # Также в главном меню игры присутсввует кнопка выхода, при нажатии на которую вы завершаете процесс игры
                pygame.quit()

                # Если кнопка играть нажата, то остальные кнопки исчезают ( как будто перешёл в раздел игры )

            if gray_button_play.rect.collidepoint(event.pos) and gray_button_play.is_active:

                gray_button_play.handle_event(event)
                gray_button_exit.set_active(False)
                gray_button_play.set_active(False)
                gray_button_back.set_active(True)
                gray_button_create_game.set_active(True)
                gray_button_back_from_game.set_active(False)

            if gray_button_create_game.rect.collidepoint(event.pos) and gray_button_create_game.is_active:

                gray_button_create_game.handle_event(event)
                gray_button_back.set_active(False)
                gray_button_back_from_game.set_active(True)
                start_game = True
                
                # соответственно и с кнопкой назад
                # Таким образом, нажимая на кнопку назад, мы попадаем в главное меню игры, и кнопка должна исчезнуть, а кнопки главного меню должны появиться

            if gray_button_back.rect.collidepoint(event.pos) and gray_button_back.is_active:

                gray_button_back.handle_event(event)
                gray_button_play.set_active(True)
                gray_button_exit.set_active(True)
                gray_button_back.set_active(False)
                gray_button_create_game.set_active(False)  
                gray_button_back_from_game.set_active(False)

            if gray_button_back_from_game.rect.collidepoint(event.pos) and gray_button_back_from_game.is_active:
                
                gray_button_back_from_game.handle_event(event)
                gray_button_play.set_active(False)
                gray_button_exit.set_active(False)
                gray_button_back.set_active(True)
                gray_button_create_game.set_active(True)
                start_game = False
                gray_button_back_from_game.set_active(False)
    
    
    # Блок воспроизведения звуков нажатия на кнопку

    gray_button_exit.handle_event(event)
    gray_button_play.handle_event(event)
    gray_button_back.handle_event(event)
    gray_button_create_game.handle_event(event)  
    gray_button_back_from_game.handle_event(event)

    # Проще говоря устанавливаю максимальный фпс игры, чтобы не нагружать цп

    pygame.time.Clock().tick(60)
        
    
        

    