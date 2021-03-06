---
layout: page
title: windows/findstr (中文)
description: "在一个或多个文件中查找指定的文本。"
content_hash: 3c235e1d824cdc0f7fa9b59b1fc7ff341b08657a
related_topics:
  - title: English version
    url: /en/windows/findstr.html
    icon: bi bi-globe
---
# findstr

在一个或多个文件中查找指定的文本。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/findstr>.

- 在所有文件中查找以空格分隔的字符串：

`findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句 查询语句 ..</span>`" *`

- 以递归方式在所有文件中查找以空格分隔的字符串：

`findstr /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句 查询语句 ..</span>`" *`

- 查找时不区分大小写：

`findstr /i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`" *"`

- 使用正则表达式搜索：

`findstr /r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>`" *`

- 在所有文本文件中查找文字字符串（包含空格）：

`findstr /c:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`" *.txt`

- 只查找完全匹配的行：

`findstr /x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`" *`

- 显示匹配的行的行数：

`findstr /n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`" *`

- 只显示匹配的文件名：

`findstr /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`" *`
