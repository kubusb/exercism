from datetime import datetime

class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change

def create_entry(date, description, change):
    return LedgerEntry(date, description, change)

LOCALE_FORMATS = {
    'en_US': {'date': '%m/%d/%Y', 'header': "Date       | Description               | Change       "},
    'nl_NL': {'date': '%d-%m-%Y', 'header': "Datum      | Omschrijving              | Verandering  "}
}

CURRENCY_SYMBOLS = {'USD': '$', 'EUR': '€'}

def format_description(description):
    return f"{description[:22]}..." if len(description) > 25 else f"{description:<25}"

def format_change(change, currency, locale):
    symbol = CURRENCY_SYMBOLS[currency]
    abs_change = abs(change) / 100
    
    if locale == 'en_US':
        formatted = f"{symbol}{abs_change:,.2f}"
        return f"({formatted})".rjust(13) if change < 0 else f"{formatted} ".rjust(13)
    elif locale == 'nl_NL':
        formatted = f"{abs_change:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return f"{symbol} -{formatted} ".rjust(13) if change < 0 else f"{symbol} {formatted} ".rjust(13)

def format_entries(currency, locale, entries):
    if locale not in LOCALE_FORMATS or currency not in CURRENCY_SYMBOLS:
        raise ValueError(f"Unsupported locale or currency")

    entries.sort(key=lambda e: (e.date, e.change, e.description))
    lines = [LOCALE_FORMATS[locale]['header']]
    
    for entry in entries:
        date_str = entry.date.strftime(LOCALE_FORMATS[locale]['date'])
        description_str = format_description(entry.description)
        change_str = format_change(entry.change, currency, locale)
        lines.append(f"{date_str} | {description_str} | {change_str}")

    return "\n".join(lines)
