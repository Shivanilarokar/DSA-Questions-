# Project Title

## What's New
- Introduced a new asynchronous `webhook` function to handle incoming requests from GitHub webhook events.
- Updated the header argument descriptions to enhance clarity regarding optional parameters.

## Getting Started
To get started with the project, follow these simple steps.

### Installation
Ensure you have the following dependencies installed:
```bash
pip install fastapi
```

### Usage
Here’s how to use the newly added `webhook` function:

```python
from fastapi import FastAPI, Request, Header
from typing import Optional

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None)):
    # Your logic here
    return {"message": "Webhook received"}
```

### API Documentation
#### `webhook`
```python
async def webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None)):
```
- **Parameters**:
  - `request` (Request): The incoming request object.
  - `x_hub_signature_256` (Optional[str]): GitHub signature for request validation.
  - `x_github_event` (Optional[str]): The event type (e.g., push, pull request).
  
This function asynchronously processes GitHub webhook events and returns a confirmation message.

## License
This project is licensed under the MIT License - see the LICENSE file for details.