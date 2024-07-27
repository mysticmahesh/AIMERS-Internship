from transformers import pipeline
pipe = pipeline("table-question-answering", model="google/tapas-base-finetuned-wtq")
data=[
    {"City":"vijayawada","Population":"84M","Area":"783.8 sq km"},
    {"City": "Hyderabad", "Population": "139M", "Area": "41302 sq km"},
    {"City": "Chennai", "Population": "127M", "Area": "6061.1 sq km"},
    {"City": "Tanuku", "Population": "7M", "Area": "1061.1 sq km"},
    {"City": "Narsapuram", "Population": "09M", "Area": "1561.1 sq km"}
]
question ="which city has largest area ?"
result = pipe(table=data, query = question)
print("Answer:", result['answer'])
