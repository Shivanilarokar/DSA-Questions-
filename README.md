```markdown
# Webhook Processor

## Overview
The Webhook Processor is a FastAPI-based application designed to handle webhook events from GitHub, allowing for efficient integration and automation in development workflows. The application listens for push and pull request events, logging relevant information for further processing.

## What's New
- **Added**: Enhanced logging functionality to capture incoming webhook data.
- **Added**: An endpoint to handle webhook events with improved request handling.
- **Updated**: API documentation to reflect changes in function signatures and workflows.

## Getting Started
To get started, you'll need to clone the repository and install the required packages. Ensure you have Python 3.7+ and FastAPI installed.

```bash
git clone https://github.com/yourusername/webhook-processor.git
cd webhook-processor
pip install fastapi uvicorn
```

### Running the Application
To run the FastAPI application, execute:

```bash
uvicorn quote:app --host 0.0.0.0 --port 8000 --reload
```

### Webhook Endpoint
The webhook endpoint is now defined as:

```python
@app.post("/webhook")
async def webhook(request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None)):
    # Process the incoming webhook event here
```

### Example Usage
Here is how to send a test webhook event to the webhook URL:

```bash
curl -X POST "http://localhost:8000/webhook" \
-H "Content-Type: application/json" \
-H "X-Hub-Signature-256: your_signature" \
-H "X-Github-Event: push" \
-d '{"pusher": {"name": "user"}, "action": "created"}'
```

### Logging
The application now includes a logging setup to track incoming requests and processes efficiently, logging at the INFO level.

## API Documentation
### webhook
#### Parameters
- `request`: The HTTP request object containing the payload.
- `x_hub_signature_256`: Optional signature for validating the request.
- `x_github_event`: The type of GitHub event (e.g., push, pull_request).

## Deprecated Functions
- None at the moment. All functionality has been revised and updated.

## Contribution
Contributions are welcome! Please create a pull request or raise an issue if you find bugs or have suggestions.
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```