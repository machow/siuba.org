from siuba.dply.verbs import DPLY_FUNCTIONS
from siuba.siu import _, call
from pathlib import Path


def row(header, fname, mod):
    return f"{header} {fname}\n\n::: {mod}.{fname}"

def row2(header, fname, mod):
    return f"::: {mod}.{fname}"

#res = list(map(lambda s: row("##", s, "siuba"), sorted(DPLY_FUNCTIONS)))
#
#print("\n\n".join(res))

IGNORE = ("left_join", "inner_join", "right_join", "full_join", "if_else", "case_when", "group_by", "ungroup")

for func_name in DPLY_FUNCTIONS:
    if func_name not in IGNORE:
        Path(f"verb-{func_name}.md").write_text(f"::: siuba.{func_name}")
