def show_messages(messages):
    print("All messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to a new list."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

short_messages = ["I am learning python!", "I like pancakes.", "Hi there!", ":D"]
sent_messages = []

show_messages(short_messages)
send_messages(short_messages, sent_messages)

# making sure messages got moved correctly
print("\nFinal lists:")
print(f"Messages: {short_messages}")
print(f"Sent messages: {sent_messages}")