# 🎬 CinematicRollingText

A simple Python terminal animation that creates a **cinematic rolling text effect**.

Each character starts at the **bottom of the terminal**, smoothly moves **upward**, and stays at the top once it reaches its final position. The next character then follows the same animation.

## ✨ Demo

The animation looks roughly like this:

```text
Hello, World!
```

But instead of appearing normally:

```text
                H
                e
                l
                l
                o
```

each character travels upward from the bottom and gradually builds the final text.

## 🚀 Features

* 🎬 Cinematic rolling animation
* ⬆️ Characters move from bottom to top
* 🔤 One character appears at a time
* 📌 Characters stay in their final position
* ⚡ Adjustable animation speed
* 💻 Works directly in the terminal
* 🐍 Built entirely with Python's standard library

## 🛠️ Requirements

* Python 3.x
* A terminal / command prompt

No external packages are required.

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/CinematicRollingText.git
```

Go into the project directory:

```bash
cd CinematicRollingText
```

## ▶️ Usage

Run the Python file:

```bash
python main.py
```

Or, depending on your system:

```bash
python3 main.py
```

## ⚙️ Customization

You can change the text, animation speed, and rolling distance.

For example:

```python
rolling_text_perfect(
    "Hello, World!",
    speed=0.1,
    lines=10
)
```

### Parameters

| Parameter | Description                                    |
| --------- | ---------------------------------------------- |
| `text`    | Text you want to animate                       |
| `speed`   | Delay between animation frames                 |
| `lines`   | Number of terminal lines the character travels |

### Example

```python
rolling_text_perfect(
    "Welcome to my project!",
    speed=0.08,
    lines=15
)
```

Lower `speed` values make the animation faster.

## 📂 Project Structure

```text
Cinematic_Rolling_Text_Terminal/
│
├── Cinematic.py
└── README.md
```

## 🧠 How It Works

The program:

1. Clears the terminal.
2. Places the current character at the bottom.
3. Moves the character upward frame by frame.
4. Keeps previously completed characters at the top.
5. Repeats the process for the next character.
6. Eventually forms the complete message.

## 🎯 Example

Starting:

```text
            H
```

Then:

```text
            H
             e
```

Then:

```text
            He
              l
```

Eventually:

```text
                Hello, World!
```

## 🤝 Contributing

Feel free to fork this project and experiment with:

* Different animation styles
* Colors
* Fade effects
* Sound effects
* Randomized animation speeds
* ASCII art
* Multiple lines of text

Pull requests and suggestions are welcome!

## 📜 License

This project is open source and available under the **MIT License**.

---

⭐ If you like this little animation, consider giving the repository a star!
