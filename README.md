# Tkinter Interface - IPv4 Validator and Utility Tool

A comprehensive Python Tkinter GUI application for IPv4 address validation, random IP generation, and simple arithmetic operations with regular expression support.

## Description

This project provides an interactive graphical user interface (GUI) built with Tkinter that demonstrates:

- **IPv4 Validation** - Validates IPv4 addresses using regular expressions
- **Random IP Generation** - Generates valid random IPv4 addresses
- **Random String Generation** - Generates non-IP random strings for testing
- **Arithmetic Operations** - Performs addition of two numbers
- **Interface Customization** - Dynamic UI theme changes
- **Input Validation** - Real-time feedback on input validity

## Features

- **Four IPv4 Validation Fields** - Independent IPv4 validators with real-time feedback
- **Random IP Generator** - One-click generation of valid random IPv4 addresses
- **Non-IP Generator** - Generates random 20-character strings for testing
- **Arithmetic Calculator** - Simple addition of two integers
- **Color-Coded Results** - Green for valid, red for invalid results
- **Clear Function** - Reset all fields and labels
- **Customizable UI** - Change background color and fonts dynamically
- **Professional Layout** - Grid-based layout with organized frames
- **Error Handling** - Robust input validation and error messages

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- Standard library modules: `re`, `random`, `string`

## Installation

1. Ensure Python 3.6+ is installed
2. Tkinter is typically included with Python installations

**Verify Tkinter installation:**
```bash
python -c "import tkinter; print('Tkinter is installed')"
```

If not installed:

**Windows:**
```bash
# Tkinter is included in most Python installations
# If missing, reinstall Python and select "tcl/tk and IDLE"
```

**macOS:**
```bash
brew install python-tk@3.9  # or your Python version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

## Usage

### Running the Application

```bash
python "Tkinter Interface.py"
```

A window will open with the following components:

### Main Interface

**Title:** "Expresiones regulares" (Regular Expressions)

**Layout:**

```
┌─────────────────────────────────────────────────┐
│        Validación de expresiones regulares      │
├─────────────────────────────────────────────────┤
│ [IP Aleatorio] [Entry: IPv4 1]  [Validar] [Resultado]  [No IP]  │
│ [IP Aleatorio] [Entry: IPv4 2]  [Validar] [Resultado]  [No IP]  │
│ [IP Aleatorio] [Entry: IPv4 3]  [Validar] [Resultado]  [No IP]  │
│ [IP Aleatorio] [Entry: IPv4 4]  [Validar] [Resultado]  [No IP]  │
│                                                         │
│ [Entry: Number 1]  [Resultado]                        │
│ [Entry: Number 2]  [Sumar]                            │
├─────────────────────────────────────────────────┤
│ [Salir]  [Limpiar]  [Personalizar]             │
└─────────────────────────────────────────────────┘
```

### Components

#### IPv4 Validation Section

**4 Rows with:**
- **"IP Aleatoria" Button** - Generates a random valid IPv4 address
- **Entry Field** - Text input for IPv4 address
- **"Validar" Button** - Validates the entered IPv4 address
- **Result Label** - Shows "IPv4 Valida" (green) or "IPv4 Invalida" (red)
- **"No IP Aleatoria" Button** - Generates a random non-IP string

**IPv4 Validation Format:**
Valid IPv4 addresses have 4 octets separated by dots, each octet 0-255.

```
Valid examples:     Invalid examples:
192.168.1.1        256.168.1.1    (256 > 255)
10.0.0.1           192.168.1      (missing octet)
8.8.8.8            192.168.1.1.1  (too many octets)
255.255.255.255    192.168.1.a    (contains letter)
127.0.0.1          ...            (empty)
```

#### Arithmetic Section

**Two Input Fields:**
- **Num 1 Entry** - First number input
- **Num 2 Entry** - Second number input
- **"Sumar" Button** - Adds the two numbers
- **Result Label** - Displays sum or error

#### Control Buttons

- **Salir (Exit)** - Close the application
- **Limpiar (Clear)** - Reset all fields and labels
- **Personalizar (Customize)** - Change UI theme to gold background

## How It Works

### IPv4 Validation Using Regular Expressions

The application uses this regex pattern:

```regex
^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$
```

**Regex Breakdown:**

```
^                          # Start of string
((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}  # First 3 octets with dots
(25[0-5]|2[0-4]\d|[01]?\d\d?)         # Last octet
$                          # End of string

Where each octet can be:
  25[0-5]    → 250-255
  2[0-4]\d   → 200-249
  [01]?\d\d? → 0-199
```

**Example Matching:**
- `192.168.1.1` → Matches (valid)
- `256.168.1.1` → No match (256 > 255)
- `192.168` → No match (missing octets)

### Random IP Generation

Generates a valid IPv4 by creating 4 random integers (0-255) and joining with dots:

```python
IP = ".".join(str(random.randint(0, 255)) for _ in range(4))
```

Example: `123.45.67.89`

### Random String Generation

Creates a 20-character random string using letters and digits:

```python
Characters = ascii_letters + digits
Random_string = ''.join(random.choice(characters) for _ in range(20))
```

Example: `aB3cD5eF7gH9iJ1kL2mN`

### Addition with Error Handling

Safely adds two numbers with try-except:

```python
try:
    result = int(num1) + int(num2)
    display_result(result)  # Green
except ValueError:
    display_error()         # Red "Error"
```

## Code Structure

### Class: aplicacion

Main application class implementing the GUI:

#### Constructor (__init__)

Initializes the Tkinter window and creates all GUI components:

```python
def __init__(self):
    self.raiz = Tk()              # Main window
    # ... window configuration ...
    # ... create frames ...
    # ... create entry fields ...
    # ... create buttons ...
    # ... create labels ...
    self.raiz.mainloop()          # Start event loop
```

#### Methods

| Method | Purpose |
|--------|---------|
| `limpiar()` | Clear all input fields and reset labels |
| `validar(cuadro, etiqueta)` | Validate IPv4 address in field |
| `doradoTMR()` | Change UI to gold theme |
| `IPAleatoria(cuadro)` | Generate random valid IPv4 |
| `NoIpAleatoria(cuadro)` | Generate random non-IP string |
| `sumar()` | Add two numbers with error handling |

### GUI Components

**Window:**
- Size: 600×400 pixels
- Non-resizable
- Title: "Expresiones regulares"

**Frames:**
- `self.textos` - Main content frame (TOP)
- `self.frameDeAbajo` - Bottom control frame (BOTTOM)

**Entry Fields:**
- `t1, t2, t3, t4` - IPv4 input fields
- `num1, num2` - Number input fields

**Buttons:**
- Entry validation buttons (b1-b4)
- Random generation buttons
- Utility buttons (Clear, Customize, Exit)

**Labels:**
- Result labels (l1-l4) for IPv4 validation feedback
- Number labels (l5-l7) for arithmetic section

## Customization Guide

### Changing Application Title

```python
self.raiz.title('Your Custom Title')
```

### Adjusting Window Size

```python
self.raiz.geometry("800x600")  # Width x Height
self.raiz.resizable(width=True, height=True)  # Allow resizing
```

### Modifying IPv4 Pattern

To validate IPv6 or custom formats:

```python
# IPv6 example
ipv6_regex = r"^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|::1)$"

# Custom format (e.g., 3 octets only)
custom_regex = r"^(\d{1,3}\.){2}\d{1,3}$"
```

### Changing Theme Colors

**Modify the `doradoTMR()` method:**

```python
def doradoTMR(self):
    self.raiz.configure(bg='lightblue')  # Change to light blue
    estilo = ('Courier', 14)  # Different font
    self.raiz.geometry('1280x720')
```

**Common colors:**
- `'gold'` - Gold/yellow
- `'lightblue'` - Light blue
- `'lightgreen'` - Light green
- `'white'` - White
- `'lightgray'` - Light gray

### Adding More Validation Fields

```python
# Add new entry
self.t5 = Entry(self.textos, width=40)
self.t5.grid(row=4, column=1, padx=10, pady=10)

# Add new button
self.b5 = Button(self.textos, text='Validar', 
                command=lambda: self.validar(self.t5, self.l5))
self.b5.grid(row=4, column=2, padx=10, pady=10)

# Add new label
self.l5 = Label(self.textos, text='...')
self.l5.grid(row=4, column=3)
```

### Changing Button Commands

```python
# Example: Change Exit button to minimize instead
self.bsalir = Button(self.frameDeAbajo, text='Salir', 
                    command=self.raiz.iconify)
```

## Advanced Usage

### Extending Validation

Add validation for multiple formats:

```python
def validar_avanzado(self, cuadro, etiqueta):
    txt = cuadro.get()
    patterns = {
        'IPv4': r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",
        'Email': r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        'URL': r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    }
    
    for pattern_type, regex in patterns.items():
        if re.search(regex, txt):
            etiqueta.config(fg='green', text=f'{pattern_type} Valid')
            return
    
    etiqueta.config(fg='red', text='Invalid Format')
```

### Adding Tooltips

```python
def create_tooltip(widget, text):
    def on_enter(event):
        tooltip = Toplevel()
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{event.x_root}+{event.y_root}")
        label = Label(tooltip, text=text, background="yellow")
        label.pack()
    
    def on_leave(event):
        # Hide tooltip
        pass
    
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# Usage
create_tooltip(self.b1, "Click to validate IPv4 address")
```

### Data Persistence

Save and load entered data:

```python
import json

def save_data(self):
    data = {
        'ipv4_1': self.t1.get(),
        'ipv4_2': self.t2.get(),
        'num1': self.num1.get(),
        'num2': self.num2.get()
    }
    with open('saved_data.json', 'w') as f:
        json.dump(data, f)

def load_data(self):
    try:
        with open('saved_data.json', 'r') as f:
            data = json.load(f)
            self.t1.insert(0, data.get('ipv4_1', ''))
            self.t2.insert(0, data.get('ipv4_2', ''))
            self.num1.insert(0, data.get('num1', ''))
            self.num2.insert(0, data.get('num2', ''))
    except FileNotFoundError:
        pass
```

### Adding Menu Bar

```python
def create_menu(self):
    menubar = Menu(self.raiz)
    self.raiz.config(menu=menubar)
    
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=self.raiz.destroy)
    
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=self.show_about)
```

## Testing

### Test Cases for IPv4 Validation

| Input | Expected | Result |
|-------|----------|--------|
| `192.168.1.1` | Valid | ✓ Green |
| `10.0.0.1` | Valid | ✓ Green |
| `255.255.255.255` | Valid | ✓ Green |
| `0.0.0.0` | Valid | ✓ Green |
| `256.1.1.1` | Invalid | ✓ Red |
| `192.168.1` | Invalid | ✓ Red |
| `192.168.1.1.1` | Invalid | ✓ Red |
| `` | Invalid | ✓ Red |
| `abc.def.ghi.jkl` | Invalid | ✓ Red |

### Test Cases for Addition

| Input 1 | Input 2 | Expected | Result |
|---------|---------|----------|--------|
| `5` | `3` | `8` | ✓ Green |
| `100` | `-50` | `50` | ✓ Green |
| `0` | `0` | `0` | ✓ Green |
| `abc` | `5` | Error | ✓ Red |
| `5.5` | `2.5` | Error | ✓ Red |

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "ModuleNotFoundError: No module named 'tkinter'" | Tkinter not installed | Install with `pip install tk` or system package manager |
| Window won't open | Tkinter import error | Verify Python installation includes Tkinter |
| Buttons not responding | Event loop issue | Ensure `mainloop()` is called at end of `__init__` |
| Labels show wrong color | Invalid color name | Use valid Tkinter color names (`'red'`, `'green'`, etc.) |
| Entry fields truncated | Small window size | Increase geometry dimensions |

## GUI Best Practices Demonstrated

1. **Clear Layout** - Grid-based organization
2. **Color Feedback** - Visual validation (green/red)
3. **User Guidance** - Descriptive labels and buttons
4. **Error Handling** - Graceful exception handling
5. **Input Validation** - Real-time feedback
6. **Responsive Design** - Immediate visual feedback
7. **Clean Code** - Well-organized class structure

## Regular Expression Reference

**Common Patterns:**

```regex
IPv4:     ^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$
Email:    ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
Phone:    ^\+?1?\d{9,15}$
URL:      ^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
Password: ^(?=.*[A-Z])(?=.*\d).{8,}$
```

## Dependencies Overview

| Module | Purpose |
|--------|---------|
| `tkinter` | GUI framework |
| `re` | Regular expressions |
| `random` | Random number/selection generation |
| `string` | ASCII letters and digits constants |

## Educational Value

This application demonstrates:

1. **GUI Development** - Building desktop applications with Tkinter
2. **Regular Expressions** - Pattern matching for validation
3. **Event Handling** - Button clicks and user interactions
4. **Error Handling** - Try-except for robust code
5. **Widget Organization** - Layout management with frames and grids
6. **User Feedback** - Color-coded results and labels
7. **Code Organization** - Class-based GUI design

## Performance Notes

- Lightweight application ideal for learning
- Regex validation is instantaneous
- No external dependencies beyond Python standard library
- Suitable for local use only (no networking)

## Future Enhancements

Possible improvements:

1. **Additional Validators** - Email, phone, credit card
2. **Input History** - Track previous validations
3. **Export Results** - Save validation results to file
4. **Dark Mode** - Add dark theme option
5. **Multi-Language** - Support multiple languages
6. **Database Integration** - Store validation results
7. **Advanced Calculations** - More mathematical operations
8. **Configuration File** - Load settings from file

## Author

**Monjaraz Briseno Luis Fernando**

Created: September 29, 2023

## License

This project is provided as-is for educational purposes.

## References

- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
- Python Regular Expressions: https://docs.python.org/3/library/re.html
- IPv4 Address Format: https://en.wikipedia.org/wiki/IPv4

## Quick Reference

**Run the application:**
```bash
python "Tkinter Interface.py"
```

**Validate IPv4:** Click "Validar" button after entering address

**Generate Random IP:** Click "IP Aleatoria" button

**Test with Invalid Input:** Click "No IP Aleatoria" button

**Reset Interface:** Click "Limpiar" button

**Change Theme:** Click "Personalizar" button

**Close Application:** Click "Salir" button

---

For questions, issues, or contributions, please contact the author.
