# Termux DDoS Script

## Disclaimer
This script is intended for educational purposes only. Unauthorized use of this script to conduct Distributed Denial of Service (DDoS) attacks is **illegal** and punishable by law. Use this script responsibly and with permission from target network owners.

## Overview
This is a lightweight, asynchronous DDoS attack script optimized for use on Termux. It uses Python’s `aiohttp` and `asyncio` to perform thousands of simultaneous HTTP requests to flood a target.

### Features
- **Asynchronous Requests**: High-speed, efficient requests without heavy system load.
- **Randomized User-Agent Headers**: Avoid detection with randomized requests.
- **Proxy Support**: Enhance anonymity by routing traffic through proxy servers.
- **GET/POST Requests**: Mix between GET and POST requests for a more versatile attack.

## Setup Instructions

### 1. Install Termux
If you don't already have Termux installed, download it from [Termux's official page](https://termux.com/).

### 2. Update and Install Python
First, update Termux and install Python by running the following commands:
```bash
pkg update
pkg install python
