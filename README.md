# Python Text Analyzer

A command-line tool for analyzing text files. This program counts lines, words, letters, and finds the most frequently used words and letters in a given text file.

## Features
- **Count lines** – Find out how many lines exist in a file.
- **Count words** – Determine the total number of words.
- **Count letters** – Count the number of letters in the text.
- **Word frequency** – Identify the seven most commonly used words.
- **Letter frequency** – Find the seven most common letters.
- **Batch analysis** – Run all text analysis functions at once.
- **Change file** – Switch to a different text file for analysis.

## Installation
### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Python-Text-Analyzer.git
cd Python-Text-Analyzer
```

### Run the Program
Make sure you have Python 3 installed, then execute:
```bash
python3 main.py
```

## Usage
Once running, enter a command from the menu to perform text analysis:

### Example Commands:
```
--> menu
--> lines
--> words
--> letters
--> word_frequency
--> letter_frequency
--> all
--> change (switch text file)
--> q (quit the program)
```

### Example Output:
```
lines: 20
words: 150
letters: 780
Most common words:
the: 10 | 5.2%
and: 8 | 4.1%
...
```

## File Structure
```
📂 Python-Text-Analyzer
├── 📄 main.py          # Main script handling user input
├── 📄 analyzer.py      # Functions for text analysis
├── 📄 menu.py         # Menu system
├── 📄 phil.txt        # Example text file
```

## Contributing
Feel free to fork the repository and submit pull requests with improvements.

## License
This project is open-source and available under the MIT License.

