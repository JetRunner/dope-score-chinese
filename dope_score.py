from utils import *
from sys import argv


def dope_score(lyrics: str):
    lines = lyrics.splitlines()

    inline_counter = 0
    interline_1_counter = 0
    interline_2_counter = 0
    inline_char_counter = 0
    interline_1_char_counter = 0
    interline_2_char_counter = 0

    line_minus_1 = None
    line_minus_2 = None
    len_interline_1 = 0
    len_interline_2 = 0
    for ix, line in enumerate(lines):
        rhymes = char_to_rhyme(line)
        len_rhymes = len(rhymes)
        if len_rhymes == 0:
            continue

        # 句内押韵计算
        processed_rhymes = char_to_rhyme(del_redundant_char(line))
        inline_char_counter += len(processed_rhymes)
        len_inline = len(lrs(processed_rhymes))

        # 句间押韵计算 - 1
        if line_minus_1 is not None:
            rhymes_minus_1 = char_to_rhyme(line_minus_1)
            processed_line_1 = del_a_char_from_b(line_minus_1, line)
            rhymes_processed_1 = char_to_rhyme(processed_line_1)
            interline_1_char_counter += len(rhymes_processed_1)
            len_interline_1 = len(lcs(rhymes_minus_1, rhymes_processed_1))

        # 句间押韵计算 - 2
        if line_minus_2 is not None:
            rhymes_minus_2 = char_to_rhyme(line_minus_2)
            processed_line_2 = del_a_char_from_b(line_minus_2, line)
            rhymes_processed_2 = char_to_rhyme(processed_line_2)
            interline_2_char_counter += len(rhymes_processed_2)
            len_interline_2 = len(lcs(rhymes_minus_2, rhymes_processed_2))

        line_minus_2 = line_minus_1
        line_minus_1 = line

        inline_counter += len_inline
        interline_1_counter += len_interline_1
        interline_2_counter += len_interline_2

    # (DopeScore, 句内押韵, 句间押韵, 跳押)
    subscore_0 = inline_counter / inline_char_counter if inline_char_counter else 0
    subscore_1 = interline_1_counter / interline_1_char_counter if interline_1_char_counter else 0
    subscore_2 = interline_2_counter / interline_2_char_counter if interline_2_char_counter else 0
    return subscore_0 + subscore_1 + subscore_2, subscore_0, subscore_1, subscore_2


if __name__ == '__main__':
    with open(argv[1], 'r') as content_file:
        content = content_file.read()
    res = dope_score(content)
    print(f'总分: {res[0] * 100:.2f}, 句内押韵: {res[1] * 100:.2f}, 句间押韵: {res[2] * 100:.2f}, 句间跳押: {res[3] * 100:.2f}')
