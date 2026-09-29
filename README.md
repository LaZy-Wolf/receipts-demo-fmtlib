# receipts-demo-fmtlib

Tiny formatting helpers used by [receipts-demo-depbump](https://github.com/LaZy-Wolf/receipts-demo-depbump).

```python
from fmtlib import human_bytes, percent, ordinal, format_number

human_bytes(1536)        # '1.5 KB'
percent(0.125, digits=1) # '12.5%'
ordinal(23)              # '23rd'
format_number(1234567)   # '1,234,567'
```

Install a release straight from GitHub:

```bash
pip install "receipts-demo-fmtlib @ git+https://github.com/LaZy-Wolf/receipts-demo-fmtlib@v1.0.0"
```

See [CHANGELOG.md](CHANGELOG.md) for release notes.
