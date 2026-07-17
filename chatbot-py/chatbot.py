"""
Project 1: Rule-Based AI Chatbot

Architecture: IPO model (Input -> Process -> Output)
  INPUT   -> continuous while loop + sanitization
  PROCESS -> dictionary lookup (O(1)) with .get() fallback
  OUTPUT  -> printed response
"""
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Good to see you.",
    "how are you": "I run on pure logic, so I'm always stable. How about you?",
    "what is your name": "I'm a rule-based bot built for DecodeLabs Project 1.",
    "help": "I answer greetings and a few commands. Type 'exit' to quit.",
    "thanks": "You're welcome!",
}

# FALLBACK: default response for anything not in the knowledge base.
FALLBACK = "I'm not sure how to respond to that yet."

# EXIT STRATEGY: any of these triggers a clean break out of the loop.
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}


def get_response(clean_input):
    """Atomic lookup + fallback in a single operation (the .get() method)."""
    return responses.get(clean_input, FALLBACK)


def main():
    print("Bot: Hello! I'm your rule-based assistant. Type 'exit' to quit.")

    # INPUT LOOP: the "heartbeat" and runs until the kill command.
    while True:
        raw_input_text = input("You: ")

        # SANITIZATION: normalize case and strip whitespace.
        clean_input = raw_input_text.lower().strip()

        # Guard against an empty line.
        if not clean_input:
            print("Bot: Say something and I'll try to help.")
            continue

        # EXIT STRATEGY: clean break.
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Take care.")
            break

        print("Bot:", get_response(clean_input))


if __name__ == "__main__":
    main()