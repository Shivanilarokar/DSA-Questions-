# Project Title

A brief description of what this project does and who it's for.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [What's New](#whats-new)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, you must first install the required dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

## Usage

Here are examples of how to use the newly introduced function within the FastAPI application component:

### FastAPI Webhook

This function sets up a webhook that listens for GitHub events such as push events and pull requests.

```python
from fastapi import FastAPI, Request, Header
import logging
import sys
from typing import Optional

# Setup logger
logger = logging.getLogger("FastAPIWebhook")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Initialize FastAPI
app = FastAPI()

@app.post("/webhook")
async def webhook(
    request: Request,
    x_hub_signature_256: Optional[str] = Header(None),
    x_github_event: Optional[str] = Header(None),
):
    body = await request.body()
    payload = await request.json()
    logger.info("📬 Received %s event", x_github_event)

    # Implementation of event handling can go here
```

### Sample Event Handling

This sample demonstrates how to process different GitHub webhook events:

```python
@app.post("/webhook")
async def webhook(
    request: Request,
    x_hub_signature_256: Optional[str] = Header(None),
    x_github_event: Optional[str] = Header(None),
):
    ...
    if x_github_event == "push":
        bot_user = payload.get("pusher", {}).get("name")
    elif x_github_event == "pull_request":
        bot_user = payload.get("sender", {}).get("login")
    # Process webhook event
    logger.info("📬 Processing webhook event from bot: %s", bot_user)
```

## API Documentation

### `webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None))`

- **Description**: This endpoint processes incoming GitHub webhook events.
- **Parameters**:
  - `request`: The incoming HTTP request.
  - `x_hub_signature_256`: Optional header containing the signature of the webhook.
  - `x_github_event`: Optional header containing the type of the GitHub event.
- **Returns**: None

## What's New

- Introduced a new FastAPI based webhook listener for GitHub events, enabling better integration and automation based on push and pull request events.
- Improved logging throughout the webhook process to assist in debugging and event tracking.

## Contributing

We welcome contributions to this project! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.