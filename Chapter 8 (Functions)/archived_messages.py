def send_messages(messages, sent_messages):
    """Print each message and move it to a new list."""
    print("Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

short_messages = ["I am learning python!", "I like pancakes.", "Hi there!", ":D"]
sent_messages = []

# calling function with a copy of the list
send_messages(short_messages[:], sent_messages)

print("\nFinal lists:")
print(short_messages)
print(sent_messages)