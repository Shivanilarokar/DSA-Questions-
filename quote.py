import random

quotes = [
    "🌟 Believe in yourself and all that you are.",
    "🔥 Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "🌱 Do something today that your future self will thank you for.",
    "💡 Great things never come from comfort zones.",
    "🏆 Don’t stop when you’re tired. Stop when you’re done.",
    "🌍 Your limitation—it’s only your imagination.",
    "🚀 Push yourself, because no one else is going to do it for you."
]

def random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("💭 Random Inspiration for You:\n")
    print(random_quote())



FastAPI, Request, Header import logging, sys, traceback, json from typing import Optional from Src.Diffhelperfunc import ( fetch_pr_files_via_rest, fetch_push_diffs_via_compare, build_diffs_from_rest_filelist, ) # Import orchestrator wrapper from Src.agents.orchestrator import orchestrator # ---------------- Logging setup ---------------- logger = logging.getLogger("FastAPIWebhook") handler = logging.StreamHandler(sys.stdout) formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s") handler.setFormatter(formatter) logger.addHandler(handler) logger.setLevel(logging.INFO) # ---------------- FastAPI ---------------- app = FastAPI() @app.post("/webhook") async def webhook( request: Request, x_hub_signature_256: Optional[str] = Header(None), x_github_event: Optional[str] = Header(None), ): body = await request.body() payload = await request.json() try: state = None # --- Auto detect bot user --- bot_user = None if x_github_event == "push": bot_user = payload.get("pusher", {}).get("name") elif x_github_event == "pull_request": bot_user = payload.get("sender", {}).get("login") logger.info("📬 Received %s event from %s (action=%s)", x_github_event, bot_user, payload.get("action")) # ---------- Pull Request ---------- if x_hub_signature_256 is not None and x_github_event == "pull_request": action = payload.get("action") if acti