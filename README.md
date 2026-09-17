# CS50P — Introduction to Programming with Python

This repository contains my coursework for HarvardX's CS50P (CS50's Introduction to
Programming with Python), an edX course covering functions, variables, conditionals,
loops, exceptions, libraries, unit testing, file I/O, regular expressions, and
object-oriented programming in Python. I completed the course and received a
certificate (see [`certificate/`](certificate/)). The exercises below are organized
by the Python concept each one primarily demonstrates rather than by problem-set
number, so related techniques are grouped together regardless of when they appeared
in the course.

Four problems — Home Federal Savings Bank (`bank`), Fuel Gauge (`fuel`), Vanity
Plates (`plates`), and Setting up my twttr (`twttr`) — were each assigned twice: once
as a plain implementation, and again later in the course restructured with a
`test_*.py` unit-test suite. To avoid duplication, only the final, tested version of
each is included, filed under **Unit Testing**.

## Table of Contents

1. [Functions and Variables](#01-functions-and-variables)
2. [Conditionals](#02-conditionals)
3. [Loops](#03-loops)
4. [Exceptions and Input Validation](#04-exceptions-and-input-validation)
5. [Libraries](#05-libraries)
6. [Unit Testing](#06-unit-testing)
7. [File I/O and Regular Expressions](#07-file-io-and-regex)
8. [Object-Oriented Programming](#08-object-oriented-programming)
9. [Final Project](#09-final-project)
10. [Et Cetera](#10-et-cetera)
11. [Certificate](#certificate)

---

## 01-functions-and-variables

Small programs built around a single calculation or transformation, with no
branching, looping, or error handling.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`einstein`](01-functions-and-variables/einstein/) | Prompts for a mass in kg and prints the energy `E = mc^2` using `pow(300000000, 2)`. | Basic arithmetic, a helper function returning a computed value. |
| [`indoor`](01-functions-and-variables/indoor/) | Prompts for a string and prints it lower-cased. | Defining and calling a simple function, string method `.lower()`. |
| [`playback`](01-functions-and-variables/playback/) | Prompts for a sentence and replaces every space with `...` to simulate slowed-down playback. | String method `.replace()`, passing/returning values between functions. |
| [`tip`](01-functions-and-variables/tip/) | Prompts for a meal cost and a tip percentage (strings like `$10` and `15%`), strips the symbols, and prints the tip owed. | Type conversion (`str` to `float`), string cleanup with `.replace()`, formatted output. |

## 02-conditionals

Programs whose logic is driven by `if`/`elif`/`else` chains or `match`/`case`
statements.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`coke`](02-conditionals/coke/) | Simulates a vending machine: accepts 5/10/25-cent coins via `match`/`case` until 50 cents is reached, then reports change owed. | `match`/`case` for handling a fixed set of valid values. |
| [`deep`](02-conditionals/deep/) | Asks "What is the answer to the Great Question?" and checks the reply against `42`, `"forty-two"`, or `"forty two"`. | `match`/`case` with multiple patterns per branch, `try`/`except` for flexible type coercion. |
| [`extensions`](02-conditionals/extensions/) | Prompts for a filename and prints the matching media type (`image/gif`, `application/pdf`, etc.) based on its suffix, defaulting to `application/octet-stream`. | Sequential `if`/`elif` string-suffix matching. |
| [`faces`](02-conditionals/faces/) | Converts `:)` and `:(` emoticons in a line of text into 🙂 and 🙁. | `if`/`elif` branching combined with `str.replace()`. |
| [`interpreter`](02-conditionals/interpreter/) | Parses an expression like `1 + 1`, splits it into operands and operator, and evaluates it. | `str.split()` unpacking, `if`/`elif` dispatch on an operator string. |
| [`meal`](02-conditionals/meal/) | Converts a 24-hour time (e.g. `7:30`) to a decimal hour and reports whether it falls in the breakfast, lunch, or dinner window. | Numeric conversion plus range checks with `if`/`elif`. |

## 03-loops

Programs where a `for` or `while` loop is the central mechanism — iterating over
characters, repeating until a sentinel value, or repeating a fixed number of times.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`camel`](03-loops/camel/) | Converts a camelCase variable name to snake_case. | `for` loop over characters, conditional transformation, string rebuilding. |
| [`game`](03-loops/game/) | A number-guessing game: picks a random integer up to a user-chosen level and loops on "Too small!"/"Too large!" until the guess is correct. | `while True` loops with `continue`/`break`, `random.randint`. |
| [`grocery`](03-loops/grocery/) | Reads grocery items one per line until EOF (Ctrl-D), then prints each item in uppercase with its count, sorted alphabetically. | Loop-until-EOF pattern, dictionaries for counting, `sorted()`. |
| [`nutrition`](03-loops/nutrition/) | Looks up the calorie count of a fruit from a hardcoded FDA-poster dictionary. | Loop-based normalization of multi-word input, dictionary lookup. |
| [`professor`](03-loops/professor/) | "Little Professor" style quiz: generates 10 addition problems at a chosen difficulty level, giving up to 3 tries each, and reports a final score. | Nested loops (10 problems x 3 tries), `random.randint`, score tallying. |
| [`taqueria`](03-loops/taqueria/) | Takes a taco-shop order one item per line until EOF, printing a running total after each item. | Loop-until-EOF pattern, dictionary-based price lookup, running totals. |

## 04-exceptions-and-input-validation

The one exercise here uses a broad `try`/`except` specifically to gate a
retry-until-valid input loop (as opposed to the exception use in `04`'s sibling
exercises `bank`/`fuel`/`plates`, which ended up filed under Unit Testing — see
below).

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`outdated`](04-exceptions-and-input-validation/outdated/) | Prompts for a date in `9/8/1636` or `September 8, 1636` format and reprints it in ISO `YYYY-MM-DD` order, re-prompting on bad input. | `try`/`except` wrapping a parsing loop, string splitting, a month-name-to-number dictionary. |

Note: **Fuel Gauge**, one of the course's core exceptions exercises (validating a
`X/Y` fraction and catching `ValueError`/`ZeroDivisionError`), is included under
[Unit Testing](#06-unit-testing) instead of here, because the version kept in this
repository is the later revision that added `test_fuel.py`.

## 05-libraries

Programs whose main point is calling a third-party (PyPI) package rather than
stdlib-only code.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`adieu`](05-libraries/adieu/) | Reads names one per line until EOF and bids them "Adieu" with grammatically correct comma/and separation. | The `inflect` library's `.join()` for natural-language list joining. |
| [`bitcoin`](05-libraries/bitcoin/) | Takes a quantity of Bitcoin as a command-line argument and prints its value in USD. | The `requests` library for an HTTP GET, JSON response parsing, `sys.argv`. |
| [`emojize`](05-libraries/emojize/) | Converts emoji shortcodes/aliases (e.g. `:thumbsup:`) typed in a string into the actual emoji. | The `emoji` library's `emojize()` function. |
| [`figlet`](05-libraries/figlet/) | Prints user-supplied text as large ASCII-art letters, in a random font or a font chosen via `-f`/`--font`. | The `pyfiglet` library, command-line argument parsing, `random.choice`. |
| [`response`](05-libraries/response/) | Validates whether user input is a properly formatted email address. | The `validator_collection` library's `checkers.is_email()`. |

## 06-unit-testing

Every exercise here ships with a companion `test_*.py` file runnable via `pytest`.
Four of them (`bank`, `fuel`, `plates`, `twttr`) are problems that were originally
assigned earlier in the course without tests, then reassigned later in the
"Unit Tests" unit with the same logic restructured into a testable function and a
matching test suite — only that final, tested version is kept here.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`bank`](06-unit-testing/bank/) | Classifies a greeting as $0 ("hello..."), $20 ("h..." but not hello), or $100 (otherwise). *(Revisit of an earlier conditionals exercise, now with tests.)* | `pytest` tests covering each branch, refactoring `print`-based logic into a `value()` function that returns instead of prints. |
| [`fuel`](06-unit-testing/fuel/) | Converts an `X/Y` fuel-fraction string to a percentage, returning `"E"`/`"F"` near empty/full. *(Revisit of an earlier exceptions exercise, now with tests.)* | `pytest.raises` for `ValueError`/`ZeroDivisionError`, separating `convert()` and `gauge()` into independently testable functions. |
| [`plates`](06-unit-testing/plates/) | Validates a Massachusetts vanity license plate against the state's formatting rules. *(Revisit of an earlier conditionals exercise, now with tests.)* | Multiple `pytest` cases per validation rule (length, first-two-letters, digit placement, leading zero, alphanumeric-only). |
| [`twttr`](06-unit-testing/twttr/) | Strips vowels from a string of text (`twitter` → `twttr`). *(Revisit of an earlier conditionals exercise, now with tests.)* | `pytest` assertions across mixed-case and punctuated input. |
| [`jar`](06-unit-testing/jar/) | A `Jar` class modeling a cookie jar with a fixed capacity, supporting `deposit`/`withdraw` and printing cookie emoji for its contents. | Class design with `@property`, custom validation raising `ValueError`, `pytest.raises`. |
| [`lines`](06-unit-testing/lines/) | Counts non-blank, non-comment lines of code in a `.py` file given as a command-line argument. | File reading with `open()`/iteration, `sys.exit` on bad arguments, minimal `pytest` coverage. |
| [`numb3rs`](06-unit-testing/numb3rs/) | Validates whether a string is a well-formed IPv4 address. | Regular expressions (`re.search` with `re.VERBOSE`) for structured validation, thorough `pytest` true/false/format cases. |
| [`seasons`](06-unit-testing/seasons/) | Computes the number of minutes a user has been alive from their date of birth, spelled out in words. | `datetime.date` arithmetic, the `inflect` library's `number_to_words`, `pytest.raises(SystemExit)`. |
| [`um`](06-unit-testing/um/) | Counts case-insensitive whole-word occurrences of "um" in a string. | Regular expressions with word boundaries (`\bum\b`) and `re.IGNORECASE`. |
| [`working`](06-unit-testing/working/) | Converts a 12-hour time range (e.g. `9 AM to 5 PM`) to 24-hour format, raising `ValueError` on malformed input. | A single detailed `re.VERBOSE` pattern with optional groups, helper function for AM/PM conversion, several `pytest` cases. |

## 07-file-io-and-regex

Exercises centered on reading/writing files, parsing CSV, processing images, or
matching text with regular expressions.

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`pizza`](07-file-io-and-regex/pizza/) | Reads a CSV menu file and renders it as an ASCII-art grid table. | `csv.DictReader`, the `tabulate` library for formatting, `sys.exit` on bad arguments. |
| [`scourgify`](07-file-io-and-regex/scourgify/) | Reads a CSV of `"last, first", house` rows and writes a new CSV with separate `first`/`last`/`house` columns. | `csv.DictReader`/`csv.DictWriter`, file input and output in the same program. |
| [`shirt`](07-file-io-and-regex/shirt/) | Overlays a transparent shirt image onto an input photo, resized and cropped to match. | The `PIL`/`Pillow` library (`Image.open`, `ImageOps.fit`, `Image.paste`, `Image.save`). |
| [`watch`](07-file-io-and-regex/watch/) | Extracts a YouTube embed URL from a block of HTML and converts it to a short `youtu.be` link. | Regular expressions (`re.search`) for extracting and reshaping matched text. |

## 08-object-oriented-programming

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`shirtificate`](08-object-oriented-programming/shirtificate/) | Generates a "\<Name\> took CS50" certificate PDF. | A custom class inheriting from `fpdf.FPDF`, overriding its `header()` hook and adding its own methods for constructor validation and rendering the name. |

## 09-final-project

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`project`](09-final-project/project/) | **Knitting shirts with code** — a virtual custom-shirt order system. The user types up to two characters to have "stitched" onto a shirt (rendered as ASCII art via the `art` library), picks a thread color (which affects price), and the program downloads the CS50 shirt template over HTTP, composites everything into an order receipt, and outputs a PDF (`custom_order.pdf`) showing the design and an itemized price. | Combines object-oriented design (a `Shirt_custom` class extending `fpdf.FPDF`), an HTTP request (`requests.get`) to fetch an image asset, PDF generation, and `pytest` unit tests (`test_project.py`) covering pricing logic and the image download. |

## 10-et-cetera

| Exercise | What it does | Key concept demonstrated |
|---|---|---|
| [`test`](10-et-cetera/test/) | A short scratch script that runs `os.path.splitext` on a couple of hardcoded filenames and prints the extension. | Not a graded problem-set exercise — kept as a small experiment/reference snippet on `os.path.splitext`, related to the suffix-matching logic used in `extensions`. |

## Certificate

[`certificate/CS50P_certificate.pdf`](certificate/CS50P_certificate.pdf) — HarvardX CS50P certificate of completion, issued via edX.
