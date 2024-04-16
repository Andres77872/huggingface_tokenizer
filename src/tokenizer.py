import os

from transformers import AutoTokenizer


async def tokenize(
        model: str,
        input_text: str,
        add_special_tokens: bool = False,
) -> tuple[list[int], list[str]]:
    tokenizer = AutoTokenizer.from_pretrained(model,
                                              token=os.environ['HF_TOKEN'])
    token_ids = tokenizer.encode(input_text,
                                 add_special_tokens=add_special_tokens)
    token_strings = tokenizer.convert_ids_to_tokens(token_ids)
    return token_ids, token_strings
