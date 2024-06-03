---
layout: page
title: common/rsync (中文)
description: "一种快速，通用，远程（和本地）文件复制工具，默认使用 SSH。"
content_hash: c44e3a5ac01a3455da2612fb5c24954461b40c61
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/rsync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/rsync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rsync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rsync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rsync.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rsync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsync

一种快速，通用，远程（和本地）文件复制工具，默认使用 SSH。
如果要指定远程路径，请使用 `user@host:path/to/file_or_directory`.
更多信息：<https://download.samba.org/pub/rsync/rsync.1>.

- 复制文件：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 使用归档模式递归拷贝文件，并保留所有属性，不解析软链接：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 将文件以归档模式并保留几乎所有属性进行传输，并以人类可读方式输出详细信息和进度条，中断时保留部分信息：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-zvhP|--compress --verbose --human-readable --partial --progress</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 以递归模式传输文件：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 将目录下的所有内容（不包含该目录），以递归方式传输：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>`/ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 归档方式传输目录，保留几乎所有属性，解析软连接，并忽略已传输的文件：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-auL|--archive --update --copy-links</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 传输目录到运行 `rsyncd` 的远端，并删除目标目录中源目录中不存在的文件：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>` --delete rsync://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>

- 指定本地和远程之间通信方式，使用指定端口，并显示进度条：

`rsync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--rsh</span>` 'ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>`' --info=progress2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/来源</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标</span>
