from pypinyin import pinyin, Style


def rhyme_convert(yunmu):
    RHYME = {  # 十三辙 / 编号按中华新韵十四韵
        # 发花
        'a': '1', 'ia': '1', 'ua': '1',
        # 梭波
        'o': '2', 'e': '2', 'uo': '2',
        # 乜斜
        'ie': '3', 've': '3', 'ue': '3',
        # 怀来
        'ai': '4', 'uai': '4',
        # 灰堆
        'ei': '5', 'ui': '5',
        # 摇条
        'ao': '6', 'iao': '6',
        # 由求
        'ou': '7', 'iu': '7',
        # 言前
        'an': '8', 'ian': '8', 'uan': '8', 'van': '8',
        # 人辰
        'en': '9', 'in': '9', 'un': '9', 'vn': '9',
        # 江阳
        'ang': 'a', 'iang': 'a', 'uang': 'a',
        # 中东
        'eng': 'b', 'ing': 'b', 'ong': 'b', 'iong': 'b',
        # 衣七
        'i': 'c', 'v': 'c', 'er': 'c',
        # 姑苏
        'u': 'd',
    }
    return RHYME[yunmu]


def char_to_yunmu(s):
    raw_yunmus = pinyin(s, style=Style.FINALS_TONE3, strict=False, errors='ignore')
    yunmus_without_tone = list(filter(lambda x: x != '', [x[0][:-1] for x in raw_yunmus]))
    return yunmus_without_tone


def yunmu_to_rhyme(yunmus):
    return [rhyme_convert(x) for x in yunmus]


def char_to_rhyme(s):
    return ''.join(yunmu_to_rhyme(char_to_yunmu(s)))


def lrs(x):
    n = len(x)
    lcs_re = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    res = ""  # To store result
    res_length = 0  # To store length of result

    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if x[i - 1] == x[j - 1] and lcs_re[i - 1][j - 1] < (j - i):
                lcs_re[i][j] = lcs_re[i - 1][j - 1] + 1

                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if lcs_re[i][j] > res_length:
                    res_length = lcs_re[i][j]
                    index = max(i, index)

            else:
                lcs_re[i][j] = 0

    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if res_length > 0:
        for i in range(index - res_length + 1,
                       index + 1):
            res = res + x[i - 1]

    return res


def lcs(x, y):
    matrix = [''] * (len(x) + 1)
    for index_x in range(len(matrix)):
        matrix[index_x] = [''] * (len(y) + 1)

    for index_x in range(1, len(x) + 1):
        for index_y in range(1, len(y) + 1):
            if x[index_x - 1] == y[index_y - 1]:
                matrix[index_x][index_y] = matrix[index_x - 1][index_y - 1] + x[index_x - 1]
            elif len(matrix[index_x][index_y - 1]) > len(matrix[index_x - 1][index_y]):
                matrix[index_x][index_y] = matrix[index_x][index_y - 1]
            else:
                matrix[index_x][index_y] = matrix[index_x - 1][index_y]

    return matrix[len(x)][len(y)]


def del_redundant_char(x):
    char_set = set()
    res = ''
    for c in x:
        if c not in char_set:
            res += c
            char_set.add(c)
    return res


def del_a_char_from_b(a, b):
    char_set = set(list(a))
    res = ''
    for c in b:
        if c not in char_set:
            res += c
    return res
