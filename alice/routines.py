from datetime import datetime

def get_time():
    now = datetime.now()
    current_time_str = now.strftime("%I:%M %p")
    speech_text = f"The current time is {current_time_str}"
    return speech_text