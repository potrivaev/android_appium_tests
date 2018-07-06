## Appium Tests for Android

To launch tests you need:
 - Python 3.6
 - Appium
 - Android SDK
 
 To install Python:
 ```bash
 > sudo apt install python3-minimal
```
 
 To install Appium:
 
 ```bash
  > curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -    # get node.js
  > sudo apt-get install -y nodejs      # get node.js
  > npm install -g appium  # get appium
  ```

To install Android SDK:
```bash
 > sudo apt update && sudo apt install android-sdk
```

To launch test:
1) Create and run emulator in Android SDK or connect real device
2) Launch Appium:
```bash
 > appium .
```
3) Check emulator/device is launched or connected:
```bash
 > adb devices
```
4) Follow these steps:
```bash
 > pip install -r requirements.txt
 > pytest tests/test_log_text_box.py
```