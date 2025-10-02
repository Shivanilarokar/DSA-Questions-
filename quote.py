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
