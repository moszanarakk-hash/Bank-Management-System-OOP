import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("จำนวนเงินต้องเป็นตัวเลข")

    if amount <= 0:
        raise ValueError("จำนวนเงินต้องมากกว่า 0")

    return True