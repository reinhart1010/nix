---
layout: page
title: common/gzip (中文)
description: "使用 `gzip` (LZ77) 压缩/解压文件。"
content_hash: 06d4c66f9bce67098a99a4a15bea7ad34ffffabb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gzip.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/gzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gzip

使用 `gzip` (LZ77) 压缩/解压文件。
更多信息：<https://www.gnu.org/software/gzip/manual/gzip.html>.

- 压缩文件，将其替换为 `gzip` 存档文件：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 解压缩文件，将其替换为原始未压缩版本：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.gz</span>

- 压缩文件，保留原始文件：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-k|--keep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 压缩文件，指定输出文件名：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件.gz</span>

- 解压缩 `gzip` 存档，指定输出文件名：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/解压缩的文件名</span>

- 指定压缩级别。 1 为最快（低压缩率），9 为最慢（高压缩率），默认值是 6：

`gzip -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--stdout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩文件.gz</span>

- 显示压缩或解压后的每个文件的名称和压缩百分比：

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decompress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.gz</span>
