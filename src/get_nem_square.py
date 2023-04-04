import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        nem = int(num)
    except Exception:
        exit()
else:
    num = 1
    
print(f"::set-output name=num_squared::{nem **2}")
