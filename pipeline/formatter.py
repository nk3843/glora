import pandas as pd

def format_event(row: pd.Series) -> str:
    date = row["SQLDATE"].strftime("%Y-%m-%d")
    actor1 = row.get("Actor1Name", "Unknown")
    actor2 = row.get("Actor2Name", "Unknown")
    code = row.get("EventCode", "N/A")
    tone = row.get("AvgTone", 0.0)
    mentions = row.get("NumMentions", 0)
    return f"{date}: Event {code} between {actor1} and {actor2}. Tone: {tone}, Mentions: {mentions}."
