import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, AdamW

# Load pre-trained model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Set up training data
train_data = [
    {
        "context": "The quick brown fox jumps over the lazy dog.",
        "question": "What color is the fox?",
        "answer": "brown"
    },
    {
        "context": "The quick brown fox jumps over the lazy dog.",
        "question": "What animal jumps over the dog?",
        "answer": "fox"
    },
    # Add more training examples as needed
]

# Tokenize training data and encode labels
train_encodings = tokenizer(train_data, padding=True, truncation=True, return_tensors="pt")
train_labels = [{"start_positions": tokenizer.encode(d["answer"], add_special_tokens=False)[0],
                 "end_positions": tokenizer.encode(d["answer"], add_special_tokens=False)[-1]} 
                for d in train_data]

# Set up optimizer and loss function
optimizer = AdamW(model.parameters(), lr=5e-5)
loss_fn = torch.nn.CrossEntropyLoss()

# Train the model
for epoch in range(3):
    model.train()
    total_loss = 0
    for i in range(len(train_data)):
        input_ids = train_encodings["input_ids"][i].unsqueeze(0)
        attention_mask = train_encodings["attention_mask"][i].unsqueeze(0)
        start_positions = torch.tensor([train_labels[i]["start_positions"]])
        end_positions = torch.tensor([train_labels[i]["end_positions"]])
        optimizer.zero_grad()
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, start_positions=start_positions, end_positions=end_positions)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch + 1} loss: {total_loss / len(train_data):.3f}")
