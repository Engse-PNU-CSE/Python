def send_msg(str, sent_msgs):
    while str:
        sent_msg = str.pop()
        print(f"sent msg : {sent_msg}")
        sent_msgs.append(sent_msg)
def show_msgs(show_msg):
    n=1
    for msg in show_msg:
        print(f"{n}: {msg}")
        n+=1

msgs = ["hi", "hello", "java", "World"]
sent_msgs = []
send_msg(msgs[:], sent_msgs)
print("send messages...")
show_msgs(msgs)
print("sent messages...")
show_msgs(sent_msgs)