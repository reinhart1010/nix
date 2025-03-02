---
layout: page
title: common/du (中文)
description: "磁盘使用率：估计和汇总文件和目录空间使用率。"
content_hash: 62e680cea026dc7c053cb2daa01c0b4a951f4cfe
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

磁盘使用率：估计和汇总文件和目录空间使用率。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- 以给定单位（B/KiB/MiB）列出目录和所有子目录的大小：

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 以可读形式列出目录和任何子目录的大小（即自动转换为的合适的单位）：

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 以可读单位显示目录大小：

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 列出目录以及其中所有文件和目录的可读大小：

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 列出目录和任何子目录的可读大小，最多可达 N 级：

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 列出当前目录中所有 `.jpg` 文件的可读大小，并在最后显示累计总数：

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./*.jpg</span>

- 列出超过特定大小的所有文件和目录（包括隐藏的文件和目录）（对于查询实际占用空间很有用）：

`du --all --human-readable --threshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G|1024M|1048576K</span>` .[^.]* *`
