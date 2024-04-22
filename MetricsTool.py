import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext
import ast
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze

def calculate_metrics(source_code):
    # Calculate Cyclomatic Complexity
    complexity = cc_visit(source_code)
    complexity_scores = [(func.name, func.complexity) for func in complexity]

    # Calculate Lines of Code
    loc = analyze(source_code)

    # Calculate Maintainability Index
    maintainability_index = mi_visit(source_code, True)

    return {
        "Cyclomatic Complexity": complexity_scores,
        "Lines of Code": loc,
        "Maintainability Index": maintainability_index
    }

def get_class_definitions(source_code):
    tree = ast.parse(source_code)
    return [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

def calculate_dit(classes, base_classes):
    dit = {}
    for cls in classes:
        depth = 0
        current = cls
        while any(base.id in base_classes for base in current.bases if isinstance(base, ast.Name)):
            depth += 1
            parent_name = next(base.id for base in current.bases if isinstance(base, ast.Name))
            current = base_classes.get(parent_name, None)
            if current is None:
                break
        dit[cls.name] = depth
    return dit

def calculate_noc_nop(classes):
    noc = {cls.name: 0 for cls in classes}
    nop = {}
    for cls in classes:
        nop[cls.name] = len([base for base in cls.bases if isinstance(base, ast.Name)])
        for base in cls.bases:
            if isinstance(base, ast.Name) and base.id in noc:
                noc[base.id] += 1
    return noc, nop

def calculate_pf(classes, class_map):
    method_overrides = {cls.name: 0 for cls in classes}
    for cls in classes:
        if not cls.bases:
            continue
        for base in cls.bases:
            if isinstance(base, ast.Name) and base.id in class_map:
                base_cls = class_map[base.id]
                base_methods = {n.name for n in base_cls.body if isinstance(n, ast.FunctionDef)}
                derived_methods = {n.name for n in cls.body if isinstance(n, ast.FunctionDef)}
                method_overrides[cls.name] += len(base_methods.intersection(derived_methods))
    return method_overrides

def analyze_object_oriented_metrics(source_code):
    classes = get_class_definitions(source_code)
    class_map = {cls.name: cls for cls in classes}
    dit = calculate_dit(classes, class_map)
    noc, nop = calculate_noc_nop(classes)
    pf = calculate_pf(classes, class_map)
    return dit, noc, nop, pf

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        analyze_button['state'] = 'normal'

def perform_analysis():
    file_path = file_entry.get()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                source_code = file.read()

            metrics = calculate_metrics(source_code)
            dit, noc, nop, pf = analyze_object_oriented_metrics(source_code)

            result_text.insert(tk.END, f"\nAnalysis of {file_path}:\n")
            result_text.insert(tk.END, "--------------------------------------------------\n")
            result_text.insert(tk.END, "Object-Oriented Metrics:\n")
            result_text.insert(tk.END, f"\nDepth of Inheritance Tree (DIT): {dit}\n")
            result_text.insert(tk.END, f"\nNumber of Children (NOC): {noc}\n")
            result_text.insert(tk.END, f"\nNumber of Parents (NOP): {nop}\n")
            result_text.insert(tk.END, f"\nPolymorphism Factor (PF): {pf}\n")
            result_text.insert(tk.END, "--------------------------------------------------\n")
            display_existing_metrics(metrics)
        except Exception as e:
            result_text.insert(tk.END, f"Error: {str(e)}\n")
        result_text.see(tk.END)

def display_existing_metrics(metrics):
    if "error" in metrics:
        result_text.insert(tk.END, f"Error reading file: {metrics['error']}\n")
    else:
        result_text.insert(tk.END, "Cyclomatic Complexity:\n")
        for name, complexity in metrics["Cyclomatic Complexity"]:
            result_text.insert(tk.END, f"{name}: {complexity}\n")
        result_text.insert(tk.END, "--------------------------------------------------\n")
        result_text.insert(tk.END, f"Lines of Code: {metrics['Lines of Code'].loc}\n")
        result_text.insert(tk.END, f"Maintainability Index: {metrics['Maintainability Index']}\n")
        result_text.insert(tk.END, "--------------------------------------------------\n")

app = tk.Tk()
app.title("Code Metrics Analyzer")

main_frame = ttk.Frame(app, padding="10")
main_frame.grid()

ttk.Label(main_frame, text="Select Python File:").grid(row=0, column=0)
file_entry = ttk.Entry(main_frame, width=50)
file_entry.grid(row=0, column=1)
ttk.Button(main_frame, text="Browse...", command=select_file).grid(row=0, column=2)

analyze_button = ttk.Button(main_frame, text="Analyze", command=perform_analysis, state='disabled')
analyze_button.grid(row=1, columnspan=3)

result_text = scrolledtext.ScrolledText(main_frame, width=80, height=20)
result_text.grid(row=2, columnspan=3)

app.mainloop()
