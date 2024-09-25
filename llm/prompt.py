class PromptGenerator():
    def __init__(self, transactions = [], categories = []):
        self.output_schema_example = [{
            "transaction": "{name of transaction}",
            "category": "{category}"
        },
        {
            "transaction": "{name of transaction}",
            "category": "{category}"
        }]
        self.transactions = ",".join(transactions)
        self.categories = ",".join(categories)
    
    def generate_prompt(self):
        prompt = f"""   
        Given the following transactions: {self.transactions}, 
        categorize each transaction into one of the following categories: {self.categories}.
        Return the response as a list of key-values formatted in JSON like this for all the transactions:
        {{
            'data': [
            {{'transaction': '[name of transaction]', 'category': '[category]'}},
            {{'transaction': '[name of transaction]', 'category': '[category]'}}
            ...
            ]
        }}
        return only JSON formatted answer, no other format is accepted, no intro text and no output text.
        """
        return prompt