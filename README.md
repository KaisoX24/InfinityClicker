## **Infinity Clicker**

**Infinity Clicker is an automated mouse clicking tool that allows users to simulate mouse clicks at fixed or random intervals. It features customizable settings, including the choice of mouse button, click type (single or double), and the ability to repeat clicks for a specific number of times or until manually stopped. This tool is designed to be efficient and user-friendly with a clean graphical user interface (GUI) built using customtkinter for easy interaction.**



## **🪄 Features**

- **Fixed Interval Clicking:** Set a specific time interval (in hours, minutes, seconds, and milliseconds) between each click.
- **Random Interval Clicking:** Clicks are simulated at random intervals between a minimum and maximum range.
- **Click Type:** Choose between single and double clicks.
- **Repeat Clicking:** Set the number of times the clicks should repeat or choose to repeat until stopped.
- **Mouse Button Selection:** Choose between left, right, or middle mouse button for clicking.
- **Hotkey Support:** Set a customizable hotkey to start and stop the clicking process.
- **Mouse Location Info:** Get the current mouse position in the window.
- **Window Settings:** Customize the window's appearance with light or dark themes, and enable topmost window functionality.


## **💾Installation**

 1. Clone this repository or download the source code.
 2. Ensure you have Python 3.8 or higher installed.
 3. Install the required dependencies:

```bash
  pip install pyautogui keyboard customtkinter
```
4. Place your desired icon (.ico file) in the same directory as the script.

    
## **Usage**
1. Run the infinity_clicker.py script to open the application window.
2. Choose your desired clicking options (interval, click type, button, etc.).
3. Press the Start button to begin clicking or use the defined hotkey to start/stop the clicking process.
4. Use the Stop button to stop the clicking at any time.


## ⚙️Available Settings
### 1. **Interval Type:**
- **Fixed Interval**: Set a fixed interval for clicks, specifying the time in hours, minutes, seconds, and milliseconds.
- **Random Interval**: Define a random range for the click intervals. Set both a minimum and maximum value for the interval.

### 2. **Repeat Options:**
- **Repeat for a Specific Count**: Set how many times the clicks should repeat. Once the count is reached, the clicking stops automatically.
- **Repeat Until Stopped**: The clicking will continue indefinitely until manually stopped by the user.

### 3. **Hotkey:**
- Set a custom hotkey to start or stop the clicking process (default is **F6**). You can change the hotkey at any time using the **"Change Hotkey"** button.

### 4. **Theme:**
- Switch between **Light** and **Dark** themes for the application to suit your preference.

These settings allow you to fully control the behavior and appearance of the auto-clicking tool.

## **Example**

### **1. Basic Setup**
**To set up the fixed interval clicking:**

-  Set the interval to **1 second**.
-  Choose **Single Click** for the click type.
-  Select **Left Mouse Button**.
-  Click **Start** or press the assigned hotkey.

### **2. Random Interval Setup**
**To set up random interval clicking:**
- Set the **minimum** and **maximum** interval values (e.g., 0.5 and 1.5 seconds).
- Choose **Double Click** for the click type.
- Select **Right Mouse Button**.
- Click **Start** or press the assigned hotkey.

These setups will allow you to configure the tool for different types of auto-clicking, either with a fixed interval or a random range of intervals.

### **3. HotKeys**
- **F6**: Start/Stop Clicking (Customizable in settings).

## **GUI OVERVIEW**

- **Interval Settings:** Allows users to set intervals for fixed or random clicking.
- **Button and Click Type Selection:** Choose the mouse button and the type of click (single or double).
- **Repeat Settings:** Choose how many times to repeat or choose to repeat until stopped.
- **Mouse Location:** Displays the current mouse position and allows you to get the position with a button click.
- **Window Settings:** Customize the theme and enable topmost window functionality.

## **👨‍💻Contributions**

Contributions are always welcome!
If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

