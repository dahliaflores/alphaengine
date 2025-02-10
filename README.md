# AlphaEngine

AlphaEngine is a Python-based program designed to customize and schedule alerts for reminders, appointments, or system events on Windows. With AlphaEngine, you can set up notifications to remind you of important tasks or events at specified times.

## Features

- Schedule reminders for any date and time.
- Customize messages for each event.
- Choose the type of alert: information, warning, or error.
- Receive both desktop notifications and message box alerts.

## Installation

Before running AlphaEngine, ensure you have Python installed along with the required packages:

1. Install [Python](https://www.python.org/downloads/)
2. Install the required Python package using pip:
   ```bash
   pip install plyer
   ```

## Usage

1. Clone the repository or download the `alpha_engine.py` file.
2. Run the script using Python:
   ```bash
   python alpha_engine.py
   ```
3. Add events by modifying the example usage section in the `alpha_engine.py` script:
   ```python
   future_time = datetime.now() + timedelta(minutes=1)
   engine.add_event("Meeting", future_time, "Attend the project meeting.", "info")
   ```

4. The scheduler will run in the background and alert you when the event time is reached.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License.

## Acknowledgements

- This program uses the `plyer` library to handle notifications on Windows.