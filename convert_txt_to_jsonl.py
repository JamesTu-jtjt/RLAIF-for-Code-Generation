import jsonlines
import os
import sys
import json
import ast
all_files = os.listdir("Manual_Iterative_Refinement_James/InitialFail_but_Pass5/")
#print(all_files)
correct_code = []
for file in all_files:  
  with open('Manual_Iterative_Refinement_James/InitialFail_but_Pass5/'+file,'r') as f:
    correct_code.append(ast.literal_eval(f.read()))
print(len(correct_code))
print(type(correct_code[0]))
with jsonlines.open('train_ifpu_v2.jsonl', 'w') as writer:
    writer.write_all(correct_code)