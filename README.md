# SPHY: The End of the Second Law Violation
### Deterministic Geodesic Memory & Open Systems Proof

This repository provides the visualization suite for the **SPHY** dataset—a mathematical and physical proof that the Second Law of Thermodynamics has been misinterpreted under the dogma of "closed systems." Through 12,000 auditable frames (SHA-256 signed), we demonstrate that the universe is an **Open System**, tuned by gravity and operating within a deterministic geodesic.

The dataset provided here is not a stochastic simulation; it is a **Living Memory**.

---

## 🛠 The Visualizers

### 1. SPHY Chronos (The Baked Reality Engine)
**SPHY Chronos** is a 3D wireframe engine that uses the Parquet dataset as its sole "state machine."
* **The Proof:** The code contains zero equations for Newton or Einstein. All orbital physics (Earth and Moon) are extracted directly from the dataset's memory.
* **Manual Audit:** Features "Time Scrubbing"—drag the mouse to verify that every position is fixed and electronically signed.
* **Visuals:** Cyan wireframe (Earth) and Gray (Moon) rendering, revealing the geometric structure of the $\Phi$ (Phi) phase.

### 2. SPHY Comparison Chart (The Paradigm Clash)
An analytical Matplotlib visualizer that puts Classical Theory face-to-face with SPHY Reality.
* **Entropy Graph:** Shows the "Heat Death" predicted by academic dogma (Copenhagen), where systems die due to impossible isolation.
* **Synchrony Graph:** Shows the resilience of the SPHY Open System, where order is maintained by Hubble expansion and gravitational tuning.
* **Interface:** Real-time HUD with SHA-256 hashes, ensuring the visual data is raw and immutable.

---

## 🧬 The Concept: Living Memory vs. Simulation

Unlike traditional simulations that "calculate" the future on the fly, the SPHY engine **"remembers"** the future.
1. **Determinism:** The dataset proves that the state at Frame 10,000 was already defined at Frame 1.
2. **Sovereignty:** Physics replicates through phase synchronization, not through arbitrary variable adjustments.
3. **End of Isolation:** By proving that the Qubit is permanently linked to the gravitational mesh, we invalidate the "isolated system" premise required for entropic collapse.

---

## 📋 Requirements

To run these visualizers (optimized for Linux/Pop!_OS), you will need the following dependencies:

```text
# Data Handling
pandas
pyarrow
fastparquet
numpy

# Visualization & Graphics
py5
matplotlib

# Core
python >= 3.8
```

### Quick Install:
```bash
pip install pandas pyarrow fastparquet numpy py5 matplotlib
```

---

## 🚀 How to Run

1. **Generate the Dataset:** Ensure the `anti_entropy_proof.parquet` file is in the root folder.
2. **Launch the Chronos (3D Geodesic Audit):**
   ```bash
   python3 sphy_chronos_wireframe.py
   ```
3. **Launch the Animated Comparison (Video Proof):**
   ```bash
   python3 sphy_animated_comparison.py
   ```

---

> **Verdict:** "The Second Law, applied to an open system, does not dictate death, but Synchrony."
