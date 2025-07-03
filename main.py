"""
🎧 Advanced Python CLI Logger with Sound Alerts, Styled Tracebacks & Email Notifications
Author: [Amit Kumar]
"""

import os
import sys
import json
import logging
import traceback
from logging.handlers import TimedRotatingFileHandler
from playsound import playsound, PlaysoundException
from rich.console import Console
from rich.traceback import Traceback
from smtplib import SMTP
from email.mime.text import MIMEText

# === Setup Console ===
console = Console()

# === Logger Setup ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name="cli_logger", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)-8s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        file_handler = TimedRotatingFileHandler(
            os.path.join(LOG_DIR, f"{name}.log"),
            when="midnight",
            backupCount=7,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)-8s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()

# === Sound Map Loader ===
SOUND_MAP = {
    "alert": "sounds/alert.wav",
    "file_error": "sounds/error.wav",
}

def safe_play_sound(key, silent=False):
    try:
        file_path = SOUND_MAP[key]
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Sound file missing: {file_path}")
        playsound(file_path)
        logger.debug(f"🔊 Played sound: {key} → {file_path}")
    except Exception as e:
        tb_text = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(f"❌ [{type(e).__name__}] {key} → {file_path} :: {e}\n{tb_text}")
        if not silent:
            console.print(Traceback.from_exception(type(e), e, e.__traceback__))
        # Optionally, re-raise or handle differently here

# === Global Exception Handler ===
def custom_exception_handler(exc_type, exc_value, exc_traceback):
    console.rule("🚨 Unhandled Exception")
    tb = Traceback.from_exception(exc_type, exc_value, exc_traceback)
    console.print(tb)
    logger.critical(f"{exc_type.__name__}: {exc_value}")
    safe_play_sound("alert", silent=True)

def attach_global_traceback():
    sys.excepthook = custom_exception_handler

# === Email Alert Sender ===
def send_error_email(subject, body, recipient, smtp_host="smtp.example.com", smtp_port=587):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "noreply@example.com"
    msg["To"] = recipient

    with SMTP(smtp_host, smtp_port) as smtp:
        smtp.starttls()
        smtp.login("your_email@example.com", "password_here")
        smtp.send_message(msg)
    logger.info("📧 Error email sent successfully.")

# === Example CLI Loader ===
def launch_loader():
    logger.info("🚀 CLI App Started.")
    safe_play_sound("file_error")  # Deliberate error for demo

if __name__ == "__main__":
    attach_global_traceback()
    try:
        launch_loader()
    except Exception:
        raise SystemExit("[ABORT] CLI crashed during startup.")
