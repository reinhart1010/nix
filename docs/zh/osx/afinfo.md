---
layout: page
title: osx/afinfo (中文)
description: "显示音频文件元数据（Metadata）详细信息（OS X）。"
content_hash: 1452e60fd9be7b95b00062013315d663b5741d80
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/afinfo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afinfo

显示音频文件元数据（Metadata）详细信息（OS X）。
OS X 自带命令。
更多信息：<https://keith.github.io/xcode-man-pages/afinfo.1.html>.

- 显示给定音频文件的详细信息：

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示简化的音频文件信息（单行）：

`afinfo --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示音频文件的元数据信息以及其 InfoDictionary 词典：

`afinfo --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 以 xml 格式显示音频文件信息：

`afinfo --xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示警告信息（如存在）：

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示完整用法帮助：

`afinfo --help`
