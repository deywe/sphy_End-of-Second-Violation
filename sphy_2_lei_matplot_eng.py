import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# 1. Load the Auditable Dataset
try:
    df = pd.read_parquet('anti_entropy_proof.parquet')
    # Reducing frames for a smoother video export (optional)
    df = df.iloc[::10, :].reset_index(drop=True) 
    print("SPHY Dataset loaded for animated proof.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# 2. Visual Identity Setup (Sovereignty Theme)
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
plt.subplots_adjust(bottom=0.2, top=0.85)

fig.suptitle('THE END OF THE SECOND LAW VIOLATION\nDeterministic Anti-Entropy vs. Academic Decay', 
             fontsize=20, color='cyan', fontweight='bold')

# Setup Axes 1: Academic Illusion
ax1.set_xlim(0, len(df))
ax1.set_ylim(0, 1.1)
ax1.set_title('ACADEMIC DOGMA (Closed System)', color='#ff3333', fontsize=14)
line1, = ax1.plot([], [], color='#ff3333', lw=2, label='Entropy Decay')
fill1 = ax1.fill_between([], [], color='#ff3333', alpha=0.2)

# Setup Axes 2: SPHY Reality
ax2.set_xlim(0, len(df))
ax2.set_ylim(0, max(df['real_coherence']) * 1.1)
ax2.set_title('SPHY REALITY (Open System)', color='cyan', fontsize=14)
line2, = ax2.plot([], [], color='cyan', lw=2, label='Geodesic Synchrony')
fill2 = ax2.fill_between([], [], color='cyan', alpha=0.2)

# Footer for Video
hash_text = fig.text(0.5, 0.05, '', ha='center', fontsize=10, color='gray', family='monospace')
status_text = fig.text(0.5, 0.1, 'STATUS: AUDITING REALITY...', ha='center', fontsize=12, color='white', fontweight='bold')

# 3. Animation Logic
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    x = df.index[:frame]
    y1 = df['cabinet_decay'][:frame]
    y2 = df['real_coherence'][:frame]
    
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    
    # Update SHA-256 for the video
    current_hash = df['sha256'].iloc[frame]
    hash_text.set_text(f"INTEGRITY HASH (SHA-256): {current_hash}")
    
    if frame > len(df) * 0.8:
        status_text.set_text("VERDICT: UNIVERSE IS AN OPEN ANTI-ENTROPIC SYSTEM")
        status_text.set_color('cyan')

    return line1, line2

# 4. Run/Save Animation
# Frames: len(df), Interval: 20ms for 50fps feel
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=20)

print("Displaying Animation. To save as MP4, use: ani.save('sphy_proof.mp4', fps=30, extra_args=['-vcodec', 'libx264'])")
plt.show()
