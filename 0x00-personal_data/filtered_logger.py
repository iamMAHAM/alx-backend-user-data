#!/usr/bin/env python3
"""
module : filter_datum
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        log = re.sub(fr'{field}=.+?{separator}',
                     f'{field}={redaction}{separator}', message)
    return log
