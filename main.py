from transformers import AutoModelForCausalLM, AutoTokenizer # import the loaders for a pretrained model and corresponding tokenizer

# load DistilGPT-2 (a lightweight version of GPT-2)
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# init 
topic = "French Revolution"
init_prompt = f"Generate a quiz based on the topic: {topic}"
