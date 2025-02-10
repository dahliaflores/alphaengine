import time
import ctypes
import threading
from datetime import datetime, timedelta
from plyer import notification

class AlphaEngine:
    def __init__(self):
        self.events = []

    def add_event(self, name, event_time, message, alert_type="info"):
        """
        Add an event to the schedule.

        :param name: Name of the event
        :param event_time: Time for the event (datetime object)
        :param message: Message to display
        :param alert_type: Type of alert (info, warning, error)
        """
        self.events.append({
            'name': name,
            'time': event_time,
            'message': message,
            'type': alert_type
        })
        print(f"Event '{name}' added for {event_time}.")
    
    def remove_event(self, name):
        """Remove an event by its name."""
        self.events = [event for event in self.events if event['name'] != name]
        print(f"Event '{name}' removed.")

    def show_notification(self, title, message, alert_type):
        """Display a notification on Windows."""
        notification.notify(
            title=title,
            message=message,
            app_name='AlphaEngine',
            timeout=10
        )

    def alert_user(self, event):
        """Alert the user with a message box."""
        mb_type = {
            "info": 0x40,
            "warning": 0x30,
            "error": 0x10
        }
        ctypes.windll.user32.MessageBoxW(0, event['message'], f"AlphaEngine - {event['name']}", mb_type.get(event['type'], 0x40))

    def schedule_events(self):
        """Continuously check for events to trigger."""
        while True:
            now = datetime.now()
            for event in self.events.copy():
                if now >= event['time']:
                    self.alert_user(event)
                    self.show_notification(event['name'], event['message'], event['type'])
                    self.events.remove(event)
            time.sleep(60)  # Check every minute

    def start(self):
        """Start the AlphaEngine scheduler."""
        print("AlphaEngine started.")
        schedule_thread = threading.Thread(target=self.schedule_events)
        schedule_thread.daemon = True
        schedule_thread.start()

if __name__ == "__main__":
    engine = AlphaEngine()
    
    # Example usage:
    # Schedule an event 1 minute from now
    future_time = datetime.now() + timedelta(minutes=1)
    engine.add_event("Meeting", future_time, "Attend the project meeting.", "info")
    
    # Start the event scheduler
    engine.start()
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("AlphaEngine stopped.")