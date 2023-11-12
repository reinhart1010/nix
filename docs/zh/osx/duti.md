---
layout: page
title: osx/duti (中文)
description: "在 macOS 上为文档类型和网页设置默认打开的应用程序。"
content_hash: 588f220e36180dd45343c6954b0e1612c4975522
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/duti.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/duti.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duti

在 macOS 上为文档类型和网页设置默认打开的应用程序。
更多信息：<https://github.com/moretension/duti>.

- 将 Safari 设置为 HTML 文档的默认打开程序：

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Safari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.html</span>` all`

- 将 vlc 设置为扩展名为.m4v 的文件的默认查看器：

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.videolan.vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m4v</span>` viewer`

- 将 Finder 设置为 ftp:// URL 访问的应用：

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Finder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp</span>

- 显示有关给定扩展名的默认应用程序的信息：

`duti -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext</span>

- 显示给定的 UTI 对应默认的处理程序：

`duti -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>

- 显示给定 UTI 对应所有的处理程序：

`duti -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>
