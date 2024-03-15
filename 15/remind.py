import matplotlib.pyplot as plt
import numpy as np


korean = {"hong": 50, "lee": 70, "kang": 20}
english = {"hong": 20, "lee": 40, "kang": 60}

names = list(korean.keys())
korean_scores = list(korean.values())
english_scores = list(english.values())


index = np.arange(len(names))


bar_width = 0.35

plt.bar(index, korean_scores, bar_width, label="korean")


plt.bar(index + bar_width, english_scores, bar_width, label="English")


plt.xlabel('name')

plt.ylabel('score')
plt.xticks(index + bar_width / 2, names)
plt.legend()

plt.tight_layout()
plt.show()