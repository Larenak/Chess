import pygame

class ImageButton:

# данные для создания кнопки и характеристики кнопки

    
    def __init__(self, x, y, width, height, text, hide_when_pressed, resize_when_hovered, image_path, hover_image_path=None, sound_path=None, is_active = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.is_active = is_active
        self.hide_when_pressed = hide_when_pressed
        self.resize_when_hovered = resize_when_hovered
        

    # импорт кнопки и её отображение
    # НЕ ТРОГАТЬ, ОНО РАБОТАЕТ!!!!
        
        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)

            if self.resize_when_hovered:

                """
                Если при создании обьекта (кнопки) указано, что его текстура должна
                увеличиваться при наведении пользователем на него, то она будет уввеличиваться, иначе размер кнопки
                останется неизменным
                """

                self.hover_image = pygame.transform.scale(self.hover_image, ((width + 10), (height + 10)))
            else:   
                self.hover_image = pygame.transform.scale(self.hover_image, ((width), (height)))
 
    
        self.rect = self.image.get_rect(topleft = (x, y))
        self.sound = None

        # звук

        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False


    # метод отображения кнопки
        
    def draw(self, screen):
        if self.is_active:              # Если на кнопку навелся пользователь, то она увеличивается  

            current_image = self.hover_image if self.is_hovered else self.image
            if current_image == self.hover_image:
                    
                    # Такая же операция, как и в 29 строчке: Если навелся на кнопку, то она увеличивается,а если не прописано, что она должна увеличиваться, то не увеличивается

                    if self.resize_when_hovered:
                        screen.blit(current_image, (self.rect.x - 5, self.rect.y + 5))
                    else:
                        screen.blit(current_image, (self.rect.x, self.rect.y))
                
            else:
                screen.blit(current_image, self.rect.topleft)
                  # Если на кнопку навелся пользователь, то она увеличивается


    # текст
            Font = pygame.font.Font(None, 32)
            text_surface = Font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(midbottom = self.rect.midbottom)
            
            # Если на кнопку навёлся пользователь, то её текст смещается в соответствии с изменением размеров кнопки при наведении на неё пользователем
            # Также, когда пользователь навелся на кнопку, то текст в ней увеличивается в размерах
            
            if current_image == self.hover_image:
                                                
                Font = pygame.font.Font(None, 36)
                text_surface = Font.render(self.text, True, (255, 255, 255))

                text_rect.y -= 7
                text_rect.x -= 7

            else:
                                                # Размер текста, если на кнопку не наводится пользователь

                Font = pygame.font.Font(None, 32)
                text_surface = Font.render(self.text, True, (255, 255, 255))

                text_rect.y -= 20
                text_rect.x += 1

            screen.blit(text_surface, text_rect)

    # подсвечивание кнопки при наведении мышки на объект

    def check_hover(self, mouse_pos):
        self.is_hovered =  self.is_active and self.rect.collidepoint(mouse_pos)

    # обработка событий ( нажатие мыши )
        
    def handle_event(self, event):
        if self.is_active:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
                if self.sound:
                    self.sound.play()
                if self.hide_when_pressed:
                    self.is_active = False
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button = self))
    
    # показывает кнопки или скрывает их

    def set_active(self, is_active):
        self.is_active = is_active
                