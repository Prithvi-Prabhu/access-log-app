import React, { useState } from 'react';
import axios from 'axios';

const AccessLogQuery = () => {
  const [startDateTime, setStartDateTime] = useState('');
  const [endDateTime, setEndDateTime] = useState('');
  const [logs, setLogs] = useState('');

  const handleQuery = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/access-logs/?start_time=${startDateTime}&end_time=${endDateTime}`);
      setLogs(response.data);
    } catch (error) {
      console.error('Error fetching access logs:', error);
    }
  };

  return (
    <div>
      <h2>Access Log Query</h2>
      <div>
        <label>Start Time:</label>
        <input type="datetime-local" value={startDateTime} onChange={(e) => setStartDateTime(e.target.value)} />
      </div>
      <div>
        <label>End Time:</label>
        <input type="datetime-local" value={endDateTime} onChange={(e) => setEndDateTime(e.target.value)} />
      </div>
      <button onClick={handleQuery}>Query Logs</button>
      {logs && (
        <div>
          <h3>Access Logs:</h3>
          <pre>{logs}</pre>
        </div>
      )}
    </div>
  );
};

export default AccessLogQuery;
