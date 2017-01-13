# Python traceback signal handler

The library registers a signal handler that will print a traceback into the
stderr upon receiving a given signal.

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
import tbsignal, signal

# this will register the signal handler for SIGUSR1
tbsignal.register_handler()

# this will register the signal handler for SIGINT
tbsignal.register_handler(signal.SIGINT)
```

To trigger the traceback print, simply run the following command from another
terminal:

```
kill -SIGUSR1 pid
```

