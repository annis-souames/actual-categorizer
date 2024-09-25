"""
Very simple test script to test the OllamaEngine class.
Should be converted to a proper unit test.
"""

from llm import OllamaEngine, PromptGenerator
from api import Actual

import pdb

def test_ollama_engine():
    engine = OllamaEngine()
    print("Connection state: ",engine.check_connection())
    resp = engine.invoke("Hello, how are you?")
    print("Response: ", resp.status_code)
    print(resp.json())
    print("Parsed response: ")
    print(engine.parse_response(resp))

def prompt_test():
    generator = PromptGenerator(
        transactions=["Netflix", "REWE", "Aldi" ,"Deutsche Bahn", "AirBnb", "Amazon", "Kebab shop"], 
        categories=["Groceries", "Entertainment", "Transport", "Shopping", "Food", "Unknown"]
    )
    print(generator.generate_prompt())


def test_llm():
    engine = OllamaEngine()
    print("Connection state: ",engine.check_connection())
    prompt_gen = PromptGenerator(
        transactions=["Netflix", "REWE", "Aldi" ,"Deutsche Bahn", "AirBnb", "Amazon", "Kebab shop"], 
        categories=["Groceries", "Entertainment", "Transport", "Shopping", "Food", "Unknown"]
    )
    prompt = prompt_gen.generate_prompt() 
    resp = engine.invoke(prompt)
    pdb.set_trace()
    print("Response: ", resp.status_code)
    print(resp.json())
    parsed = engine.parse_response(resp)
    print("Parsed response: ")
    print(parsed)

def test_actual():



if __name__ == "__main__":
    #test_ollama_engine()
    prompt_test()
    test_llm()
