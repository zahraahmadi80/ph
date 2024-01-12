import random
import time

# ابعاد صفحه بازی
WIDTH = 5
HEIGHT = 5

# تابع برای ایجاد صفحه بازی
def create_game_board():
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    return board

# تابع برای نمایش صفحه بازی
def display_game_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * (WIDTH * 2 - 1))

# تابع برای انتخاب یک خانه به صورت تصادفی
def select_random_cell():
    x = random.randint(0, WIDTH - 1)
    y = random.randint(0, HEIGHT - 1)
    return x, y

# تابع برای تمیز کردن یک خانه
def clean_cell(board, x, y):
    board[y][x] = ' '

# تابع برای انتقال جاروبرقی به یک خانه
def move_vacuum(board, x, y):
    board[y][x] = 'V'

# تابع برای بررسی وضعیت صفحه بازی
def check_game_state(board):
    for row in board:
        if 'D' in row:
            return False
    return True

# تابع برای شروع بازی
# تابع برای شروع بازی
def start_game():
    board = create_game_board()

    # انتخاب دو خانه با کثافت تصادفی
    dirty_x1, dirty_y1 = select_random_cell()
    dirty_x2, dirty_y2 = select_random_cell()
    board[dirty_y1][dirty_x1] = 'D'
    board[dirty_y2][dirty_x2] = 'D'

    # انتخاب خانه‌ای برای جاروبرقی به صورت تصادفی
    vacuum_x, vacuum_y = select_random_cell()
    board[vacuum_y][vacuum_x] = 'V'

    display_game_board(board)

    # بررسی وضعیت صفحه بازی تا زمانی که تمام خانه‌ها تمیز شوند
    while not check_game_state(board):
        time.sleep(1)  # تاخیر 1 ثانیه

        # جابجایی جاروبرقی به خانه‌ی کثیف
        clean_cell(board, vacuum_x, vacuum_y)
        vacuum_x, vacuum_y = dirty_x1, dirty_y1  # جابجایی جاروبرقی به خانه‌ی کثیف اول
        board[vacuum_y][vacuum_x] = 'V'
        display_game_board(board)

        time.sleep(1)  # تاخیر 1 ثانیه

        # جابجایی جاروبرقی به خانه‌ی کثیف دوم
        clean_cell(board, vacuum_x, vacuum_y)
        vacuum_x, vacuum_y = dirty_x2, dirty_y2  # جابجایی جاروبرقی به خانه‌ی کثیف دوم
        board[vacuum_y][vacuum_x] = 'V'
        display_game_board(board)

    print("تمام خانه‌ها تمیز شدند!")

# شروع بازی
start_game()
