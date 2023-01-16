import random

from anki import hooks
from anki.template import TemplateRenderContext
import re


def randalg(
    field_text: str,
    field_name: str,
    filter_name: str,
    context: TemplateRenderContext,
) -> str:
    separators = "|"  # Characters to split on, if you wanted to include ! and ? as well, set it to "|!?".
    if filter_name == "rand-alg":
        return random.choice(
            [
                strip_anki_string(x)
                for x in re.split(rf"[{separators}]", field_text)
                if strip_anki_string(x)
            ]
        )
    else:
        return field_text


def strip_anki_string(string: str) -> str:
    return string.replace("&nbsp;", "").strip()


hooks.field_filter.append(randalg)
