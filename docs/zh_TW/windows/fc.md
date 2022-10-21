---
layout: page
title: windows/fc (中文 (繁體, 台灣))
description: "比較兩個檔案或一組檔案間的差異。"
content_hash: bff14be77e00088541a4b4a9d0c90ecd1c647d79
related_topics:
  - title: English version
    url: /en/windows/fc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fc.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fc

比較兩個檔案或一組檔案間的差異。
以萬用字元 (*) 比較一組檔案。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- 比較兩個指定檔案：

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 比較檔案且忽略大小寫差異：

`fc /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 以 Unicode 文字檔方式比較檔案：

`fc /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 以 ASCII 文字形式比較檔案：

`fc /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 以二進位方式比較檔案：

`fc /b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 禁止將定位字元 (tab) 展開成空格：

`fc /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>

- 壓縮空白字元（定位字元與空格）後，再進行比較：

`fc /w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑2</span>
