# Changelog

## 1.1.0

### Changed

- **Breaking:** `percent()` now defaults to `digits=0` (was `digits=1`). `percent(0.125)` returns `'12%'` instead of `'12.5%'`. Pass `digits=1` to keep the old output.

## 1.0.1

Internal cleanup and docstring improvements.

## 1.0.0

Initial release: `human_bytes`, `percent`, `ordinal`, `format_number`.
