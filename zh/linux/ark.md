---
layout: page
title: linux/ark (中文)
description: "KDE 归档工具。"
content_hash: 32370960777b66efd077eba94b6bd6cf412f895b
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
---
# ark

KDE 归档工具。
更多信息：<https://docs.kde.org/stable5/en/ark/ark/>.

- 将存档解压缩到当前目录：

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存档名</span>

- 改变解压缩目录：

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">解压缩目录路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存档名</span>

- 创建一个原本不存在的存档并向它添加文件：

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">存档名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件2</span>
