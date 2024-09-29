from actual import Actual
from actual.queries import get_transactions, get_categories
from llm import OllamaEngine, PromptGenerator
from config import Config

cfg = Config(env_path=".env")

actual_params = {
    "base_url": cfg.get("ACTUAL_SERVER"),
    "password": cfg.get("ACTUAL_PASSWORD"),
    "encryption_password": "",
    "file": cfg.get("ACTUAL_BUDGET_FILE"),
    "data_dir": "./data",
}

cats = []
transacts = []
with Actual(**actual_params) as actual:
    cats = [c.name for c in get_categories(actual.session)]
    transacts = [t.imported_description for t in get_transactions(actual.session)]

print("Categories:", cats)
print("Number of transactions:", len(transacts))

prompt_gen = PromptGenerator(transactions=transacts, categories=cats)
prompt = prompt_gen.generate_prompt()

engine = OllamaEngine(base_url=cfg.get("LLAMA_SERVER"), model=cfg.get("OLLAMA_MODEL"))
resp = engine.invoke(prompt)

parsed = engine.parse_response(resp)

print("Parsed response: ")
print(parsed)





