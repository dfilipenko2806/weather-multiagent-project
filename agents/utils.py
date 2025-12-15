# agents/utils.py
import re

def parse_numbered_list(text: str):
    """
    Извлекает элементы списка из текста, даже если они в одной строке или с лишними символами.
    """
    # разделяем по переносу строки и номерам с точкой или скобкой
    lines = re.split(r'\n|(?<=\d)[\.\)]\s', text)
    items = []
    for line in lines:
        line = line.strip("-1234567890. ) ").strip()
        if line:
            items.append(line)
    # fallback: если список пуст, разбиваем по запятым
    if not items and ',' in text:
        items = [x.strip() for x in text.split(',') if x.strip()]
    return items
