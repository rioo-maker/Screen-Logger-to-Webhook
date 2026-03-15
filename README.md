# Screen Logger to Discord Webhook

⚠️ **Warning**

Do **NOT** run this program on your main computer, if you want to test if it work you can.
This project is provided **for educational and research purposes only**.

Restarting your computer will stop the screen logger.

---

## Description

A **screen logger** is a type of malware that secretly captures screenshots of a user's computer and sends them to a remote server.

In this project, screenshots are automatically sent to a **Discord webhook**.
This allows the receiver to see what is happening on the target computer in near real time.

This demonstrates how attackers could monitor activity and potentially capture sensitive information such as:

* passwords
* messages
* private data
* on-screen activity

---

## Purpose

The goal of this repository is **educational**:

* understand how screen capture malware works
* learn about common data exfiltration techniques
* raise awareness about cybersecurity threats

---

## Disclaimer

This project is intended **only for educational and cybersecurity research purposes**.

The author is **not responsible** for any misuse of this code.
Do not use this software on systems without explicit permission.

---

## How it works (concept)

1. Capture a screenshot of the screen.
2. Convert the screenshot into an image file.
3. Send the image to a **Discord webhook**.
4. Repeat the process at a defined interval.

---

## Educational reminder

Always protect your system by:

* installing software only from trusted sources
* using antivirus / endpoint protection
* monitoring network activity
* keeping your system updated
