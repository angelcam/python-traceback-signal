import sys, traceback, signal

def traceback_signal_handler(sig, frame):
    message = "Signal %d received.\n" % sig
    message += "Traceback (most recent call last):\n"
    message += ''.join(traceback.from_stack(frame))
    print(message, file=sys.stderr)

def register_handler(sig=signal.SIGUSR1):
    signal.signal(sig, traceback_signal_handler)

