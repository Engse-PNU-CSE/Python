from pathlib import Path
import json

numbers = [1, 2, 3, 4, 11, 22, 33]

path = Path('number.json')
contents = json.dumps(numbers)
path.write_text(contents)
print(json.loads(contents))

data = json.loads('{}')