from actual import Actual
from actual.queries import get_transactions, get_categories
from config import Config

cfg = Config(env_path=".env")

with Actual(
    base_url=cfg.get("ACTUAL_SERVER"),
    password=cfg.get("ACTUAL_PASSWORD"),
    encryption_password="",
    file=cfg.get("ACTUAL_BUDGET_FILE"),
    data_dir="./data",
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