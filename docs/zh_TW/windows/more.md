---
layout: page
title: windows/more (中文 (繁體, 台灣))
description: "分頁顯示標準輸入或文件的輸出。"
content_hash: bdc47faa0c972c017c1749ce26e42707dd40d804
related_topics:
  - title: English version
    url: /en/windows/more.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># more

分頁顯示標準輸入或文件的輸出。
更多資訊：<https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- 分頁顯示標準輸入的輸出：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- 分頁顯示一個或多個文件的內容：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 將製表符（tab）轉換為指定的空格數（space）：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">空格數</span>

- 顯示內容前先清除輸出：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>` /c`

- 從第 5 行開始顯示輸出：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 啟用擴展交互模式（請參閱使用幫助）：

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>` /e`

- 顯示全部幫助資訊：

`more /?`
