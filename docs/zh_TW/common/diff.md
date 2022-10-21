---
layout: page
title: common/diff (中文 (繁體, 台灣))
description: "比較兩個檔案或目錄間的差異。"
content_hash: 7759329be39841d3268f8809c1cb02e074ce768d
related_topics:
  - title: Deutsch version
    url: /de/common/diff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/diff.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diff.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/diff.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diff

比較兩個檔案或目錄間的差異。
更多資訊：<https://man7.org/linux/man-pages/man1/diff.1.html>.

- 比較兩檔案，列出 `舊檔案` 相異於 `新檔案` 而需更改之處，以讓兩者相同：

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊檔案</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新檔案</span>

- 忽略空格下，比較兩檔案：

`diff --ignore-all-space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊檔案</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新檔案</span>

- 比較兩檔案，並排顯示差異：

`diff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊檔案</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新檔案</span>

- 比較兩檔案，並以統一格式 (unified format) 顯示差異（為 `git diff` 預設格式）：

`diff --unified `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊檔案</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新檔案</span>

- 遞迴比較兩目錄，顯示相異的檔名或目錄名，與檔案內更動：

`diff --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊目錄</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新目錄</span>

- 比較兩目錄，只顯示相異檔案的檔名：

`diff --recursive --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊目錄</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新目錄</span>

- 由兩個文字檔之間差異建立一個補丁 (patch) 檔給 Git，不存在的檔案視為空白文件：

`diff --text --unified --new-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">舊檔案</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新檔案</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.patch</span>
