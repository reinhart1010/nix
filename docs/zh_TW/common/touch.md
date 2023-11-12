---
layout: page
title: common/touch (中文 (繁體, 台灣))
description: "改變檔案的存取與修改時間。"
content_hash: 0cbc074ece9622abbfc29b55be33f64222018eac
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># touch

改變檔案的存取與修改時間。
更多資訊：<https://manned.org/man/freebsd-13.1/touch>.

- 建立新檔案，或更新現存檔案的存取與修改時間：

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案名稱</span>

- 將存取與修改時間設定為指定時刻：

`touch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">西元年份月份日期小時分鐘.秒鐘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案名稱</span>

- 以其中一個檔案的存取與修改時間為基準，設定另一個檔案的存取與修改時間：

`touch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">來源檔案名稱</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目標檔案名稱</span>
