message = input("Message: ").strip()

if not message.startswith("ZT:"):
    print("Not a message from planet Zeta")
else:
    # remove ZT: and decode
    text = message[3:].strip()
    text = text.replace("4", "a").replace("3", "e").replace("0", "o").replace("1", "i")

    letters = len(text.replace(" ", ""))
    lower = text.lower()

    # help must be checked first, because a distress call can also say hello
    if "help" in lower:
        kind = "DISTRESS"
    elif "hello" in lower:
        kind = "GREETING"
    elif "?" in lower:
        kind = "QUESTION"
    else:
        kind = "UNKNOWN"

    marks = text.count("!")
    if marks >= 3:
        urgency = "HIGH"
    elif marks >= 1:
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    print(text.upper())
    print("Letters:", letters)
    print("Type:", kind)
    print("Urgency:", urgency)

    reply = "we come in peace"
    reply = reply.replace("a", "4").replace("e", "3").replace("o", "0").replace("i", "1")
    print("EA:", reply)
 # If I checked hello first, "hello earth, we need help" would be GREETING, but it is a distress call, so help comes first.
# Test 1: ZT: h3ll0 34rth, w3 n33d h3lp!!! -> 24 letters, DISTRESS, HIGH
# Test 2: ZT: wh3r3 1s y0ur pl4n3t? -> QUESTION, LOW
# Test 3: ZT: wh4t 1s y0ur n4m3?! -> QUESTION, MEDIUM
# Test 4: hello -> Not a message from planet Zeta