
# Shutdown Timer & Alarm

`shutdown_timer` is a simple and user-friendly Python GUI tool that allows you to set a timer or a countdown to automatically shut down your computer. The tool offers a sleek interface with a real-time progress view and allows users to cancel the shutdown at any time.

## Features

- **Timer Shutdown**: Set a timer in minutes to automatically shut down your computer.
- **Countdown to Specific Time**: Set a specific time for the shutdown to occur (alarm-style).
- **Real-Time Progress View**: See the remaining time visualized with a circular progress bar.
- **Shutdown Cancelation**: Option to cancel the shutdown at any time.
- **Dark Mode GUI**: A modern dark-themed interface for a pleasant user experience.

## Requirements

- Python 3.x (if using the source code).
- `tkinter` for the graphical interface (pre-installed with Python on most systems).
(none for the .exe file)

## Installation

### Using the Python Script

1. Clone this repository:

    ```bash
    git clone https://github.com/truelockmc/shutdown_timer.git
    cd shutdown_timer
    ```
3. You are now ready to run the script:

### Using the Executable

If you prefer not to use Python or need a more straightforward setup, you can use the pre-built executable:

1. Download the latest executable file from the repository

2. Double-click the `.exe` file to run the application. No additional setup or installation is required.

## Usage

1. **Setting a Timer:**
    - Enter the number of minutes in the `Set Timer` field and click **Start Timer**. The computer will shut down when the timer reaches zero.

2. **Setting a Countdown (Specific Time):**
    - Enter the target hour and minute in the respective fields under `Hour` and `Minute`, then click **Set Alarm**. The shutdown will occur at the specified time.
   
3. **Canceling the Shutdown:**
    - Once the timer or countdown starts, a progress window appears with a **Cancel Shutdown** button. Clicking this will abort the shutdown and restore the main window.

### Example

- Setting a 15-minute timer:

    ![Timer Example](docs/images/timer_example.png)

- Countdown for a shutdown at 23:30:

    ![Countdown Example](docs/images/countdown_example.png)

## Code Breakdown

- **Main Functionality**: The script provides two main shutdown modes: a minute-based timer or a countdown to a specific time.
- **Progress Window**: Displays a circular progress bar showing the percentage of time remaining.
- **Shutdown Logic**: Once the timer or countdown finishes, the script runs a system command to shut down the computer.

    ```python
    os.system("shutdown /s /t 1")
    ```

- **Cancel Functionality**: The shutdown process can be canceled by clicking the **Cancel Shutdown** button in the progress window.

## Customization

- You can modify the interface, colors, or even add extra functionality by editing the `shutdown_timer.py` file. For example, you can customize the shutdown command to log off or restart the system instead.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
