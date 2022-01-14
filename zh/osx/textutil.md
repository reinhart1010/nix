---
layout: page
title: osx/textutil (中文)
description: "用于操作各种格式的文本文件。"
content_hash: 69f6e820bddb00fd56e31aa4588e3cadba45fa05
related_topics:
  - title: English version
    url: /en/osx/textutil.html
    icon: bi bi-globe
---
# textutil

用于操作各种格式的文本文件。
更多信息：<https://ss64.com/osx/textutil.html>.

- 显示有关 `foo.rtf` 的信息：

`textutil -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>

- 将 `foo.rtf` 转换为 `foo.html`:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>

- 将带格式的 rtf 文本转换为普通 txt 文本：

`textutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.rtf</span>` -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- 将 `foo.txt` 转换为 `foo.rtf`, 字体使用 Times 字号 10:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtf</span>` -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.txt</span>

- 加载当前目录中的所有 RTF 文件，连接其内容，并将结果作为 `index.html` 写入，HTML 标题设置为"多个文件":

`textutil -cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` -title "多个文件" -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` *.rtf`
