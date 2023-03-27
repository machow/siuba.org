from __future__ import annotations

import re

from importlib.resources import files
from quartodoc import MdRenderer
from quartodoc.renderers.base import convert_rst_link_to_md, sanitize
from plum import dispatch
from typing import Union

from quartodoc import ast as qast
from griffe import dataclasses as dc
from griffe.docstrings import dataclasses as ds
from numpydoc.docscrape import NumpyDocString


class Renderer(MdRenderer):
    style = "siuba"

    @dispatch
    def render(self, el: dc.Union[dc.Object, dc.Alias]):
        # the See Also section may need to know the current object's module,
        # so we very roughly set it here.
        prev_obj = getattr(self, "crnt_obj", None)
        self.crnt_obj = el
        res = super().render(el)
        self.crnt_obj = prev_obj

        return res

    @dispatch
    def render(self, el: qast.DocstringSectionSeeAlso):
        lines = el.value.split("\n")

        # each entry in result has form: ([('func1', '<directive>), ...], <description>)
        parsed = NumpyDocString("")._parse_see_also(lines)

        result = []
        for funcs, description in parsed:
            links = [f"[{name}](`{self._name_to_target(name)}`)" for name, role in funcs]

            str_links = ", ".join(links)

            if description:
                str_description = "<br>".join(description)
                result.append(f"{str_links}: {str_description}")
            else:
                result.append(str_links)

        return "*\n".join(result)
                
    def _name_to_target(self, name: str):
        # hard-code siuba for now
        # I'm not sure what exactly the behavior of numpydoc is. For example,
        # it might also use the current object's module by default?
        crnt_path = getattr(self.crnt_obj, "path", None)
        parent = crnt_path.rsplit(".", 1)[0] + "."
        pkg = "siuba."

        if crnt_path and not (name.startswith(pkg) or name.startswith(parent)):
            return f"{parent}{name}"
        elif not name.startswith(pkg):
            return f"{pkg}{name}"
        
        return name


