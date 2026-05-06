import py5
import pandas as pd
import numpy as np

class SphyChronosWire:
    def __init__(self):
        try:
            self.df = pd.read_parquet('anti_entropy_proof.parquet')
            print(f"SPHY Chronos Wireframe: {len(self.df)} frames prontos.")
        except Exception as e:
            print(f"Erro ao carregar dataset: {e}")
            self.df = None

        self.index = 0
        self.manual_mode = False
        self.phi = (1 + np.sqrt(5)) / 2

    def settings(self):
        py5.size(1200, 800, py5.P3D)

    def setup(self):
        py5.window_title("SPHY CHRONOS: WIREFRAME GEODESIC AUDIT")
        py5.text_size(14)

    def draw(self):
        py5.background(5) # Fundo quase negro para destacar as linhas
        
        if self.df is None: return

        # Controle de Scrubbing (Arrastar o tempo)
        if py5.is_mouse_pressed:
            self.manual_mode = True
            self.index = int(py5.remap(py5.mouse_x, 0, py5.width, 0, len(self.df) - 1))
            self.index = max(0, min(self.index, len(self.df) - 1))
        
        row = self.df.iloc[self.index]
        self.draw_hud(row)

        # Configuração do Espaço 3D
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2, -100)
        py5.rotate_x(py5.radians(-15))
        py5.rotate_y(py5.frame_count * 0.005)

        # --- TERRA: WIREFRAME CIANO ---
        py5.push_matrix()
        py5.rotate_y(self.index * 0.01) # Rotação síncrona com o tempo
        py5.no_fill()
        py5.stroke(0, 255, 255, 150) # Ciano vibrante
        py5.stroke_weight(0.5)
        py5.sphere_detail(20) # Detalhe da malha
        py5.sphere(80) 
        py5.pop_matrix()
        
        # --- LUA: WIREFRAME BRANCO/CINZA ---
        # A posição vem estritamente do dataset determinístico
        orbit_radius = 350
        angle = self.index * (self.phi * 0.01) 
        
        lx = orbit_radius * np.cos(angle)
        ly = orbit_radius * np.sin(angle)
        lz = 80 * np.sin(angle * self.phi) # Oscilação de fase
        
        py5.translate(lx, ly, lz)
        py5.rotate_y(self.index * 0.02)
        py5.stroke(200, 200, 200, 180) # Cinza lunar/Branco
        py5.sphere_detail(12)
        py5.sphere(25) 
        
        py5.pop_matrix()

        if not self.manual_mode:
            self.index = (self.index + 1) % len(self.df)

    def draw_hud(self, row):
        py5.fill(255)
        py5.text("SPHY CHRONOS | WIREFRAME MODE", 30, 40)
        py5.text(f"FRAME: {self.index}", 30, 65)
        py5.text(f"SHA-256 HASH: {row['sha256'][:40]}...", 30, 90)
        
        # Timeline
        py5.stroke(60)
        py5.line(30, 110, 400, 110)
        p = py5.remap(self.index, 0, len(self.df), 30, 400)
        py5.stroke(0, 255, 255)
        py5.line(30, 110, p, 110)

        status = "MANUAL AUDIT" if self.manual_mode else "DETERMINISTIC FLOW"
        py5.fill(0, 255, 255)
        py5.text(f"STATUS: {status}", 30, 140)

# --- EXECUÇÃO ---
visualizer = SphyChronosWire()

def settings(): visualizer.settings()
def setup(): visualizer.setup()
def draw(): visualizer.draw()

if __name__ == "__main__":
    py5.run_sketch()
