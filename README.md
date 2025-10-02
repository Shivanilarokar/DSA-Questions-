```markdown
# Project Title

## Overview
Brief description of the project, its purpose, and functionalities.

## What's New
- **Added** a new async webhook function to handle incoming GitHub webhooks.
- **Updated** the API documentation to reflect new parameter signatures.
- **Deprecated** any existing synchronous methods related to webhook handling.

## Getting Started
To get started with this project, follow the instructions below.

### Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/username/repo.git
   ```
2. Navigate to the project directory.
   ```bash
   cd repo
   ```
3. Install necessary dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Webhook Handler
The new webhook function can be utilized to handle incoming requests from GitHub. Below is an example of how to use the latest `webhook` function.

```python
from fastapi import FastAPI, Request, Header
from your_module import webhook

app = FastAPI()

@app.post("/webhook/")
async def handle_webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None)):
    response = await webhook(request, x_hub_signature_256, x_github_event)
    return response
```

## API Documentation
### `async def webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None))`
This asynchronous function processes incoming webhook requests from GitHub.

- **Parameters:**
  - `request` (Request): The incoming HTTP request object.
  - `x_hub_signature_256` (Optional[str]): The signature for validating the request. Default is None.
  - `x_github_event` (Optional[str]): The GitHub event type of the webhook. Default is None.

### Deprecated Functions
- Any previously used synchronous webhook handling methods have been deprecated and should be removed from your codebase to ensure compatibility with the latest updates.

## License
Specify the license under which the project is released.
```

This README summarizes the updates made to the project, providing new usage examples, updated API documentation, and clear indications of deprecated functions.