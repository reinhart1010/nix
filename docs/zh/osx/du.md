---
layout: page
title: osx/du (中文)
description: "磁盘使用率：估计和汇总文件和目录空间使用率。"
content_hash: 39ea27048e19e2ad4b4d0cda6d723ecad9baf4ea
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

磁盘使用率：估计和汇总文件和目录空间使用率。
更多信息：<https://keith.github.io/xcode-man-pages/du.1.html>.

- 以给定单位（KiB/MiB/GiB）列出目录和所有子目录的大小：

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>

- 以可读形式列出目录和任何子目录的大小（即自动为转换为选择的适当单位 kb|mb|gb）：

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>

- 以可读单位显示目录大小：

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>

- 列出目录以及其中所有文件和目录的可读大小：

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>

- 列出一个目录和任何子目录的可读大小，最深可达 n 级：

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件夹</span>

- 列出当前目录子目录中所有.jpg 文件的可读大小，并在末尾显示累计总数：

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
