import random

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.has_moved = False
    
    def get_symbol(self):
        return "?"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return False


class Pawn(Piece): # пешка
    def get_symbol(self):
        return "P" if self.color == "white" else "p"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        direction = -1 if self.color == "white" else 1
        start_row_condition = 6 if self.color == "white" else 1
        
        if start_col == end_col:
            if end_row == start_row + direction:
                return board.get_piece(end_row, end_col) is None
            elif end_row == start_row + 2 * direction and not self.has_moved:
                middle_row = start_row + direction
                return (board.get_piece(middle_row, start_col) is None and 
                        board.get_piece(end_row, end_col) is None)
        
        elif abs(end_col - start_col) == 1 and end_row == start_row + direction:
            target = board.get_piece(end_row, end_col)
            return target is not None and target.color != self.color
        
        return False


class Rook(Piece): # ладья
    def get_symbol(self):
        return "R" if self.color == "white" else "r"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if start_row != end_row and start_col != end_col:
            return False
        
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board.get_piece(start_row, col) is not None:
                    return False
        else:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board.get_piece(row, start_col) is not None:
                    return False
        
        target = board.get_piece(end_row, end_col)
        return target is None or target.color != self.color


class Knight(Piece): # конь
    def get_symbol(self):
        return "N" if self.color == "white" else "n"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        return False


class Bishop(Piece): # слон
    def get_symbol(self):
        return "B" if self.color == "white" else "b"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if row_diff != col_diff:
            return False
        
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        
        row = start_row + row_step
        col = start_col + col_step
        while row != end_row:
            if board.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        
        target = board.get_piece(end_row, end_col)
        return target is None or target.color != self.color


class Queen(Piece): # королева
    def get_symbol(self):
        return "Q" if self.color == "white" else "q"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if start_row == end_row or start_col == end_col:
            if start_row == end_row:
                step = 1 if end_col > start_col else -1
                for col in range(start_col + step, end_col, step):
                    if board.get_piece(start_row, col) is not None:
                        return False
            else:
                step = 1 if end_row > start_row else -1
                for row in range(start_row + step, end_row, step):
                    if board.get_piece(row, start_col) is not None:
                        return False
            
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        elif row_diff == col_diff:
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            
            row = start_row + row_step
            col = start_col + col_step
            while row != end_row:
                if board.get_piece(row, col) is not None:
                    return False
                row += row_step
                col += col_step
            
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        return False


class King(Piece): # король
    def get_symbol(self):
        return "K" if self.color == "white" else "k"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if row_diff <= 1 and col_diff <= 1:
            target = board.get_piece(end_row, end_col)
            if target and target.color == self.color:
                return False
            
            original_piece = board.get_piece(end_row, end_col)
            board.set_piece(end_row, end_col, self)
            board.set_piece(start_row, start_col, None)
            
            in_check = board.is_check(self.color)
            
            board.set_piece(start_row, start_col, self)
            board.set_piece(end_row, end_col, original_piece)
            
            return not in_check
        
        return False


# ____________________ Доп задание _____________________________
# 1 - 3 оригинальные фигуры с уникальной логикой перемещения

class Flamingo(Piece):
    def get_symbol(self):
        return "F" if self.color == "white" else "f"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if (row_diff == 3 and col_diff == 1) or (row_diff == 1 and col_diff == 3):
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        return False


class Hippo(Piece):
    def get_symbol(self):
        return "H" if self.color == "white" else "h"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if row_diff == 2 and col_diff == 0:
            step = 1 if end_row > start_row else -1
            middle_row = start_row + step
            if board.get_piece(middle_row, start_col) is not None:
                return False
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        elif row_diff == 0 and col_diff == 2:
            step = 1 if end_col > start_col else -1
            middle_col = start_col + step
            if board.get_piece(start_row, middle_col) is not None:
                return False
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        elif row_diff == 2 and col_diff == 2:
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            middle_row = start_row + row_step
            middle_col = start_col + col_step
            if board.get_piece(middle_row, middle_col) is not None:
                return False
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        return False


class Oxelot(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.can_fly = True
    
    def get_symbol(self):
        return "O" if self.color == "white" else "o"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        if row_diff == 0 and col_diff == 0:
            return False
        
        if row_diff <= 2 and col_diff <= 2:
            target = board.get_piece(end_row, end_col)
            return target is None or target.color != self.color
        
        return False

# ___________________ конец допа ___________________


# ___________________ доп задание ______________________
# 2 - шашки
class Checker(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.is_king = False
    
    def get_symbol(self):
        if self.is_king:
            return "W" if self.color == "white" else "B"
        return "w" if self.color == "white" else "b"
    
    def make_king(self):
        self.is_king = True
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)
        
        if col_diff != 1:
            return False
        
        if not self.is_king:
            if self.color == "white":
                if row_diff != -1:
                    return False
            else:
                if row_diff != 1:
                    return False
        
        target = board.get_piece(end_row, end_col)
        if target is not None:
            return False
        
        return True
    
    def is_valid_capture(self, start_row, start_col, end_row, end_col, board):
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)
        
        if col_diff != 2:
            return False
        
        if not self.is_king:
            if self.color == "white":
                if row_diff != -2:
                    return False
            else:
                if row_diff != 2:
                    return False
        
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        target = board.get_piece(mid_row, mid_col)
        
        if target is None or target.color == self.color:
            return False
        
        end_target = board.get_piece(end_row, end_col)
        if end_target is not None:
            return False
        
        return True


class CheckersBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.current_turn = "white"
        self.must_capture = False
        self.capture_positions = []
    
    def setup_pieces(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker("black", row, col)
        
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker("white", row, col)
    
    def display(self):
        print("  a b c d e f g h")
        for row in range(8):
            print(8 - row, end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    print(piece.get_symbol(), end=" ")
                else:
                    if (row + col) % 2 == 0:
                        print("#", end=" ")
                    else:
                        print(".", end=" ")
            print(8 - row)
        print("  a b c d e f g h")
    
    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def set_piece(self, row, col, piece):
        self.board[row][col] = piece
        if piece:
            piece.row = row
            piece.col = col
    
    def get_all_captures(self, color):
        captures = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == color:
                    for dr in [-2, 2]:
                        for dc in [-2, 2]:
                            end_row = row + dr
                            end_col = col + dc
                            if 0 <= end_row < 8 and 0 <= end_col < 8:
                                if piece.is_valid_capture(row, col, end_row, end_col, self):
                                    captures.append((row, col, end_row, end_col))
        return captures
    
    def has_any_captures(self, color):
        return len(self.get_all_captures(color)) > 0
    
    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece(start_row, start_col)
        if not piece:
            return False
        
        if piece.color != self.current_turn:
            return False
        
        target = self.get_piece(end_row, end_col)
        if target is not None:
            return False
        
        if self.must_capture:
            if (start_row, start_col, end_row, end_col) not in self.capture_positions:
                return False
        
        if abs(end_col - start_col) == 2:
            if piece.is_valid_capture(start_row, start_col, end_row, end_col, self):
                mid_row = (start_row + end_row) // 2
                mid_col = (start_col + end_col) // 2
                self.set_piece(mid_row, mid_col, None)
                
                self.set_piece(end_row, end_col, piece)
                self.set_piece(start_row, start_col, None)
                
                if (piece.color == "white" and end_row == 0) or (piece.color == "black" and end_row == 7):
                    piece.make_king()
                
                new_captures = []
                for dr in [-2, 2]:
                    for dc in [-2, 2]:
                        new_end_row = end_row + dr
                        new_end_col = end_col + dc
                        if 0 <= new_end_row < 8 and 0 <= new_end_col < 8:
                            if piece.is_valid_capture(end_row, end_col, new_end_row, new_end_col, self):
                                new_captures.append((end_row, end_col, new_end_row, new_end_col))
                
                if new_captures:
                    self.must_capture = True
                    self.capture_positions = new_captures
                    return True
                else:
                    self.must_capture = False
                    self.capture_positions = []
                    self.current_turn = "black" if self.current_turn == "white" else "white"
                    return True
        
        elif abs(end_col - start_col) == 1:
            if piece.is_valid_move(start_row, start_col, end_row, end_col, self):
                if self.has_any_captures(self.current_turn):
                    return False
                
                self.set_piece(end_row, end_col, piece)
                self.set_piece(start_row, start_col, None)
                
                if (piece.color == "white" and end_row == 0) or (piece.color == "black" and end_row == 7):
                    piece.make_king()
                
                self.must_capture = False
                self.capture_positions = []
                self.current_turn = "black" if self.current_turn == "white" else "white"
                return True
        
        return False
    
    def has_moves(self, color):
        if self.has_any_captures(color):
            return len(self.get_all_captures(color)) > 0
        
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == color:
                    for dr in [-1, 1]:
                        for dc in [-1, 1]:
                            end_row = row + dr
                            end_col = col + dc
                            if 0 <= end_row < 8 and 0 <= end_col < 8:
                                if piece.is_valid_move(row, col, end_row, end_col, self):
                                    return True
        return False
    
    def count_pieces(self, color):
        count = 0
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == color:
                    count += 1
        return count
    
    def is_game_over(self):
        if not self.has_moves("white") or self.count_pieces("white") == 0:
            return "black"
        if not self.has_moves("black") or self.count_pieces("black") == 0:
            return "white"
        return None


class CheckersGame:
    def __init__(self):
        self.board = CheckersBoard()
    
    def parse_position(self, pos):
        if len(pos) != 2:
            return None
        col_char = pos[0].lower()
        row_char = pos[1]
        
        if col_char not in "abcdefgh" or row_char not in "12345678":
            return None
        
        col = ord(col_char) - ord('a')
        row = 8 - int(row_char)
        return (row, col)
    
    def run(self):
        print("ШАШКИ")
        print("Правила: обычные шашки, дамка ходит на любое расстояние по диагонали")
        print("Для хода вводите: e2 e4")
        print("Для выхода введите: exit")
        
        while True:
            self.board.display()
            
            winner = self.board.is_game_over()
            if winner:
                print(f"Победили {winner}!")
                break
            
            if self.board.has_any_captures(self.board.current_turn):
                print("Обязательное взятие!")
            
            print(f"Ход: {self.board.current_turn}")
            
            start_input = input("Введите координаты шашки: ")
            if start_input.lower() == "exit":
                break
            
            start_pos = self.parse_position(start_input)
            if not start_pos:
                print("Неверный формат!")
                continue
            
            start_row, start_col = start_pos
            piece = self.board.get_piece(start_row, start_col)
            
            if not piece:
                print("Здесь нет шашки!")
                continue
            
            if piece.color != self.board.current_turn:
                print("Сейчас не ваш ход!")
                continue
            
            end_input = input("Введите координаты хода: ")
            end_pos = self.parse_position(end_input)
            if not end_pos:
                print("Неверный формат!")
                continue
            
            end_row, end_col = end_pos
            
            if self.board.move_piece(start_row, start_col, end_row, end_col):
                print("Ход выполнен!")
            else:
                print("Невозможный ход!")
# ______________________ конец допа _________________-

# _____________ доп задание ________________ 
# история ходов и откат хода назад

# класс для хранения информации о ходе
# class Move:
    # def __init__(self, start_row, start_col, end_row, end_col, piece, captured_piece=None):
        # self.start_row = start_row
        # self.start_col = start_col
        # self.end_row = end_row
        # self.end_col = end_col
        # self.piece = piece
        # self.captured_piece = captured_piece
        # self.piece_has_moved = piece.has_moved if piece else False
    
    # def get_coordinates_string(self):
        # start_file = chr(ord('a') + self.start_col)
        # start_rank = str(8 - self.start_row)
        # end_file = chr(ord('a') + self.end_col)
        # end_rank = str(8 - self.end_row)
        # return f"{start_file}{start_rank} -> {end_file}{end_rank}"

# _____________________ подсветка фигур под боем и шаха ____________________
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.current_turn = "white"
        # self.under_attack = [[False for _ in range(8)] for _ in range(8)] 
        # под прицелом
        # self.move_history = []
        # для информации истории ходов
    
    def setup_pieces(self):
        for i in range(8):
            self.board[1][i] = Pawn("black", 1, i)
            self.board[6][i] = Pawn("white", 6, i)
        
        pieces_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        
        for i, piece_class in enumerate(pieces_order):
            self.board[0][i] = piece_class("black", 0, i)
            self.board[7][i] = piece_class("white", 7, i)
        
        # ______________ Добавление новых фигур на доску (для 1) ________________
        # self.board[0][2] = Flamingo("black", 0, 2)
        # self.board[7][2] = Flamingo("white", 7, 2)
        # self.board[0][5] = Hippo("black", 0, 5)
        # self.board[7][5] = Hippo("white", 7, 5)
        # self.board[0][3] = Oxelot("black", 0, 3)
        # self.board[7][3] = Oxelot("white", 7, 3)
    
    def display(self):

        # self.update_under_attack() 
        # для списка фигур под боем

        print("  a b c d e f g h")
        for row in range(8):
            print(8 - row, end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    print(piece.get_symbol(), end=" ")

                    # для фигуры под боем в квадратных скобках убираем строчку выше и добавляем:
                    # symbol = piece.get_symbol()
                    # if self.under_attack[row][col]:
                        # print(f"[{symbol}]", end=" ")
                    # else:
                        # print(f" {symbol} ", end=" ")

                else:
                    print(".", end=" ")
            print(8 - row)
        print("  a b c d e f g h")

    # новый метод, который обновляет under_attack, где хранятся фигуры под прицелом
    # def update_under_attack(self):
        # self.under_attack = [[False for _ in range(8)] for _ in range(8)]
        
        # for row in range(8):
            # for col in range(8):
                # piece = self.get_piece(row, col)
                # if piece:
                    # for end_row in range(8):
                        # for end_col in range(8):
                            # if piece.is_valid_move(row, col, end_row, end_col, self):
                                # self.under_attack[end_row][end_col] = True
    
    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def set_piece(self, row, col, piece):
        self.board[row][col] = piece
        if piece:
            piece.row = row
            piece.col = col
    
    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece(start_row, start_col)
        if not piece:
            return False
        
        if piece.color != self.current_turn:
            return False
        
        target = self.get_piece(end_row, end_col)
        if target and target.color == piece.color:
            return False
        
        if piece.is_valid_move(start_row, start_col, end_row, end_col, self):
            # сохраняем информацию о коде для отката
            # captured_piece = target
            # move = Move(start_row, start_col, end_row, end_col, piece, captured_piece)
            self.set_piece(end_row, end_col, piece)
            self.set_piece(start_row, start_col, None)
            # сохраняем код в историю
            # self.move_history.append(move)
            # обновляеи флаг has_moved для фигуры
            # piece.has_moved = True
            self.current_turn = "black" if self.current_turn == "white" else "white"
            return True
        return False
    
    # метод для отката хода
    # def undo_move(self):
        # if not self.move_history:
            # print("Нет ходов для отката!")
            # return False
        # последний ход из истории
        # last_move = self.move_history.pop()
        # восстановление флага has_moved для фигуры
        # last_move.piece.has_moved = last_move.piece_has_moved
        # перемещение фигуры обратно
        # self.set_piece(last_move.start_row, last_move.start_col, last_move.piece)
        # self.set_piece(last_move.end_row, last_move.end_col, None)
        # если была съедена фигура, восстанавливаем
        # if last_move.captured_piece:
            # self.set_piece(last_move.end_row, last_move.end_col, last_move.captured_piece)
        # меняем ход обратно
        # self.current_turn = "black" if self.current_turn == "white" else "white"
        # print(f"Откат выполнен! Отменён ход: {last_move.get_coordinates_string()}")
        # return True
    
    def is_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        
        opponent_color = "black" if color == "white" else "white"
        
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == opponent_color:
                    if piece.is_valid_move(row, col, king_pos[0], king_pos[1], self):
                        return True
        return False
    
    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and isinstance(piece, King) and piece.color == color:
                    return (row, col)
        return None
    
    def has_moves(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == color:
                    for end_row in range(8):
                        for end_col in range(8):
                            if piece.is_valid_move(row, col, end_row, end_col, self):
                                target = self.get_piece(end_row, end_col)
                                if target and target.color == color:
                                    continue
                                start_piece = self.get_piece(row, col)
                                end_piece = self.get_piece(end_row, end_col)
                                
                                self.set_piece(end_row, end_col, start_piece)
                                self.set_piece(row, col, None)
                                
                                in_check = self.is_check(color)
                                
                                self.set_piece(row, col, start_piece)
                                self.set_piece(end_row, end_col, end_piece)
                                
                                if not in_check:
                                    return True
        return False
    
    def is_checkmate(self, color):
        if not self.is_check(color):
            return False
        return not self.has_moves(color)
    
    def is_stalemate(self, color):
        if self.is_check(color):
            return False
        return not self.has_moves(color)


class Game:
    def __init__(self):
        self.board = Board()
    
    def parse_position(self, pos):
        if len(pos) != 2:
            return None
        col_char = pos[0].lower()
        row_char = pos[1]
        
        if col_char not in "abcdefgh" or row_char not in "12345678":
            return None
        
        col = ord(col_char) - ord('a')
        row = 8 - int(row_char)
        return (row, col)
    
    def run(self):
        print("ШАХМАТЫ")
        # print("Фигуры в [скобках] находятся под боем")
        # print("ШАХ выделяется отдельной строкой")
        # print("Доп. команда:")
        # print("'undo' - отменить последний ход")
        
        while True:
            self.board.display()

            # is_check_now = self.board.is_check(self.board.current_turn)
            
            if self.board.is_checkmate(self.board.current_turn):
                winner = "черные" if self.board.current_turn == "white" else "белые"
                print(f"мат, победили {winner}")
                break
            
            if self.board.is_stalemate(self.board.current_turn):
                print("пат, ничья")
                break
            
            if self.board.is_check(self.board.current_turn):
                print("шах")

            # if is_check_now:
                # print("_" * 20)
                # print("ШАХ КОРОЛЮ")
                # print("_" * 20)
            
            print(f"ход {self.board.current_turn}")
            
            start_input = input("Введите координаты фигуры, которую хотите переместить (например, e2): ")
            if start_input.lower() == "exit":
                break

            # if start_input.lower() == "undo":
                # self.board.undo_move()
                # continue
            
            start_pos = self.parse_position(start_input)
            if not start_pos:
                print("неверный формат")
                continue
            
            start_row, start_col = start_pos
            piece = self.board.get_piece(start_row, start_col)
            
            if not piece:
                print("здесь нет фигуры")
                continue
            
            if piece.color != self.board.current_turn:
                print("сейчас не ваш ход")
                continue
            
            end_input = input("введите координаты хода: куда переместить фигуру (например, e4): ")
            
            # if end_input.lower() == "undo":
                # self.board.undo_move()
                # continue

            end_pos = self.parse_position(end_input)
            if not end_pos:
                print("неверный формат")
                continue
            
            end_row, end_col = end_pos
            
            if self.board.move_piece(start_row, start_col, end_row, end_col):
                print("ход выполнен")
            else:
                print("невозможный ход")

if __name__ == "__main__":
    print("выберите:")
    print("1 - шахматы")
    print("2 - шашки")
    
    choice = input("Ваш выбор: ")
    
    if choice == "1":
        game = Game()
        game.run()
    else:
        game = CheckersGame()
        game.run()

# Сделанные допы: 1, 2, 5, 7

# 1
# 3 новые фигуры:
# Flamingo — ходит как конь, но на 3 клетки по одной оси и на 1 по другой (3+1, 1+3). Символы: C (белый), c (черный).
# Hippo — ходит на 2 клетки по горизонтали, вертикали или диагонали, но не может перепрыгивать через фигуры. Символы: E (белый), e (черный).
# Oxelot — ходит на любую клетку в радиусе 2 клеток (включая диагонали). Символы: D (белый), d (черный).

# 2
# Шахматы становятся шашками:
# Класс Checker — наследуется от Piece, представляет шашку. Обычная шашка ходит на одну клетку вперед по диагонали 
# Дама (символы W/B) ходит на любое расстояние по диагонали и ест противника (несколько шашек за ход)
# Класс CheckersBoard — аналог шахматной доски для шашек. Расстановка шашек на темных клетках (первые 3 ряда для черных, последние 3 для белых)
# если есть возможность съесть шашку, игрок обязан это сделать, шашка становится дамкой при достижении последней горизонтали
# Класс CheckersGame — управление игровым процессом в шашки. окончание игры (нет ходов или нет шашек), отображение доски с темными клетками (#)
# при запуске позволяет выбрать между шахматами и шашками

# 5 - 

# 7 - под прицелом
# пример:
# Допустим, белый конь на f3 (координаты) находится под боем черной пешки:
# 3 .  .  .  .  . [N] .  . 3
# ____________________
# !!! ШАХ КОРОЛЮ !!!
# ____________________
# МАТ! Победили white!
# ПАТ! Ничья!
