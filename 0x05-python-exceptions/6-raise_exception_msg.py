#!/usr/bin/python3
def raise_exception_msg(message=""):
  if not message:
    message = "This is a custom error message."
  raise NameError(message)
