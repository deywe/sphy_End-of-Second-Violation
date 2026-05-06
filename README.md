--

# SPHY: The End of the Second Law Violation
### Deterministic Geodesic Memory & Open Systems Proof

Este repositório contém as ferramentas de visualização para o dataset **SPHY**, uma prova matemática e física de que a Segunda Lei da Termodinâmica tem sido mal interpretada sob o dogma de sistemas fechados. Através de 12.000 frames auditáveis (SHA-256), demonstramos que o universo é um sistema aberto, sintonizado pela gravidade e operando em uma geodésia determinística.

O dataset aqui contido não é uma simulação estocástica; é uma **Memória Viva**.

---

## 🛠 Os Visualizadores

### 1. SPHY Chronos (The Baked Reality Engine)
O **SPHY Chronos** é um visualizador de malha (wireframe) que utiliza o dataset Parquet como seu único motor de estado.
*   **A Prova:** O código não contém equações de Newton ou Einstein. Toda a física orbital (Terra e Lua) é extraída diretamente da memória do dataset.
*   **Auditoria Manual:** Permite o *scrubbing* (arrastar o tempo) para verificar que cada posição é fixa e assinada eletronicamente.
*   **Visual:** Renderização em wireframe ciano (Terra) e cinza (Lua), revelando a estrutura geométrica da fase $\Phi$.

### 2. SPHY Comparison Chart (The Paradigm Clash)
Um visualizador analítico em Matplotlib que coloca a teoria clássica frente a frente com a Realidade SPHY.
*   **Gráfico de Entropia:** Mostra o decaimento previsto pela academia (Copenhagen), onde o sistema morre por isolamento.
*   **Gráfico de Sincronia:** Mostra a resiliência do sistema aberto SPHY, onde a ordem é mantida pela expansão de Hubble e sintonização gravitacional.
*   **Interface:** HUD em tempo real com hashes SHA-256, garantindo que os dados visualizados são os dados brutos e imutáveis.

---

## 🧬 O Conceito: Memória Viva vs. Simulação

Diferente das simulações tradicionais que "calculam" o futuro, o motor SPHY **"lembra"** do futuro. 
1. **Determinismo:** O dataset prova que o estado no frame 10.000 já estava definido no frame 1.
2. **Soberania:** A física se replica através da sintonização de fase, e não por ajustes arbitrários de variáveis.
3. **Fim do Isolamento:** Ao provar que o Qubit está sempre ligado à malha gravitacional, invalidamos a premissa de "sistema isolado" necessária para o colapso entrópico.

---

## 📋 Requirements

Para rodar os visualizadores no seu ambiente (recomendado: Linux/Pop!_OS), você precisará das seguintes dependências:

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

### Instalação rápida:
```bash
pip install pandas pyarrow fastparquet numpy py5 matplotlib
```

---

## 🚀 Como Executar

1. **Gere o Dataset:** Certifique-se de que o arquivo `anti_entropy_proof.parquet` está na raiz da pasta.
2. **Execute o Chronos (3D Audit):**
   ```bash
   python3 sphy_chronos_wireframe.py
   ```
3. **Execute a Comparação Animada (Video Proof):**
   ```bash
   python3 sphy_animated_comparison.py
   ```

---

> **Veredito:** "A Segunda Lei, aplicada a um sistema aberto, não dita morte, mas Sincronia."
```
