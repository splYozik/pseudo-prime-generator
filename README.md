# pseudo-prime-generator

This is a simple Python tool I made to generate and test **pseudo-prime numbers**.
> ⚠️ **WARNING:** The generated numbers are **NOT cryptographically secure**.

- **def generate_random** - uses the built-in random.randint(0, 9) function
- **def generate_time** - digits from the system clock
- **def generate_LCG** - classic Linear Congruential Generator

## 🗂 What's inside?

* `main.py` — The main script. Run this to start the generator.
* `func.py` — All the math logic.
* `config.py` — A change text print.

## 🚀 To run it

First, you have **Python 3.8+** installed (no extra packages needed!).

```bash
# 1. Clone the repo
git clone https://github.com/splYozik/pseudo-prime-generator.git

# 2. Cd folder
cd pseudo-prime-generator

# 3. Start
python main.py
```

## ⚠️ Limitations

* **Non-uniform Distribution:** Candidates are found via linear increment, causing predictable digit patterns and biased distribution.
* **Not Cryptographically Secure:** Do not use for real-world encryption or key generation.
