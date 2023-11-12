---
layout: page
title: common/ar (中文)
description: "创建，修改，提取库文件（`.a`, `.so`, `.o`）。"
content_hash: 714508752bd098d607c060262c747d810721ba5f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

创建，修改，提取库文件（`.a`, `.so`, `.o`）。
更多信息：<https://manned.org/ar>.

- 从库文件中提取全部成员：

`ar -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a 文件</span>

- 列出库文件中的成员：

`ar -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a 文件</span>

- 替换或添加文件到库文件：

`ar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">要被添加内容的 a 文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 3</span>

- 插入对象文件索引（相当于使用`ranlib`）：

`ar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a 文件</span>

- 使用文件和附带的目标文件索引创建存档：

`ar -rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a 文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o 文件 3</span>
