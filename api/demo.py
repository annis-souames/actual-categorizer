from actual import Actual
from actual.queries import get_transactions, get_categories

with Actual(
    base_url="",  # Url of the Actual Server
    password="",  # Password for authentication
    encryption_password=None,    # Optional: Password for the file encryption. Will not use it if set to None.
    file="",  # Set the file to work with. Can be either the file id or file name, if name is unique
    data_dir="./data",  # Optional: Directory to store downloaded files
) as actual:
    cats = get_categories(actual.session)
    print("Categories:")
    for c in cats:
        print(c.name)
    transactions = get_transactions(actual.session)
    for t in transactions:
        account_name = t.account.name if t.account else None
        category = t.category.name if t.category else None
        print(t.date, t.imported_description, account_name, t.notes, t.amount, category)