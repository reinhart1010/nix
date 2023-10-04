---
layout: page
title: common/crontab (中文 (繁體, 台灣))
description: "排程作業按時間間隔執行。"
content_hash: a4b5f058428abac26ec02c58cec66e407ff22845
last_modified_at: 2023-10-04
related_topics:
  - title: English version
    url: /en/common/crontab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/crontab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crontab.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># crontab

排程作業按時間間隔執行。
更多資訊：<https://crontab.guru/>.

- 編輯目前使用者的排程文件：

`crontab -e`

- 編輯特定使用者的排程文件：

`sudo crontab -e -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">使用者名稱</span>

- 用給定檔案的內容取代目前的排程文件：

`crontab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 查看目前使用者的排程：

`crontab -l`

- 刪除目前使用者的所有排程：

`crontab -r`

- 範例排程：每天於 10：00 時執行， `*` 表示任意值：

`0 10 * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">執行命令</span>

- 範例排程：每 10 分鐘執行一次命令：

`*/10 * * * * `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">執行命令</span>

- 範例排程：每週五 02：30 執行sh檔：

`30 2 * * Fri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh檔路徑</span>
