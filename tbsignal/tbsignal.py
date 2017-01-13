import sys, traceback, signal

def traceback_signal_handler(file, sig, frame):
    message = "Signal %d received.\n" % sig
    message += "Traceback (most recent call last):\n"
    message += ''.join(traceback.format_stack(frame))
    print(message, file=file)

def register_handler(sig=signal.SIGUSR1, file=sys.stdout):
    signal.signal(sig, lambda s, frm: traceback_signal_handler(file, s, frm))

