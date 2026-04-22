# IP Log Analyzer + Reputation Checker

Parses a sample auth log to detect failed login attempts, flags suspicious IPs, and checks them against the AbuseIPDB threat intelligence API.

## What it does

**Log Parser (`IP_address_loop.py`)**
- Scans the log file for failed login attempts
- Displays the IP address, username, and timestamp for each failure
- Flags any IP with 3 or more failures
- Shows total failure count

**Reputation Checker (`reputation checker.py`)**
- Takes the flagged IPs from the log parser
- Makes an API call to AbuseIPDB for each one
- Returns abuse confidence score, ISP, country code, and last reported date

## Setup

1. Sign up for a free API key at [abuseipdb.com](https://www.abuseipdb.com)
2. Create a `.env` file in the project folder:
   ```
   ABUSEIPDB_API_KEY=your_key_here
   ```
3. Install dependencies:
   ```
   pip install requests python-dotenv
   ```

## Usage

Run the log parser first, then the reputation checker:

```bash
python IP_address_loop.py
python "reputation checker.py"
```
