import pygame, sys
from board import Board
from constants import *
from cell import*
from button import*

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    #background_image = pygame.image.load("sudokuImage.png")  # Replace with the path to your image

    # Resize the background image to match the screen size
    #background_image = pygame.transform.scale(background_image, (900, 900))

    # Blit the background image onto the screen
    #screen.blit(background_image, (0, 0))

    title_surface = start_title_font.render("Welcome to Sudoku", 0, (PINK))
    title_rectangle = title_surface.get_rect(
        center=(HEIGHT // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    title_surface2 = start_title_font.render("Select Game Mode: ", 0, (PINK))
    title_rectangle2 = title_surface2.get_rect(
        center=(HEIGHT // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface2, title_rectangle2)

    diffEasy = button_font.render("Easy", 0, (255, 255, 255))
    diffMedium = button_font.render("Medium", 0, (255, 255, 255))
    diffHard = button_font.render("Hard", 0, (255, 255, 255))

    easy_surface = pygame.Surface((diffEasy.get_size()[0] + 20, diffEasy.get_size()[1] + 20))
    easy_surface.fill(GREEN)
    easy_surface.blit(diffEasy, (10, 10))

    medium_surface = pygame.Surface((diffMedium.get_size()[0] + 20, diffMedium.get_size()[1] + 20))
    medium_surface.fill(ORANGE)
    medium_surface.blit(diffMedium, (10, 10))

    hard_surface = pygame.Surface((diffHard.get_size()[0] + 20, diffHard.get_size()[1] + 20))
    hard_surface.fill(RED)
    hard_surface.blit(diffHard, (10, 10))

    # initialize buttons
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 +100))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 +100))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 +100))

    # draw the buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30 #how many cells are removed
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def game_over(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

     #background_image = pygame.image.load("sudokuImage.png")  # Replace with the path to your image

    # Resize the background image to match the screen size
     #background_image = pygame.transform.scale(background_image, (900, 900))

    # Blit the background image onto the screen
    # screen.blit(background_image, (0, 0))

    title_surface = start_title_font.render("Game Over", 0, (RED))
    title_rectangle = title_surface.get_rect(
        center=(HEIGHT // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

def you_win(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill((255, 255, 255))

    #background_image = pygame.image.load("sudokuImage.png")  # Replace with the path to your image

    # Resize the background image to match the screen size
     #background_image = pygame.transform.scale(background_image, (900, 900))

    # Blit the background image onto the screen
     #screen.blit(background_image, (0, 0))

    title_surface = start_title_font.render("You Win!", 0, (0,255,0))
    title_rectangle = title_surface.get_rect(
        center=(HEIGHT // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)



if __name__ == '__main__':
  # draws the screen
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("SudokuGame")
  main_run = True

  while main_run:
    game_run = True
    difficulty = draw_game_start(screen)
    game_board = Board(difficulty)
    print('difficult selected')
    game_board.draw()
    while game_run:

      restartB = Button(120, 50, (WIDTH//2-220), (HEIGHT+20), 'Restart', 30)
      resetB = Button(100, 50, (WIDTH//2-50), (HEIGHT+20), 'Reset', 30)
      exitB = Button(100, 50, (WIDTH//2+100), (HEIGHT+20), 'Exit', 30)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              exit()

          if event.type == pygame.MOUSEBUTTONDOWN:
              x, y = event.pos
              if y < HEIGHT:
                  row, col = game_board.click(x, y)
                  highlighted_cell = game_board.select(row, col)
                  game_board.draw()
                  if game_board.board_values[highlighted_cell.row][highlighted_cell.col] == 0:
                    game_board.draw_select(highlighted_cell)

              if restartB.is_clicked((x, y)):
                  print('Restart button clicked')
                  game_run = False
                  break
              elif resetB.is_clicked((x, y)):
                  print('Reset button clicked')
                  game_board.reset_to_original()
                  game_board.draw()
              elif exitB.is_clicked((x, y)):
                  print('Exit button clicked')
                  game_run = False
                  main_run = False

          if event.type == pygame.KEYDOWN:
              user_inpt = False
              if event.key == pygame.K_1:
                  highlighted_cell.sketched_value = 1
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_2:
                  highlighted_cell.sketched_value = 2
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_3:
                  highlighted_cell.sketched_value = 3
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_4:
                  highlighted_cell.sketched_value = 4
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_5:
                  highlighted_cell.sketched_value = 5
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_6:
                  highlighted_cell.sketched_value = 6
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_7:
                  highlighted_cell.sketched_value = 7
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_8:
                  highlighted_cell.sketched_value = 8
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True
              if event.key == pygame.K_9:
                  highlighted_cell.sketched_value = 9
                  game_board.draw()
                  game_board.draw_select(highlighted_cell)
                  pygame.display.update()
                  user_inpt == True

              #Checks if user has pressed the enter key and officially places the value in the board
              if event.key == pygame.K_RETURN:
                  if highlighted_cell.sketched_value != None:
                      game_board.place_number(highlighted_cell.sketched_value, highlighted_cell)
                      game_board.draw()
                      game_board.draw_select(highlighted_cell)
                      pygame.display.update()
              #Checks if the user has sketched in any values and displays them


              if event.key == pygame.K_BACKSPACE:  # removes number from currently selected cell
                  if highlighted_cell.value != 0 or highlighted_cell.sketched_value != None:
                      if game_board.board_values[highlighted_cell.row][highlighted_cell.col] == 0:
                          game_board.clear(highlighted_cell)
                          highlighted_cell.sketched_value = None
                          game_board.draw()
                          game_board.draw_select(highlighted_cell)
                          pygame.display.update()

                #test game over screen
              if event.key == pygame.K_g:
                  game_over(screen)
                  pygame.display.update()

              if event.key == pygame.K_w:
                  you_win(screen)
                  pygame.display.update()




              if game_board.is_full():
                  if game_board.check_board():
                      you_win(screen) #display winner screen
                  else:
                      game_over(screen) #display Game Over!







          # Draw buttons
      restartB.draw_button(screen, (255, 255, 255), (0, 0, 0,), (250,0,150))
      resetB.draw_button(screen, (255, 255, 255), (0, 0, 0,), (250,0,150))
      exitB.draw_button(screen, (255, 255, 255), (0, 0, 0,), (250,0,150))

      pygame.display.update()








