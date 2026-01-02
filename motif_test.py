import tkinter as tk
from tkinter import simpledialog, messagebox

def find_motif(mosaic, motif, rq, cq, rp, cp):
    matches = 0
    positions = []

    for i in range(rq - rp + 1):
        for j in range(cq - cp + 1):
            match_found = True
            for x in range(rp):
                for y in range(cp):
                    if motif[x][y] != 0 and mosaic[i + x][j + y] != motif[x][y]:
                        match_found = False
                        break
                if not match_found:
                    break
            if match_found:
                matches += 1
                positions.append((i + 1, j + 1))

    return matches, positions

def input_matrix(rows, cols, title):
    matrix = []
    for i in range(rows):
        row = simpledialog.askstring(title, f"Enter row {i + 1} (space-separated values):")
        matrix.append([int(num) for num in row.split()])
    return matrix

def start_application():
    root = tk.Tk()
    root.withdraw() 

    rp = simpledialog.askinteger("Motif", "Enter the number of rows in motif:")
    cp = simpledialog.askinteger("Motif", "Enter the number of columns in motif:")
    motif = input_matrix(rp, cp, "Motif")

    rq = simpledialog.askinteger("Mosaic", "Enter the number of rows in mosaic:")
    cq = simpledialog.askinteger("Mosaic", "Enter the number of columns in mosaic:")
    mosaic = input_matrix(rq, cq, "Mosaic")

    matches, positions = find_motif(mosaic, motif, rq, cq, rp, cp)

    output_message = f"Total matches found: {matches}\n"
    if matches > 0:
        output_message += "Positions:\n" + "\n".join([f"Row: {pos[0]}, Column: {pos[1]}" for pos in positions])

    messagebox.showinfo("Result", output_message)


start_application()