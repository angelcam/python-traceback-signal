# Python traceback signal handler

The library registers a signal handler that will print a traceback into the
stdout upon receiving a given signal.

## Installation

Add the following line into your requirements.txt:

```
git+https://bitbucket.org/angelcam/python-traceback-signal.git#egg=tbsignal
```

and run:

```
pip3 install -r requirements.txt
```

## Usage

To register the signal handler, simply call the following function:

```
import tbsignal, signal, sys

# this will register the signal handler for SIGUSR1
tbsignal.register_handler()

# this will register the signal handler for SIGINT and print the output to
# stderr
tbsignal.register_handler(signal.SIGINT, sys.stderr)
```

To trigger the traceback print, simply run the following command from another
terminal:

```
kill -SIGUSR1 pid
```

