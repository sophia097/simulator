import pygame
import sys

pygame.init()

# Setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
PLAY_IMAGE = pygame.transform.scale(pygame.image.load("play_button.png"), (250, 100))
RULES_IMAGE = pygame.transform.scale(pygame.image.load("rules_button.png"), (250, 100))
QUIT_IMAGE = pygame.transform.scale(pygame.image.load("quit_button.png"), (250, 100))
BG_IMAGE = pygame.transform.scale(pygame.image.load("menu_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
CHARACTER_BG = pygame.transform.scale(pygame.image.load("character_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
BACK_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load("back_button.png"), (80, 40))
PROCEED_IMAGE = pygame.transform.scale(pygame.image.load("proceed_button.png"), (200, 80))
BEDROOM_IMAGE = pygame.transform.scale(pygame.image.load("bedroom_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
KITCHEN_IMAGE = pygame.transform.scale(pygame.image.load("kitchen_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
FRIDGE_INSIDE_IMAGE = pygame.transform.scale(pygame.image.load("fridge_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
BOY_TEXT = pygame.transform.scale(pygame.image.load("boy_text.png"), (600, 200))
GIRL_TEXT = pygame.transform.scale(pygame.image.load("girl_text.png"), (600, 200))
NONBINARY_TEXT = pygame.transform.scale(pygame.image.load("non_binary_text.png"), (600, 200))
SANDWICH_IMAGE = pygame.transform.scale(pygame.image.load("sandwich.png"), (200, 150))
BREAD = pygame.transform.scale(pygame.image.load("bread.png"), (200, 200))
APPLE = pygame.transform.scale(pygame.image.load("apple.png"), (200, 200))
EGGPLANT = pygame.transform.scale(pygame.image.load("eggplant.png"), (200, 200))
CHICKEN = pygame.transform.scale(pygame.image.load("chicken.png"), (200, 200))
CARROT = pygame.transform.scale(pygame.image.load("carrot.png"), (200, 200))
CLASSROOM_BG = pygame.transform.scale(pygame.image.load("classroom_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYGROUND_IMAGE = pygame.transform.scale(pygame.image.load("playground2_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
GLITCHGROUND_IMAGE = pygame.transform.scale(pygame.image.load("glitched.playground2_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
CREDITS=pygame.transform.scale(pygame.image.load("credits2_bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
# Load character images
character1 = pygame.image.load("Boy.png")
character2 = pygame.image.load("Girl.png")
character3 = pygame.image.load("Nonbinary.png")

# Global to track selected player image
selected_player_image = None

# Button class
class Button:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

# Player class
class Player:
    def __init__(self, image, x, y):
        self.image = pygame.transform.scale(image, (100, 150))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Fade in effect
def fade_in(screen, background_image, duration=1000):
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.fill((0, 0, 0))
    fade_surface.set_alpha(255)
    start_time = pygame.time.get_ticks()

    while True:
        elapsed = pygame.time.get_ticks() - start_time
        alpha = max(255 - int((255 * elapsed) / duration), 0)

        screen.blit(background_image, (0, 0))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        CLOCK.tick(60)

        if alpha == 0:
            break

# Main Menu
def main_menu():
    while True:
        SCREEN.blit(BG_IMAGE, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=PLAY_IMAGE, pos=(SCREEN_WIDTH // 2, 250))
        
        QUIT_BUTTON = Button(image=QUIT_IMAGE, pos=(SCREEN_WIDTH // 2, 490))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        CLOCK.tick(60)

# Character selection
def play():
    global selected_player_image

    selected_character = None
    bounce_offset = 0
    bounce_direction = 1

    character1_button = Button(image=pygame.transform.scale(character1, (100, 150)), pos=(SCREEN_WIDTH // 4, 350))
    character2_button = Button(image=pygame.transform.scale(character2, (100, 150)), pos=(SCREEN_WIDTH // 2, 350))
    character3_button = Button(image=pygame.transform.scale(character3, (100, 150)), pos=(SCREEN_WIDTH * 3 // 4, 350))

    play_back_button = Button(image=BACK_BUTTON_IMAGE, pos=(60, 40))
    proceed_button = Button(image=PROCEED_IMAGE, pos=(SCREEN_WIDTH // 2, 650))

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(CHARACTER_BG, (0, 0))

        if selected_character:
            bounce_offset += bounce_direction * 2
            if bounce_offset > 10 or bounce_offset < -10:
                bounce_direction *= -1
        else:
            bounce_offset = 0

        character1_button.rect.centery = 350 + bounce_offset if selected_character == "Boy" else 350
        character2_button.rect.centery = 350 + bounce_offset if selected_character == "Girl" else 350
        character3_button.rect.centery = 350 + bounce_offset if selected_character == "Nonbinary" else 350

        for button in [character1_button, character2_button, character3_button]:
            button.update(SCREEN)

        if selected_character:
            selected_text = pygame.font.SysFont("arial", 30).render(f"You selected: {selected_character}", True, WHITE)
            selected_rect = selected_text.get_rect(center=(SCREEN_WIDTH // 2, 550))
            SCREEN.blit(selected_text, selected_rect)
            proceed_button.update(SCREEN)

        play_back_button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if character1_button.checkForInput(PLAY_MOUSE_POS):
                    selected_character = "Boy"
                    selected_player_image = character1
                if character2_button.checkForInput(PLAY_MOUSE_POS):
                    selected_character = "Girl"
                    selected_player_image = character2
                if character3_button.checkForInput(PLAY_MOUSE_POS):
                    selected_character = "Nonbinary"
                    selected_player_image = character3
                if play_back_button.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if selected_character and proceed_button.checkForInput(PLAY_MOUSE_POS):
                    next_screen()

        pygame.display.update()
        CLOCK.tick(60)

# Bedroom typing scene
def next_screen():
    fade_in(SCREEN, BEDROOM_IMAGE, duration=1000)

    player = Player(selected_player_image, 750, 400)
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT

    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "I need to get ready for school!"
    font = pygame.font.SysFont("arial", 28)

    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    text_done = False
    text_done_time = 0

    while True:
        SCREEN.blit(BEDROOM_IMAGE, (0, 0))
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(SCREEN)
        SCREEN.blit(comment_image, comment_rect)

        now = pygame.time.get_ticks()
        if current_letter_index < len(text_to_type):
            if now - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = now
        else:
            if not text_done:
                text_done = True
                text_done_time = pygame.time.get_ticks()

        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width() // 2, comment_rect.centery - text_surface.get_height() // 2 + 30))

        if text_done and pygame.time.get_ticks() - text_done_time > 2000:
            fade_in(SCREEN, KITCHEN_IMAGE, duration=1000)
            kitchen_scene(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(60)

# Kitchen scene
def kitchen_scene(player):
    fridge_rect = pygame.Rect(20, 30, 100, 250)

    # Use the same comment image based on the selected character
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT
    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "Click the fridge to make a sandwich!"
    font = pygame.font.SysFont("arial", 28)

    text_done = False
    text_done_time = 0

    while True:
        SCREEN.blit(KITCHEN_IMAGE, (0, 0))
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(SCREEN)
        SCREEN.blit(comment_image, comment_rect)

        now = pygame.time.get_ticks()
        if current_letter_index < len(text_to_type):
            if now - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = now
        else:
            if not text_done:
                text_done = True
                text_done_time = pygame.time.get_ticks()

        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width() // 2, comment_rect.centery - text_surface.get_height() // 2 + 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fridge_rect.collidepoint(pygame.mouse.get_pos()):
                    fridge_game()

        pygame.display.update()
        CLOCK.tick(60)


# Fridge minigame
def fridge_game():
    bread_rect = BREAD.get_rect(topleft=(100, -50))
    apple_rect = APPLE.get_rect(topleft=(300, -20))
    eggplant_rect = EGGPLANT.get_rect(topleft=(500, -70))
    chicken_rect = CHICKEN.get_rect(topleft=(700, 50))
    carrot_rect = CARROT.get_rect(topleft=(900, 100))

    foods = [
        {"image": BREAD, "rect": bread_rect, "clicked": False},
        {"image": APPLE, "rect": apple_rect, "clicked": False},
        {"image": EGGPLANT, "rect": eggplant_rect, "clicked": False},
        {"image": CHICKEN, "rect": chicken_rect, "clicked": False},
        {"image": CARROT, "rect": carrot_rect, "clicked": False}
    ]

    STOP_Y = SCREEN_HEIGHT - 200

    while True:
        SCREEN.blit(FRIDGE_INSIDE_IMAGE, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for food in foods:
                    if food["rect"].collidepoint(mouse_pos):
                        food["clicked"] = True

        all_collected = True
        for food in foods:
            if not food["clicked"]:
                if food["rect"].y < STOP_Y:
                    food["rect"].y += 2
                SCREEN.blit(food["image"], food["rect"])
                all_collected = False

        if all_collected:
            fade_in(SCREEN, KITCHEN_IMAGE, duration=1000)
            kitchen_scene_with_sandwich()
            return

        pygame.display.update()
        CLOCK.tick(60)

def kitchen_scene_with_sandwich():
    player = Player(selected_player_image, 750, 400)
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT
    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "I have to get to school! I'm running late!"
    font = pygame.font.SysFont("arial", 28)

    sandwich_image = pygame.transform.scale(SANDWICH_IMAGE, (80, 50))  # make sandwich smaller

    text_done = False
    text_done_time = 0

    while True:
        SCREEN.blit(KITCHEN_IMAGE, (0, 0))
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(SCREEN)

        # Draw the sandwich next to player
        sandwich_offset = (30, 100)  # x and y offset
        SCREEN.blit(sandwich_image, (player.rect.x + sandwich_offset[0], player.rect.y + sandwich_offset[1]))

        SCREEN.blit(comment_image, comment_rect)

        now = pygame.time.get_ticks()
        if current_letter_index < len(text_to_type):
            if now - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = now
        else:
            if not text_done:
                text_done = True
                text_done_time = pygame.time.get_ticks()

        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width() // 2, comment_rect.centery - text_surface.get_height() // 2 + 30))

        if text_done and pygame.time.get_ticks() - text_done_time > 3000:
            fade_in(SCREEN, CLASSROOM_BG, duration=1000)
            classroom_scene(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(60)
        
def classroom_scene(player):
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT
    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "Let's do the math quiz!"
    font = pygame.font.SysFont("arial", 28)

    text_done = False
    text_done_time = 0

    while True:
        SCREEN.blit(CLASSROOM_BG, (0, 0))
        player.draw(SCREEN)
        SCREEN.blit(comment_image, comment_rect)

        now = pygame.time.get_ticks()
        if current_letter_index < len(text_to_type):
            if now - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = now
        else:
            if not text_done:
                text_done = True
                text_done_time = pygame.time.get_ticks()

        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width() // 2, comment_rect.centery - text_surface.get_height() // 2 + 30))

        if text_done and pygame.time.get_ticks() - text_done_time > 2000:
            fade_in(SCREEN, CLASSROOM_BG, duration=1000)
            math_quiz()
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(60)
def math_quiz():
    questions = [
        {"question": "What is 5 + 7?", "answers": ["12", "13", "11", "10"], "correct": 0},
        {"question": "What is 8 × 3?", "answers": ["24", "21", "32", "16"], "correct": 0},
        {"question": "What is 15 - 9?", "answers": ["6", "5", "7", "4"], "correct": 0},
        {"question": "What is 20 ÷ 4?", "answers": ["5", "4", "6", "8"], "correct": 0},
        {"question": "What is 9 + 6?", "answers": ["15", "14", "16", "13"], "correct": 0}
    ]
    
    current_question = 0
    score = 0
    answer_buttons = []
    question_font = pygame.font.SysFont("arial", 40)
    answer_font = pygame.font.SysFont("arial", 30)
    feedback_font = pygame.font.SysFont("arial", 36)
    
    # Create answer buttons
    for i in range(4):
        button = Button(image=pygame.Surface((300, 60)), pos=(SCREEN_WIDTH // 2, 300 + i * 80))
        button.image.fill((200, 200, 200))
        answer_buttons.append(button)
    
    next_button = Button(image=pygame.Surface((200, 60)), pos=(SCREEN_WIDTH // 2, 600))
    next_button.image.fill((100, 200, 100))
    next_text = answer_font.render("Next", True, BLACK)
    next_text_rect = next_text.get_rect(center=next_button.rect.center)
    
    feedback = ""
    feedback_color = BLACK
    show_next = False
    
    while current_question < len(questions):
        SCREEN.fill(WHITE)
        question = questions[current_question]
        
        # Draw question
        question_text = question_font.render(question["question"], True, BLACK)
        SCREEN.blit(question_text, (SCREEN_WIDTH // 2 - question_text.get_width() // 2, 150))
        
        # Draw answer buttons
        for i, button in enumerate(answer_buttons):
            button.update(SCREEN)
            answer_text = answer_font.render(question["answers"][i], True, BLACK)
            answer_rect = answer_text.get_rect(center=button.rect.center)
            SCREEN.blit(answer_text, answer_rect)
        
        # Draw feedback
        if feedback:
            feedback_text = feedback_font.render(feedback, True, feedback_color)
            SCREEN.blit(feedback_text, (SCREEN_WIDTH // 2 - feedback_text.get_width() // 2, 500))
        
        # Draw next button if needed
        if show_next:
            next_button.update(SCREEN)
            SCREEN.blit(next_text, next_text_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not show_next:
                    for i, button in enumerate(answer_buttons):
                        if button.checkForInput(mouse_pos):
                            if i == question["correct"]:
                                feedback = "Correct!"
                                feedback_color = (0, 200, 0)
                                score += 1
                            else:
                                feedback = f"Wrong! Correct answer: {question['answers'][question['correct']]}"
                                feedback_color = (200, 0, 0)
                            show_next = True
                elif show_next and next_button.checkForInput(mouse_pos):
                    current_question += 1
                    feedback = ""
                    show_next = False
        
        pygame.display.update()
        CLOCK.tick(60)
    
    # Show final score and fade back to classroom
    score_display_time = 0
    show_score = True
    
    while show_score:
        SCREEN.fill(WHITE)
        score_text = question_font.render(f"Quiz Complete! Score: {score}/{len(questions)}", True, BLACK)
        SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        
        continue_button = Button(image=pygame.Surface((200, 60)), pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        continue_button.image.fill((100, 200, 100))
        continue_button.update(SCREEN)
        continue_text = answer_font.render("Continue", True, BLACK)
        continue_rect = continue_text.get_rect(center=continue_button.rect.center)
        SCREEN.blit(continue_text, continue_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.checkForInput(mouse_pos):
                    show_score = False
        
        pygame.display.update()
        CLOCK.tick(60)
    
    # Fade back to classroom
    fade_in(SCREEN, CLASSROOM_BG, duration=1000)
    classroom_after_quiz()
    
    
def classroom_after_quiz():
    player = Player(selected_player_image, 750, 400)
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT
    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "That was a great quiz! Time for Recess!"
    font = pygame.font.SysFont("arial", 28)

    text_done = False
    text_done_time = 0
    transition_started = False

    while True:
        # Always draw the classroom background first
        SCREEN.blit(CLASSROOM_BG, (0, 0))
        player.draw(SCREEN)
        SCREEN.blit(comment_image, comment_rect)

        now = pygame.time.get_ticks()
        
        # Handle typing effect
        if current_letter_index < len(text_to_type):
            if now - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = now
        else:
            if not text_done:
                text_done = True
                text_done_time = now

        # Draw typed text
        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width() // 2, 
                                     comment_rect.centery - text_surface.get_height() // 2 + 30))

        # Handle transition to playground
        if text_done and not transition_started:
            if now - text_done_time > 2000:  # Wait 2 seconds after text is done
                fade_in(SCREEN, PLAYGROUND_IMAGE, duration=1000)
                transition_started = True
                playground_scene()  # Call the playground scene function

def playground_scene():
    # Initialize background
    current_bg = PLAYGROUND_IMAGE
    scene_start_time = pygame.time.get_ticks()

    # Player and dialogue setup
    player = Player(selected_player_image, 750, 400)
    comment_image = BOY_TEXT if selected_player_image == character1 else GIRL_TEXT if selected_player_image == character2 else NONBINARY_TEXT
    comment_rect = comment_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))

    # Typing effect
    typed_text = ""
    typing_speed = 50
    last_letter_time = pygame.time.get_ticks()
    current_letter_index = 0
    text_to_type = "Hmmm... What should I do on the playground?"
    font = pygame.font.SysFont("arial", 28)

    # Glitch timing
    glitch_start_time = 0
    glitch_started = False
    glitching_active = False
    glitch_duration = 3000  # 3 seconds glitching
    glitch_interval = 200   # ms between switches
    last_glitch_switch = 0

    # Dialogue Flags
    first_dialogue_done = False
    second_dialogue_done = False
    third_dialogue_done = False
    last_dialogue_done = False  # New flag for checking the last dialogue

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        scene_elapsed = current_time - scene_start_time

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Start glitch after 5 seconds
        if not glitch_started and scene_elapsed >= 5000:
            glitch_started = True
            glitching_active = True
            glitch_start_time = current_time
            last_glitch_switch = current_time
            current_bg = GLITCHGROUND_IMAGE  # Start with glitch background

        # Handle glitch effect
        if glitching_active:
            # Switch backgrounds at the specified interval
            if current_time - last_glitch_switch >= glitch_interval:
                current_bg = GLITCHGROUND_IMAGE if current_bg == PLAYGROUND_IMAGE else PLAYGROUND_IMAGE
                last_glitch_switch = current_time

            # Check if glitch duration has ended
            if current_time - glitch_start_time >= glitch_duration:
                glitching_active = False
                current_bg = PLAYGROUND_IMAGE  # Force set to normal background

        # Draw everything
        SCREEN.blit(current_bg, (0, 0))
        player.draw(SCREEN)
        SCREEN.blit(comment_image, comment_rect)

        # Typing effect for the initial dialogue
        if current_letter_index < len(text_to_type):
            if current_time - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = current_time

        # Draw typed text
        if typed_text:
            text_surface = font.render(typed_text, True, BLACK)
            SCREEN.blit(text_surface, (comment_rect.centerx - text_surface.get_width()//2, 
                                     comment_rect.centery - text_surface.get_height()//2 + 30))

        # Once glitch ends, move to new dialogue
        if not first_dialogue_done and not glitching_active and current_letter_index >= len(text_to_type):
            if current_time - last_letter_time > 2000:  # Wait 2 seconds after glitch ends
                typed_text = ""  # Clear current text
                text_to_type = "Girl: Did you see that outside? When the sky turned red?"
                current_letter_index = 0
                first_dialogue_done = True

        # Draw the next dialogue
        if first_dialogue_done and current_letter_index < len(text_to_type):
            if current_time - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = current_time

        # After the first dialogue, display the response using dialogue.png
        if first_dialogue_done and current_letter_index >= len(text_to_type):
            if not second_dialogue_done and current_time - last_letter_time > 2000:  # Wait before showing next
                typed_text = ""  # Clear current text
                text_to_type = "Bystander: No? The sky was never red, it's always blue"
                current_letter_index = 0
                second_dialogue_done = True

        # Draw the second dialogue (using dialogue image for response)
        if second_dialogue_done and current_letter_index < len(text_to_type):
            if current_time - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = current_time

        # After the second dialogue, display the final dialogue
        if second_dialogue_done and current_letter_index >= len(text_to_type):
            if current_time - last_letter_time > 2000:  # Wait before showing next
                typed_text = ""  # Clear current text
                text_to_type = "Girl: Why does no one notice the strange things?"
                current_letter_index = 0
                third_dialogue_done = True

        # Draw the final dialogue
        if third_dialogue_done and current_letter_index < len(text_to_type):
            if current_time - last_letter_time > typing_speed:
                typed_text += text_to_type[current_letter_index]
                current_letter_index += 1
                last_letter_time = current_time

        # After the final dialogue, end the game after a short delay
        if third_dialogue_done and current_letter_index >= len(text_to_type):
            if not last_dialogue_done and current_time - last_letter_time > 2000:  # Wait 2 seconds after last dialogue
                last_dialogue_done = True  # Mark last dialogue as done
                # Add the end screen after the final dialogue
                pygame.time.wait(1000)  # Optional: Wait a bit before ending
                end_screen()  # Call the end screen function
                running = False  # Exit the loop to end the game

        pygame.display.update()
        CLOCK.tick(60)

    pygame.quit()

       
if __name__ == "__main__":
    main_menu()