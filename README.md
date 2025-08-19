
---

## 🧠 Theoretical Framework

The engine is grounded in **Screenplectics**, an emergent screenplay theory that formalizes screenplay components (e.g., action, dialogue, transitions, sluglines) as computable states. The parser uses a **state machine + regex hybrid model** to resolve ambiguous screenplay elements, allowing flexibility without violating professional formatting standards.

Key principles:

- **Symbolic State Parsing:** Each screenplay element (e.g., slugline, action, dialogue) is mapped to a distinct parser state.
- **Deterministic Flow:** Scenes are sequenced and normalized using structural grammar patterns.
- **Format-Preserving Validation:** Outputs are canonicalized to .txt or .pdf with strict indentation and spacing.

---

## ⚙️ Features

- ✅ Format-free text → professionally formatted screenplay
- 🧾 Slugline parsing (INT./EXT., location, time)
- 🎭 Dialogue formatting with intelligent speaker detection
- 🎬 Action block recognition and spacing control
- 🗂️ Output-ready for PDF, TXT, and integration with Final Draft (.fdx planned)
- 🧪 Unit-tested parsing logic

---

## 🧪 Getting Started

### 🖥️ Prerequisites
- Python 3.8+
- Git
- Recommended: `virtualenv` or `venv`

### 💾 Installation

```bash
git clone https://github.com/Abraham75/Screenplay.git
cd Screenplay
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
