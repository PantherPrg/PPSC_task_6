def passwords(attempt):
  # write your code here
  req1 = False
  req2 = False
  req3 = (7 <= len(attempt) <= 25)

  for char in attempt:
    if char == "_" or char == ".":
      pass
    elif 48 <= ord(char) <= 57:
      pass
      req1 = True
    elif 65 <= ord(char) <= 90:
      pass
      req2 = True
    elif 97 <= ord(char) <= 122:
      pass
    else:
      return "invalid\n"

  if req1 and req2 and req3:
    return "valid\n"
  else:
    return "invalid\n"