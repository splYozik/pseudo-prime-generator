import config
from func import generator


def main() -> None:
    """Handles user inputs, performs validation, and triggers the generator."""
    print(f'{config.LINE}\n{config.WELCOME}\n{config.LINE}')

    # 1. Get and validate digit length
    while True:
        length_input = input(config.LENGTH_PROMPT).strip()
        try:
            # Handle binary, hex, and octal inputs if the user tries to get fancy
            if length_input.lower().startswith(('0b', '0x', '0o')):
                length = int(length_input, 0)
            else:
                length_float = float(length_input)

                # Block Infinity or NaN inputs to prevent infinite loops
                if length_float == float('inf') or length_float == float('-inf'):
                    print(config.ERR_OVERFLOW)
                    continue

                # Ensure it's a whole number (e.g., reject 10.5 but allow 10.0)
                if not length_float.is_integer():
                    print(config.ERR_NOT_INT)
                    continue

                length = int(length_float)

            # Keep it within reasonable bounds
            if length < 1 or length > 1000:
                print(config.ERR_RANGE)
                continue
            
            break
    
        except (ValueError, NameError):
            print(config.ERR_NOT_NUM)
            continue

    # 2. Get and validate LCG constants
    while True:
        constants_input = input(config.CONSTANTS_PROMPT).strip()
        
        # Fallback to default safe LCG parameters
        a, c, m = 15245, 1889, 2**31

        if constants_input:
            try:
                full = constants_input.split(',')

                # Must have exactly A, C, and M
                if len(full) != 3:
                    raise ValueError

                # Clean spaces, parse floats first (to support 1e3 syntax), then cast to int
                a_new = int(float(full[0].strip()))
                c_new = int(float(full[1].strip()))
                m_new = int(float(full[2].strip()))

                # Prevent ZeroDivisionError in the modulo operation later
                if m_new == 0:
                    print(config.ERR_ZERO_DIV)
                    continue

                a, c, m = a_new, c_new, m_new
                
            except (ValueError, IndexError):
                print(config.ERR_INVALID_FORMAT)
                continue
        
        break

    generator(a, c, m, length)


if __name__ == "__main__":
    while True:
        main()
        print(config.LINE)

        end = input(config.EXIT_PROMPT).strip().lower()
        if end == 'y':
            print(config.BYE_MSG)
            break
