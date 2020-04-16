# dope-score-chinese
Automatic metric for evaluating rap lyrics in Chinese (Mandarin).

## Declaration
This tool is only used for evaluating the quality of machine generated rap lyrics and only considers the rhymes in a rap song. **It does not in any way indicate the quality of a human-composed rap song.** This metric does not work on English nor Chinese dialects.

## How it works?
This tool automatically measures the non-repeating "density" of rhymes in a line, between the line and its two previous lines. After calculating these subscores, we sum up them to be the total score. We'll add more details later.

## Examples

| 歌名(Title)                | 歌手(Artist)           | 句内(Inner)     | 句间(Inter-1)     | 跳押(Inter-2)     | 总分(Total)      |
|-------------------|--------------|--------|--------|--------|---------|
| 英雄归来              | PG One       | 14\.26 | 45\.01 | 44\.80 | 104\.07 |
| 差不多先生             | MC Hotdog    | 13\.18 | 42\.68 | 41\.76 | 97\.63  |
| 带我回家              | C\-BLOCK     | 11\.88 | 39\.34 | 37\.16 | 88\.39  |
| 虎山行               | GAI/艾福杰尼/功夫胖 | 11\.86 | 38\.91 | 37\.04 | 87\.81  |
| 孤独症               | C\-BLOCK     | 12\.06 | 39\.67 | 35\.80 | 87\.53  |
| 天生爱你              | 幼稚园杀手        | 9\.82  | 40\.25 | 37\.21 | 87\.28  |
| 江湖流               | C\-BLOCK     | 13\.36 | 36\.84 | 33\.96 | 84\.16  |
| 野狼Disco           | 宝石Gem        | 12\.03 | 36\.38 | 34\.23 | 82\.64  |
| 阿司匹林              | 王以太          | 11\.84 | 36\.89 | 32\.92 | 81\.65  |
| 套路                | Jony J       | 11\.59 | 34\.14 | 34\.82 | 80\.55  |
| 我想part2           | MC法老         | 10\.56 | 34\.27 | 34\.33 | 79\.17  |
| 庆功酒               | 福克斯Fox       | 11\.73 | 34\.38 | 32\.52 | 78\.63  |
| 上学威龙              | MC法老         | 9\.91  | 33\.87 | 33\.16 | 76\.94  |
| 天地                | 吴亦凡          | 12\.85 | 27\.70 | 31\.12 | 71\.66  |
| 大碗宽面              | 吴亦凡          | 13\.65 | 28\.20 | 28\.61 | 70\.45  |

PLEASE NOTICE: THIS TABLE IS CALCULATED BY A PROGRAM. IT DOES NOT INDICATE THE AUTHOR OF THIS REPO AGREES WITH THESE RESULTS!!

请注意：本表是由程序计算得出，不代表程序作者同意此表中的结果！

## Usage
```bash
python dope_score.py /path/to/the/lyrics.txt
```

or

```bash
bash ./dope_score_dir.sh ./example_lyrics/
```
