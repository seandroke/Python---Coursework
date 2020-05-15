def new_split_iter(expr): 

   """divide a character string into individual tokens, which need not be separated by spaces (but can be!)

   also, the results are returned in a manner similar to iterator instead of a new data structure

   """

   expr = expr + ";"                # append new symbol to mark end of data, for simplicity
   pos = 0                             # begin at first character position in the list
   while expr[pos] != ";":         # repeat until the end of the input is found
       token = ""
       if expr[pos].isdigit():
           while expr[pos].isdigit():
               token = token + expr[pos]
               pos = pos + 1
           yield token
       elif expr[pos] == " ":
           pos = pos + 1
       else:
          if expr[pos+1] == '=':
             yield expr[pos:pos + 2]
             pos += 1
          else:
             token = expr[pos]
             yield token
          pos = pos + 1

   yield ";"                             # inform client of end of data


