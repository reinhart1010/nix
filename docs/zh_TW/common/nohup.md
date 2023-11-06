---
layout: page
title: common/nohup (中文 (繁體, 台灣))
description: "當終端被關閉時允許程序繼續存在運作。"
content_hash: ce371337b1992d81f22f494e6b4a144eb495ccde
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
---
# nohup

當終端被關閉時允許程序繼續存在運作。
更多資訊：<https://www.gnu.org/software/coreutils/nohup>.

- 執行一個可以在終端機之外繼續執行的程序：

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序指令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">參數1 參數2 ...</span>

- 在背景啟動 `nohup`：

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序指令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">參數1 參數2 ...</span>` &`

- 執行可以在終端機之外繼續執行的的 `.sh` 檔：

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh檔案</span>` &`

- 執行一個程序並將其輸出寫入特定文件：

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">程序指令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">參數1 參數2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路徑</span>` &`
