---
layout: page
title: linux/ark (中文)
description: "KDE 归档工具。"
content_hash: 0ee66dd03715c8de362d0d10b72cc52faf6067e5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ark

KDE 归档工具。
更多信息：<https://docs.kde.org/stable5/en/ark/ark/>.

- 将存档解压缩到当前目录：

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/存档名</span>

- 改变解压缩目录：

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/存档名</span>

- 创建一个原本不存在的存档并向它添加文件：

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/存档名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>
