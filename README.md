# Car Troubleshooting Expert System

![Python 3](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-00599C?style=for-the-badge)
![Rule-Based AI](https://img.shields.io/badge/AI-Rule_Based_Expert_System-FF6F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

## Executive Overview
Automotive troubleshooting often requires navigating a complex matrix of interrelated mechanical and electrical symptoms. This project introduces a **Rule-Based Expert System** engineered in Python. It acts as an interactive diagnostic agent, capturing user-observed symptoms and pushing them through a deterministic forward-chaining inference engine to isolate vehicle malfunctions and recommend corrective maintenance actions.

> [!WARNING]
> **Automotive Safety Hazard**
> Diagnostics recommended by this system may require interacting with high-amperage 12V lead-acid batteries, highly pressurized high-temperature coolant systems, and volatile fuel vapors. Always disconnect the negative battery terminal before servicing electrical components, and NEVER open a radiator cap while the engine is hot.

## System Highlights
- **Multi-Subsystem Diagnostic Coverage**: Evaluates Starter/Ignition, Fuel Delivery, Cooling/Thermal, and Electrical systems.
- **Deterministic Forward-Chaining Algorithm**: Uses rigid, traceable logic rather than stochastic machine learning, ensuring safety-critical recommendations are predictable and verifiable.
- **Cross-Platform GUI**: Built with standard `tkinter` for seamless execution across Windows, macOS, and Linux without heavy third-party dependencies.
- **Standalone Binary Support**: Capable of being compiled into a standalone `.exe` using PyInstaller for use in garage environments without a Python runtime.

## System Architecture & Diagnostic Decision Tree

mermaid
flowchart TD
    UI["User Interface / Checkboxes"] -->|Selects Symptoms| FCE["Forward-Chaining Inference Engine"]
    
    KB["(Knowledge Base / Rule Matrix)"] -->|Provides Rules| FCE
    
    FCE -->|Rule Match: No crank + Click| D1["Diagnosis: Dead Battery / Starter Relay"]
    FCE -->|Rule Match: Sputter + Crank| D2["Diagnosis: Fuel Delivery Failure"]
    FCE -->|Rule Match: Steam + Overheat| D3["Diagnosis: Coolant Leak / Head Gasket"]
    FCE -->|Rule Match: Battery Drain| D4["Diagnosis: Parasitic Electrical Draw"]
    
    D1 --> REC["Recommend Corrective Action"]
    D2 --> REC
    D3 --> REC
    D4 --> REC


## Theoretical & Mathematical Model

### Propositional Logic & Inference
The expert system operates on classical propositional logic using **Modus Ponens**. Given a rule $P \to Q$ (If $P$ then $Q$), and the assertion of premise $P$, the system deduces $Q$.
$$ P \land (P \to Q) \vdash Q $$

In the forward-chaining algorithm, the premise $P$ is a logical conjunction ($\bigwedge$) of specific symptoms $S_i$ required by a diagnostic rule $D_k$:
$$ \left( \bigwedge_{"i=1"}^{n} S_i \right) \implies D_k $$
If the set of user-selected symptoms is a superset of the rule's required symptoms, the rule fires. 

### Algorithmic Complexity
The time complexity of the forward-chaining evaluation is bounded by $\mathcal{"O"}(R \times S)$, where $R$ is the total number of rules in the knowledge base and $S$ is the number of active user symptoms. Because automotive rules are highly structured, the evaluation is practically instantaneous $\mathcal{"O"}(1)$.

## System Requirements & Prerequisites
- **Python 3.8+** (No external libraries required for the source script).
- Operating System: Windows 10/11, macOS, or Linux (requires standard Tcl/Tk system libraries).

## Repository Layout Tree
```text
.
├── docs/                  # Original academic RTF report detailing the system logic
├── releases/              # Historical compiled standalone executable (PyInstaller)
├── src/                   # Reconstructed Python source code and GUI implementation
└── _archive/              # PyInstaller build caches and legacy files
```

## Step-by-Step Execution Guide

### 1. Running from Source
1. Clone the repository and navigate to the project directory.
2. Open a terminal or command prompt.
3. Execute the script:
   ```bash
   python src/car_troubleshooter_gui.py
   ```
4. Select the observed symptoms in the GUI and click **Run Diagnostics**.

### 2. Compiling a Standalone Executable (Windows)
If you wish to compile the system for use on a shop computer without Python:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed src/car_troubleshooter_gui.py
```
The resulting `car_troubleshooter_gui.exe` will be located in the `dist/` directory.

## Authentic Documentation & Historical Asset Links
- **Historical Executable**: [`releases/car_troubleshooter_gui.exe`](releases/) **[ORIGINAL COMPILED BINARY]**
- **Evidence Classification**: The Python source code was lost to time but has been officially **[RECONSTRUCTED]** based strictly on the parameters documented in the verified `.rtf` file and the behavior of the original binary.

## Engineering Audit, Defensibility & Limitations
- **Static Rule Base vs. Dynamic Diagnostics**: This expert system relies entirely on a static, hard-coded Knowledge Base. While highly reliable for surface-level analog symptoms (e.g., clicking starter, steam), modern vehicles heavily utilize CAN bus networks and OBD-II (On-Board Diagnostics). A production-grade system would need to integrate a serial ELM327 interface to pull live DTCs (Diagnostic Trouble Codes) to supplement the user's visual symptom selections.

---

**Hassan Moqbel Morshed Ghaleb**
Mechatronics Engineer | Mechanical Design & CAD (SolidWorks & AutoCAD) | Preventive Maintenance & Electromechanical Systems | Industrial Automation, Control Systems, Robotics & Intelligent Machines | CAD/FEA, Embedded Systems, Python & C++
[GitHub](https://github.com/Hassan-Moqbel) · [Facebook](https://www.facebook.com/share/1BqxAgVjHi/) · [LinkedIn](https://www.linkedin.com/in/hassan-moqbel)

## License
This project is licensed under the ["MIT License"](LICENSE).
