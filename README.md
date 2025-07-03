# 🎿 Advanced Python CLI Logger with Sound Alerts, Styled Tracebacks & Email Notifications

This is a **production-ready error logging system** designed for serious Python CLI apps and automation tools.\
It delivers **instant feedback**, ensuring you never miss a bug.

---

## ✨ Key Features — Why Developers Love This System

| Feature                      | Status     |
| ---------------------------- | ---------- |
| 🎨 Styled Terminal Logs      | ✅ Included |
| ⚡ Auto Traceback Hooking     | ✅ Included |
| 🔊 Sound Alerts for Errors   | ✅ Included |
| 🗑️ Rotating File Logging    | ✅ Included |
| 📧 Email Error Notifications | ✅ Optional |

---

## 🚀 Why Use This?

This system is crafted for developers who need:

- Instant error detection (sound + styled logs)
- Auto traceback logging (no manual setup)
- Robust file logging with daily rotation
- Optional email alerts for critical failures
- Seamless integration into CLI tools, AI apps, automation bots, and more.

---

## 📦 Setup Instructions

1. Clone or download this repository.
2. Install required dependencies:

```bash
pip install playsound rich
```

3. Adjust SMTP settings for email alerts (if needed).

---

## ✅ Quick Start Example

```python
from cli_logger_with_alerts import attach_global_traceback, launch_loader

attach_global_traceback()  # Auto-hook global exception logger
launch_loader()            # Your CLI tool’s main function
```

---

## 💡 Why It’s Special

Unlike basic loggers, this system:

- Plays real **sound alerts** for instant feedback
- Shows beautiful, colored tracebacks in terminal
- Logs errors automatically to both console & files
- Works out-of-the-box for CLI apps, bots, and automation tools

---

## 💬 Questions? Contributions?

- Feel free to open an **Issue** or start a **Discussion** on GitHub.
- You can also connect with me on [**LinkedIn**](https://www.linkedin.com/in/your-profile/) for collaboration or questions.

---

## 📜 License

MIT — Free to use, modify, and enhance in your own projects.

---

> 🚀 Ready to improve your CLI debugging?\
> ⭐ Star this repo and start integrating today!

