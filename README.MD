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
  > curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
  > sudo apt-get install -y nodejs      # get node.js
  > npm install -g appium  # get appium
  > npm install wd         # get appium client
  > appium &               # start appium 
  ```

To install Android SDK:
```bash
 > sudo apt update && sudo apt install android-sdk
```

To launch test:
```bash
 > pip install requirements.txt
 > pytest tests/test_log_text_box.py
```