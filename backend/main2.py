from fastapi import FastAPI, HTTPException, Query

from typing import List, Optional

from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware

import re



app = FastAPI()



app.add_middleware(

    CORSMiddleware,

    allow_origins=["http://localhost:3000"],  # Replace with the actual origin of your React app

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)



# Function to read and filter access logs

def get_filtered_logs(start_time: Optional[datetime], end_time: Optional[datetime]) -> List[str]:

    log_entries = []

    log_file_path = '/var/log/apache2/access.log'

  # Replace with the actual path to your access log file



    try:

        with open(log_file_path, 'r') as file:

            for line in file:

                log_time_str = re.search(r'\[(.*?)\]', line).group(1)

                log_time = datetime.strptime(log_time_str, '%d/%b/%Y:%H:%M:%S %z')

                if (start_time is None or start_time <= log_time) and (end_time is None or log_time <= end_time):

                    log_entries.append(line.strip())

    except FileNotFoundError:

        raise HTTPException(status_code=404, detail="Access log file not found.")



    return log_entries



# API endpoint to get filtered logs

@app.get("/filtered-logs/")

async def read_filtered_logs(

    start_time: Optional[datetime] = Query(None, alias="start_time", description="Start time for filtering"),

    end_time: Optional[datetime] = Query(None, alias="end_time", description="End time for filtering")

):

    logs = get_filtered_logs(start_time, end_time)

    return {"filtered_logs": logs}



# Run the FastAPI app with Uvicorn

if __name__ == "__main__":

    import uvicorn



    uvicorn.run(app, host="127.0.0.1", port=8000)
