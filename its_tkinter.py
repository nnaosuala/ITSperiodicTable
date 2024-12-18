import tkinter as tk
from owlready2 import get_ontology

# Load ontology
ontology_path = ontology_path = r"C:\Users\osual\Desktop\Ontology\ITSperiodicTable" # Update this with the exact location of your OWL file
onto = get_ontology(f"file://{ontology_path}").load()

# Function to fetch element data
def fetch_element():
    element_name = entry.get().capitalize()  # Get user input and capitalize
    try:
        # Search for the element as an individual of the 'Element' class
        element = onto.search_one(iri=f"*{element_name}")
        if element:
            # Retrieve data properties
            atomic_number = element.has_Atomic_Number[0] if element.has_Atomic_Number else "N/A"
            atomic_mass = element.has_Atomic_Mass[0] if element.has_Atomic_Mass else "N/A"
            
            # Update result label
            result_label.config(
                text=f"Name: {element_name}\n"
                     f"Atomic Number: {atomic_number}\n"
                     f"Atomic Mass: {atomic_mass}"
            )
        else:
            result_label.config(text=f"Element '{element_name}' not found in ontology!")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Tkinter setup
root = tk.Tk()
root.title("Periodic Table ITS")

# Input field
tk.Label(root, text="Enter Element Name:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Search button
tk.Button(root, text="Search", command=fetch_element).pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()

print("Ontology loaded classes:", list(onto.classes()))

