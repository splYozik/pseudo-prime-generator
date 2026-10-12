# --- UI Decorators ---
WELCOME = "====== Huge Number Generator Script v1.0 ======"
LINE = "=" * 50

# --- Prompts ---
LENGTH_PROMPT = "\nEnter required digit length (1-1000) => "
CONSTANTS_PROMPT = "Enter LCG constants A, C, M (separated by commas) [Leave empty for default]: \n=> "
EXIT_PROMPT = "Exit application? (y/n): "

# --- Success / Info Messages ---
BYE_MSG = "Goodbye!"
GENERATION_END_MSG = "Generation completed."

# --- Error Messages ---
ERR_OVERFLOW = "[-] Error: Value is out of bounds (Too HUGE or too SMALL)!"
ERR_NOT_INT = "[-] Error: Length must be a whole integer."
ERR_RANGE = "[-] Error: Please enter a length between 1 and 1000."
ERR_NOT_NUM = "[-] Error: Invalid input format. Numeric integer value required."
ERR_ZERO_DIV = "[-] Error: Modulus M cannot be zero (Division by zero protection)."
ERR_INVALID_FORMAT = "[-] Error: Invalid format.\n>> Expected exactly 3 numbers separated by commas: A, C, M (e.g., '15245, 1889, 2147483648')"