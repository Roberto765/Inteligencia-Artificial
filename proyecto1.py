import pygame
import heapq #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

# Configuración de Pygame
ANCHO_VENTANA = 500
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Algoritmo A*")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NARANJA = (255, 165, 0)
PURPURA = (128, 0, 128)

class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila
        self.col = col
        self.x = fila * ancho
        self.y = col * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas
        self.vecinos = [] #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
    
    def get_pos(self):
        return self.fila, self.col

    def es_pared(self):
        return self.color == NEGRO

    def es_inicio(self):
        return self.color == NARANJA

    def es_fin(self):
        return self.color == PURPURA

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = PURPURA

    def hacer_camino(self):
        self.color = VERDE

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))

    def actualizar_vecinos(self, grid): #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
        self.vecinos = [] 
        movimientos = [
            (-1, 0), (1, 0), (0, -1), (0, 1), # Arriba, Abajo, Izquierda, Derecha
            (-1, -1), (-1, 1), (1, -1), (1, 1) # Diagonales
        ]
        for dx, dy in movimientos:
            nueva_fila, nueva_col = self.fila + dx, self.col + dy
            if 0 <= nueva_fila < self.total_filas and 0 <= nueva_col < self.total_filas:
                if not grid[nueva_fila][nueva_col].es_pared():
                    self.vecinos.append(grid[nueva_fila][nueva_col])#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

def crear_grid(filas, ancho):#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
    grid = []
    ancho_nodo = ancho // filas
    for i in range(filas):
        grid.append([])
        for j in range(filas):
            nodo = Nodo(i, j, ancho_nodo, filas)
            grid[i].append(nodo)
    return grid #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

def dibujar_grid(ventana, filas, ancho):
    ancho_nodo = ancho // filas
    for i in range(filas):
        pygame.draw.line(ventana, GRIS, (0, i * ancho_nodo), (ancho, i * ancho_nodo))
        for j in range(filas):
            pygame.draw.line(ventana, GRIS, (j * ancho_nodo, 0), (j * ancho_nodo, ancho))

def dibujar(ventana, grid, filas, ancho):
    ventana.fill(BLANCO)
    for fila in grid:
        for nodo in fila:
            nodo.dibujar(ventana)
    dibujar_grid(ventana, filas, ancho) 
    pygame.display.update()

def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

def h(nodo1, nodo2): #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
    x1, y1 = nodo1.get_pos()
    x2, y2 = nodo2.get_pos()
    return abs(x1 - x2) + abs(y1 - y2) #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

def reconstruir_camino(came_from, actual): #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
    while actual in came_from:
        actual = came_from[actual]
        actual.hacer_camino() #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

def algoritmo_a_estrella(dibujar, grid, inicio, fin): #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, inicio))
    came_from = {}
    g_score = {nodo: float("inf") for fila in grid for nodo in fila}
    g_score[inicio] = 0
    f_score = {nodo: float("inf") for fila in grid for nodo in fila}
    f_score[inicio] = h(inicio, fin)

    open_set_hash = {inicio}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        actual = heapq.heappop(open_set)[2]
        open_set_hash.remove(actual)

        if actual == fin:
            reconstruir_camino(came_from, fin)
            return True
        
        for vecino in actual.vecinos:
            temp_g_score = g_score[actual] + 1

            if temp_g_score < g_score[vecino]:
                came_from[vecino] = actual
                g_score[vecino] = temp_g_score
                f_score[vecino] = temp_g_score + h(vecino, fin)
                if vecino not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[vecino], count, vecino))
                    open_set_hash.add(vecino)
        
        dibujar()

    return False #ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA#ESTA

def main(ventana, ancho):
    FILAS = 20
    grid = crear_grid(FILAS, ancho)

    inicio = None
    fin = None

    corriendo = True
    ejecutando = False

    while corriendo:
        dibujar(ventana, grid, FILAS, ancho)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if pygame.mouse.get_pressed()[0]:  # Click izquierdo
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                if not inicio and nodo != fin:
                    inicio = nodo
                    inicio.hacer_inicio()
                elif not fin and nodo != inicio:
                    fin = nodo
                    fin.hacer_fin()
                elif nodo != fin and nodo != inicio:
                    nodo.hacer_pared()

            elif pygame.mouse.get_pressed()[2]:  # Click derecho
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                nodo.color = BLANCO
                if nodo == inicio:
                    inicio = None
                elif nodo == fin:
                    fin = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and inicio and fin and not ejecutando:
                    for fila in grid:
                        for nodo in fila:
                            nodo.actualizar_vecinos(grid)
                    algoritmo_a_estrella(lambda: dibujar(ventana, grid, FILAS, ancho), grid, inicio, fin)
                    ejecutando = True

                if event.key == pygame.K_c:
                    inicio = None
                    fin = None
                    grid = crear_grid(FILAS, ancho)
                    ejecutando = False

    esperando_cierre = True
    while esperando_cierre:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando_cierre = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                esperando_cierre = False

    pygame.quit()

main(VENTANA, ANCHO_VENTANA)
