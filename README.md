# Zodiac Sign Finder

> An interactive CLI application that determines your zodiac sign based on birth date and month information with user validation logic.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Repository Size](https://img.shields.io/github/repo-size/TROJAN1HAMMER/zodiac-sign-finder)](https://github.com/TROJAN1HAMMER/zodiac-sign-finder)

---

## 📋 Overview

The **Zodiac Sign Finder** is a Python-based command-line application designed to calculate and display a user's zodiac sign based on their birth date and month. The application implements input validation patterns, recursive error handling, and conditional logic for date-range mapping across all twelve zodiac signs.

### Key Value Proposition
- **User-Centric Design**: Interactive confirmation flow to prevent data entry errors
- **Data Validation**: Recursive input correction mechanism for accurate zodiac determination
- **Comprehensive Coverage**: Complete mapping of all 366 possible date ranges to zodiac signs
- **Learning Resource**: Demonstrates fundamental Python concepts including conditionals, range operations, and user input handling

---

## ✨ Features

- ✅ **Interactive User Input**: Captures user name, birth date, and birth month
- ✅ **Data Verification**: Confirmation prompt before zodiac calculation to ensure accuracy
- ✅ **Recursive Error Correction**: Automatically re-prompts users if they indicate incorrect information
- ✅ **Complete Zodiac Mapping**: Accurate date-range assignments for all 12 zodiac signs
- ✅ **User-Friendly Output**: Clear, personalized messages with zodiac sign results
- ✅ **Cross-Platform Compatible**: Pure Python with no external dependencies

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.6+ |
| **Type** | Command-Line Interface (CLI) |
| **Dependencies** | None (standard library only) |
| **Runtime** | Python Interpreter |

---

## 🏗️ Architecture

### Design Pattern: Sequential Processing with Validation

```
User Input (Name)
    ↓
Date/Month Collection
    ↓
Confirmation Logic
    ├─→ If Incorrect → Recursive Re-entry
    └─→ If Correct → Zodiac Determination
    ↓
Conditional Date-Range Mapping
    ↓
User-Personalized Output
```

### Core Logic Components

1. **Input Collection Module**
   - Captures user identifiers (name)
   - Collects birth date (integer: 1-31)
   - Collects birth month (string, case-insensitive)

2. **Validation Module**
   - String normalization (lowercase conversion)
   - User confirmation prompt
   - Recursive correction mechanism

3. **Zodiac Determination Module**
   - Month-based branching logic
   - Date-range comparisons using Python's `range()` function
   - 24 conditional statements covering all zodiac sign boundaries

4. **Output Module**
   - Personalized user greeting
   - Zodiac sign assignment
   - Gratitude message

---

## 📁 Folder Structure

```
zodiac-sign-finder/
├── main.py                 # Primary application logic (100 lines)
├── README.md              # Project documentation
└── [configuration files]  # GitHub workflows & settings
```

### File Descriptions

| File | Purpose | Size |
|------|---------|------|
| `main.py` | Complete zodiac sign determination logic | 3.5 KB |

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Command-line terminal/shell

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/TROJAN1HAMMER/zodiac-sign-finder.git
   cd zodiac-sign-finder
   ```

2. **Verify Python installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the application**
   ```bash
   python main.py
   # or
   python3 main.py
   ```

---

## 💻 Usage

### Running the Application

```bash
$ python main.py
Hi!
What is your name: John Smith
What is your birth date(00): 15
What is the month of your birth: March
Since your birth month is: march
And your birth date is: 15
Is the given informations correct? yes
Your zodiac sign is Pisces.
Thank you for using this,  John Smith
hope your found your zodiac sign.
```

### User Interaction Flow

1. **Enter Your Name**: The system greets you and requests identification
2. **Input Birth Date**: Provide your day of birth (1-31)
3. **Input Birth Month**: Specify your birth month (case-insensitive)
4. **Confirm Information**: Verify accuracy; enter "no" to re-enter data
5. **Receive Zodiac Sign**: Get your astrological sign based on the provided dates

### Example Scenarios

**Scenario 1: Correct Information**
```
Is the given informations correct? yes
Your zodiac sign is Aries.
```

**Scenario 2: Incorrect Information (Recursive)**
```
Is the given informations correct? No
What is your birth date(00): 25
What is the month of your birth: april
Since your birth month is: april
And your birth date is: 25
Is the given informations correct? yes
Your zodiac sign is Tarus.
```

---

## 🎯 Challenges Solved

### 1. **Date Range Mapping Complexity**
   - **Challenge**: Accurately mapping 366 date combinations to 12 zodiac signs
   - **Solution**: Implemented monthly branching with nested date-range conditionals using Python's `range()` function for efficient boundary comparisons

### 2. **User Input Validation**
   - **Challenge**: Preventing incorrect data entry from producing false zodiac assignments
   - **Solution**: Added confirmation logic with case-insensitive string comparison and recursive re-entry mechanism

### 3. **String Normalization**
   - **Challenge**: Handling month names with varying case inputs (MARCH, March, march)
   - **Solution**: Implemented `.lower()` method for consistent case handling before conditional matching

### 4. **Improved User Experience**
   - **Challenge**: Distinguishing valid "no" responses across different case variations
   - **Solution**: Created reference list `a_1` to capture multiple case formats before recursive call

### 5. **Data Type Conversions**
   - **Challenge**: Converting mixed input types (date as integer, month as string)
   - **Solution**: Explicit type casting with `int()` and string input management

---

## 🔮 Future Improvements

### Short-Term Enhancements
- [ ] **Input Validation Enhancement**
  - Validate date range (1-31) before processing
  - Validate month exists in zodiac calendar
  - Add error messages for invalid inputs

- [ ] **Code Refactoring**
  - Extract zodiac mapping into dictionary/data structure
  - Implement function-based month handling
  - Remove code duplication using loops

- [ ] **Bug Fixes**
  - Correct spelling errors: "Aquaiurs" → "Aquarius", "Sagattarius" → "Sagittarius"
  - Fix line 64: "zodiac sgn" → "zodiac sign"
  - Correct line 78: Handle "October" case-sensitivity
  - Fix line 49: Range should start from 1, not 0

### Medium-Term Features
- [ ] **Testing Framework**
  - Unit tests for all zodiac sign boundaries
  - Integration tests for complete user flows
  - Edge case testing (leap years, month boundaries)

- [ ] **GUI Enhancement**
  - Migrate to tkinter for graphical interface
  - Date picker widget for easier date selection
  - Display zodiac symbol and traits

- [ ] **Data Structure Optimization**
  ```python
  ZODIAC_SIGNS = {
      "january": [
          {"sign": "Capricornus", "start": 1, "end": 22},
          {"sign": "Aquarius", "start": 23, "end": 31}
      ],
      # ... additional months
  }
  ```

### Long-Term Initiatives
- [ ] **API Development**
  - RESTful API for zodiac determination
  - JSON request/response format
  - Integration with astrology databases

- [ ] **Extended Features**
  - Chinese zodiac sign calculation
  - Lunar zodiac integration
  - Zodiac compatibility checker

- [ ] **Deployment**
  - Docker containerization
  - Cloud-based deployment options
  - Web application version

---

## 👨‍💻 Author

**TROJAN1HAMMER/Harshith B**  
GitHub: [@TROJAN1HAMMER](https://github.com/TROJAN1HAMMER)  
Repository: [zodiac-sign-finder](https://github.com/TROJAN1HAMMER/zodiac-sign-finder)

### Project Timeline
- **Created**: July 1, 2022
- **Last Updated**: July 6, 2022

---

## 📝 License

This project is currently unlicensed. Consider adding a LICENSE file (MIT, Apache 2.0, etc.) for clarity on usage rights.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes and test thoroughly
4. Submit a pull request with clear description

---

## 📞 Support & Feedback

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/TROJAN1HAMMER/zodiac-sign-finder/issues)
- Check existing discussions or start a new discussion
- Review the code and suggest improvements

---

**Last Updated**: June 2022  
*Professional Grade: Entry-Level Python Project with Refactoring Opportunities*
