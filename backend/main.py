from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from datetime import datetime, timedelta

app = FastAPI()

# Path to the Apache access log file
access_log_path = "/var/log/apache2/access.log"

@app.get("/access-logs/")
def get_access_logs(start_time: str, end_time: str):
    try:
        start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Use '%Y-%m-%d %H:%M:%S'.")

    logs = []
    
    with open(access_log_path, "r") as file:
        for line in file:
            log_time_str = line.split()[3][1:]
            log_datetime = datetime.strptime(log_time_str, "%d/%b/%Y:%H:%M:%S")
            
            if start_datetime <= log_datetime <= end_datetime:
                logs.append(line)

    if not logs:
        raise HTTPException(status_code=404, detail="No logs found within the specified time range.")

    return PlainTextResponse(content="".join(logs), media_type="text/plain")

