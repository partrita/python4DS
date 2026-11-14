# Fix: Duplicate dependency `soupsieve`

## Problem
The build failed with:
```
error: Failed to parse `uv.lock`
  Caused by: For package `beautifulsoup4==4.15.0`, found duplicate dependency `soupsieve==4.0`
```

## Root Cause
`soupsieve>=2.8.4` was listed as a direct dependency in `pyproject.toml` (line 52), but `beautifulsoup4>=4.12.3` (also a direct dependency) already brings in `soupsieve` as a transitive dependency. This created a duplicate dependency conflict in `uv.lock`.

Additionally, three security alerts were detected for `soupsieve`:
- **#302**: Polynomial-time denial of service in the descendant combinator
- **#303**: Uncontrolled recursion in CSS parser lets nested pseudo-class selectors exhaust the Python call stack  
- **#304**: Exponential ReDoS in selector compilation via `\9-run` in CSS_ESCAPES/IDENTIFIER

## Fix
Removed `soupsieve>=2.8.4` from the direct dependencies in `pyproject.toml`. Since `beautifulsoup4` already depends on `soupsieve` (version `2.10` for Python < 3.11.5 or `4.1` for Python >= 3.11.5), listing it separately as a direct dependency is redundant and potentially conflicting.

## Verification
`uv sync` now completes successfully, resolving 239 packages.

## Security Note
The current `soupsieve` version in use is **4.1** (transitive dependency via `beautifulsoup4==4.15.0`, installed for Python >= 3.11.5). The three security alerts above relate to ReDoS and recursion vulnerabilities in soupsieve. Further investigation may be needed to determine if a newer soupsieve version is required to address these specific CVEs, as the fixes may be in a point release beyond 4.1.