import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        # Tamaño del tablero
        self.board_width = 400
        self.board_height = 400

        # Crear el lienzo para el tablero
        self.canvas = tk.Canvas(self.master, width=self.board_width, height=self.board_height, bg="black")
        self.canvas.pack()

        # Crear la serpiente
        self.snake = Snake(self.canvas, self.board_width, self.board_height)

        # Crear la comida
        self.food = Food(self.canvas, self.snake)
        
        # Inicializar puntaje
        self.score = 0
        self.max_score = self.load_max_score()
        
        # Velocidad inicial del juego
        self.speed = 300
        
        # Etiqueta para mostrar el puntaje
        self.score_label = tk.Label(self.master, text="Puntaje: {}".format(self.score))
        self.score_label.pack()
        
        # Etiqueta para mostrar el puntaje máximo
        self.max_score_label = tk.Label(self.master, text="Puntaje Máximo: {}".format(self.max_score))
        self.max_score_label.pack()

        # Dibujar el tablero
        self.draw_board()

        # Manejar la entrada del usuario
        self.master.bind("<KeyPress>", self.handle_keypress)

        # Iniciar el ciclo de juego
        self.game_loop()

    def draw_board(self):
        # Dibujar las líneas horizontales
        for i in range(20):
            self.canvas.create_line(0, i * 20, self.board_width, i * 20, fill="gray")

        # Dibujar las líneas verticales
        for i in range(20):
            self.canvas.create_line(i * 20, 0, i * 20, self.board_height, fill="gray")

        # Dibujar la serpiente
        self.snake.draw()

        # Dibujar la comida
        self.food.draw()

    def handle_keypress(self, event):
        directions = {"Up": "Up", "Down": "Down", "Left": "Left", "Right": "Right"}
        key = event.keysym
        if key in directions:
            self.snake.change_direction(directions[key])

    def game_loop(self):
        if self.snake.check_self_collision() or self.snake.check_boundary_collision(self.board_width, self.board_height):
            print("Game Over")
            self.end_game()
            return

        if self.snake.check_collision(self.food.position, "food"):
            self.snake.grow()
            self.canvas.delete("food")
            self.food.generate_position()
            self.food.draw()
            self.speed -= 20
        
            # Incrementar el puntaje cuando la serpiente come la fruta
            self.score += 1
            self.score_label.config(text="Puntaje: {}".format(self.score))

        self.snake.move()  # Mover la serpiente después de verificar si ha comido la comida
        self.snake.draw()
        self.master.after(self.speed, self.game_loop)
        
    def end_game(self):
        self.canvas.delete("food")
        
        # Guardar el puntaje máximo
        if self.score > self.max_score:
            self.max_score = self.score
            self.save_max_score()
        
        # Mostrar el menú de reinicio
        self.restart_frame = tk.Frame(self.master)
        self.restart_frame.pack(pady=20)

        # Botón para reiniciar el juego
        self.restart_button = tk.Button(self.restart_frame, text="Reiniciar", command=self.restart_game)
        self.restart_button.pack()
        
    def restart_game(self):
        # Eliminar el botón de reinicio
        self.restart_button.pack_forget()
        self.restart_frame.pack_forget()

        # Guardar el puntaje máximo actualizado
        self.save_max_score()

        # Cargar el puntaje máximo actualizado
        self.max_score = self.load_max_score()

        # Reiniciar el juego
        self.score = 0  # Reiniciar el puntaje
        self.snake = Snake(self.canvas, self.board_width, self.board_height)
        self.food = Food(self.canvas, self.snake)
        self.draw_board()
        self.game_loop()
        self.score_label.config(text="Puntaje: {}".format(self.score))
        self.max_score_label.config(text="Puntaje Máximo: {}".format(self.max_score))  # Actualizar la etiqueta del puntaje máximo
        self.speed = 300
        
    def save_max_score(self):
        # Guardar el puntaje máximo en un archivo o en la base de datos
        with open("max_score.txt", "w") as file:
            file.write(str(self.max_score))

    def load_max_score(self):
        # Cargar el puntaje máximo desde el archivo o la base de datos
        try:
            with open("max_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

class Snake:
    def __init__(self, canvas, board_width, board_height):  # Agregar board_width y board_height como argumentos
        self.canvas = canvas
        self.board_width = board_width  # Guardar board_width y board_height
        self.board_height = board_height
        self.segments = [(100, 100), (80, 100), (60, 100)]  # Posición inicial de la serpiente
        self.direction = "Right"  # Dirección inicial de la serpiente

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == "Right":
            new_head = (head_x + 20, head_y)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)

        self.segments = [new_head] + self.segments[:-1]

    def change_direction(self, new_direction):
        opposite_directions = {"Right": "Left", "Left": "Right", "Up": "Down", "Down": "Up"}
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def draw(self):
        self.canvas.delete("snake")
        for segment in self.segments:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green", tag="snake")

    def check_collision(self, position, obj_type):
        if obj_type == "food":
            collision_detected = any(segment == position for segment in self.segments)
            return collision_detected

    def grow(self):
        tail_x, tail_y = self.segments[-1]
        self.segments.append((tail_x, tail_y))

    def check_self_collision(self):
        self_collision_detected = len(set(self.segments)) != len(self.segments)
        return len(set(self.segments)) != len(self.segments)

    def check_boundary_collision(self, board_width, board_height):
        head_x, head_y = self.segments[0]
        return head_x < 0 or head_x >= board_width or head_y < 0 or head_y >= board_height

class Food:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        self.snake = snake
        self.position = (0, 0)  # Posición inicial de la comida
        self.generate_position()

    def generate_position(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake.segments:
                self.position = (x, y)
                break

    def draw(self):
        x, y = self.position
        self.canvas.create_oval(x, y, x + 20, y + 20, fill="red", tag="food")

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
