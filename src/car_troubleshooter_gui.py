"""
[RECONSTRUCTED] Car Troubleshooting Expert System
Historical source code reconstructed from original RTF documentation and binary specifications.
Framework: Python 3, tkinter
Architecture: Forward-Chaining Rule-Based Expert System
"""

import tkinter as tk
from tkinter import ttk, messagebox

class KnowledgeBase:
    def __init__(self):
        # Format: (Symptom Set, Diagnosis, Recommendation)
        self.rules = [
            (
                {"No crank", "Clicking sound"},
                "Dead Battery or Bad Starter Relay",
                "Check battery voltage (should be >12.4V). Jump start the vehicle. If it still clicks, test the starter relay and solenoid."
            ),
            (
                {"No crank", "Lights dim when turning key"},
                "Severely Discharged Battery or Corroded Terminals",
                "Clean battery terminals with a wire brush. Attempt a jump start. Test alternator output once running."
            ),
            (
                {"Slow crank"},
                "Weak Battery or Thick Oil (Cold Weather)",
                "Test battery CCA (Cold Cranking Amps). Ensure engine oil viscosity is correct for current climate."
            ),
            (
                {"Cranks but no start", "Sputtering"},
                "Fuel Delivery Failure",
                "Listen for fuel pump priming when key is turned to ON. Check fuel pressure at the rail. Inspect fuel filter."
            ),
            (
                {"Cranks but no start"},
                "Ignition or Fuel System Failure",
                "Check for spark at the plugs using a spark tester. Verify fuel pump operation and check for blown fuses."
            ),
            (
                {"Overheating", "Steam from under hood"},
                "Coolant Leak or Blown Head Gasket",
                "DO NOT OPEN RADIATOR CAP WHILE HOT! Check for visible leaks in hoses. Check oil for milky consistency (head gasket)."
            ),
            (
                {"Overheating"},
                "Radiator Fan Failure or Thermostat Stuck Closed",
                "Verify radiator fan turns on at operating temp. Check thermostat and coolant levels."
            ),
            (
                {"Battery drain overnight"},
                "Parasitic Electrical Draw",
                "Perform a parasitic draw test using a multimeter in series with the negative terminal. Pull fuses one by one to isolate the circuit."
            )
        ]

class ExpertSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Troubleshooting Expert System")
        self.root.geometry("600x500")
        
        self.kb = KnowledgeBase()
        self.symptoms = [
            "No crank", 
            "Clicking sound", 
            "Lights dim when turning key", 
            "Slow crank", 
            "Cranks but no start", 
            "Sputtering", 
            "Overheating", 
            "Steam from under hood", 
            "Battery drain overnight"
        ]
        
        self.check_vars = {}
        
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = ttk.Label(self.root, text="Automotive Diagnostic System", font=("Helvetica", 16, "bold"))
        header.pack(pady=10)
        
        instructions = ttk.Label(self.root, text="Select all symptoms currently exhibited by the vehicle:")
        instructions.pack(pady=5)
        
        # Checkboxes Frame
        frame = ttk.Frame(self.root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        for sym in self.symptoms:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(frame, text=sym, variable=var)
            chk.pack(anchor=tk.W, padx=20, pady=2)
            self.check_vars[sym] = var
            
        # Analyze Button
        btn = ttk.Button(self.root, text="Run Diagnostics", command=self.run_diagnostics)
        btn.pack(pady=20)
        
    def run_diagnostics(self):
        # Gather facts (selected symptoms)
        active_symptoms = {sym for sym, var in self.check_vars.items() if var.get()}
        
        if not active_symptoms:
            messagebox.showinfo("Result", "Please select at least one symptom.")
            return
            
        # Forward Chaining Inference Engine
        best_match = None
        max_overlap = 0
        
        for rule_symptoms, diagnosis, recommendation in self.kb.rules:
            # Check intersection of symptoms
            overlap = len(active_symptoms.intersection(rule_symptoms))
            
            # If the rule's conditions are a subset of the active symptoms (Modus Ponens trigger)
            # Or if it's the strongest partial match
            if rule_symptoms.issubset(active_symptoms):
                best_match = (diagnosis, recommendation)
                break # Exact subset match fires immediately
            elif overlap > max_overlap:
                max_overlap = overlap
                best_match = (diagnosis, recommendation)
                
        if best_match:
            diag, rec = best_match
            self.show_results(diag, rec)
        else:
            self.show_results("Unknown Malfunction", "The symptom combination does not match known deterministic rules. Further physical OBD-II scanning required.")

    def show_results(self, diagnosis, recommendation):
        res_win = tk.Toplevel(self.root)
        res_win.title("Diagnostic Report")
        res_win.geometry("400x300")
        
        lbl_diag_title = ttk.Label(res_win, text="Diagnosis:", font=("Helvetica", 12, "bold"))
        lbl_diag_title.pack(pady=(20,5))
        
        lbl_diag = ttk.Label(res_win, text=diagnosis, wraplength=350, justify=tk.CENTER)
        lbl_diag.pack(pady=5)
        
        lbl_rec_title = ttk.Label(res_win, text="Recommended Action:", font=("Helvetica", 12, "bold"))
        lbl_rec_title.pack(pady=(20,5))
        
        lbl_rec = ttk.Label(res_win, text=recommendation, wraplength=350, justify=tk.CENTER)
        lbl_rec.pack(pady=5)
        
        btn_close = ttk.Button(res_win, text="Close", command=res_win.destroy)
        btn_close.pack(side=tk.BOTTOM, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemGUI(root)
    root.mainloop()
