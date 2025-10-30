import os

# --- Configuración ---
MAP_WIDTH = 10
MAP_HEIGHT = 6
PLAYER = "P"
GRASS = "G"
DIRT = "D"
AIR = " "

# --- Crear mundo inicial ---
world = [[AIR for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
# Capa de tierra
for x in range(MAP_WIDTH):
    world[MAP_HEIGHT-1][x] = GRASS
    if MAP_HEIGHT > 1:
        world[MAP_HEIGHT-2][x] = DIRT

# Posición del jugador
player_x = MAP_WIDTH // 2
player_y = MAP_HEIGHT - 2

def draw_world():
    os.system("cls" if os.name == "nt" else "clear")  # limpiar pantalla
    for y in range(MAP_HEIGHT):
        row = ""
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                row += PLAYER
            else:
                row += world[y][x]
        print(row)
    print("\nControles: w/a/s/d = mover, p = poner bloque, q = quitar bloque, x = salir")

# --- Juego ---
while True:
    draw_world()
    move = input(">>> ").lower()
    if move == "x":
        break
    elif move == "w" and player_y > 0:
        player_y -= 1
    elif move == "s" and player_y < MAP_HEIGHT-1:
        player_y += 1
    elif move == "a" and player_x > 0:
        player_x -= 1
    elif move == "d" and player_x < MAP_WIDTH-1:
        player_x += 1
    elif move == "p":
        if player_y > 0:
            world[player_y-1][player_x] = DIRT
    elif move == "q":
        if player_y > 0:
            world[player_y-1][player_x] = AIR
