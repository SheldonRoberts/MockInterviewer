"""
Like this:

annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)

But instead of "verb" or "abj" we track filler words from a filler list

"""
import re

filler_words = ["actually", "basically", "literally", "supposedly", "totally"]


def annotate_raw_text(raw_text: str) -> (str, int):
    """Annotate text with filler words"""
    # split on spaces, but don't remove them
    words = re.findall(r"(\S+ )", raw_text)
    annotated_text = []
    num_fillers = 0
    for word in words:
        if word.strip() in filler_words:
            annotated_text.append((word, "filler", "#faa"))
            num_fillers += 1
        else:
            annotated_text.append(word)
    return annotated_text, num_fillers
