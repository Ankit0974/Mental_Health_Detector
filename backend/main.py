from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

MODEL_PATH = "../model/bert_model"

# Load model + tokenizer
model = BertForSequenceClassification.from_pretrained(
    "ankitml01/mental-health-model"
)

tokenizer = AutoTokenizer.from_pretrained(
    "ankitml01/mental-health-model"
)

device = torch.device("cpu")  # Use CPU for API
model.to(device)
model.eval()


class TextInput(BaseModel):
    text: str


@app.post("/predict")
def predict(data: TextInput):
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)

    suicide_prob = probs[0][1].item()
    non_suicide_prob = probs[0][0].item()


    if suicide_prob > 0.75:
        risk = "High Risk"
    elif suicide_prob > 0.45:
        risk = "Moderate Risk"
    else:
        risk = "Low Risk"

    return {
        "suicide_probability": round(suicide_prob, 4),
        "non_suicide_probability": round(non_suicide_prob, 4),
        "risk_level": risk,
        "note": "This tool is an AI-based screening system and not a medical diagnosis."
    }