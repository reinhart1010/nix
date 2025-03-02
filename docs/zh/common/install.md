---
layout: page
title: common/install (中文)
description: "复制文件并设置属性。"
content_hash: f66fdf51dc5aa05be056a26c1d2b602a27cac374
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# install

复制文件并设置属性。
将文件（通常是可执行文件）复制到系统位置，如 `/usr/local/bin`，并赋予它们适当的权限或所有权。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- 复制文件到目标目录：

`install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 复制文件到目标目录，并设置其所有权：

`install --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 复制文件到目标目录，并设置其所属组：

`install --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户组</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 复制文件到目标目录，并设置其权限：

`install --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 复制文件到目标目录，保留访问时间和修改时间：

`install --preserve-timestamps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 创建目标目录及其父目录，然后复制文件到目标目录：

`install -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件1 路径/到/源文件2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>
