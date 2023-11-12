---
layout: page
title: common/chown (中文)
description: "修改用户和用户组对文件或目录的所有权。"
content_hash: cd53e55317763694f2eabc1c3ab9aa936960889f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chown.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chown.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chown.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chown.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chown.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/chown.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chown

修改用户和用户组对文件或目录的所有权。
更多信息：<https://www.gnu.org/software/coreutils/chown>.

- 修改文件或目录的所有者：

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 修改文件或目录的所有者及所属组：

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户组</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>

- 递归修改目录及其子目录和文件的所有者：

`chown -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 修改符号链接的所有者：

`chown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/符号链接</span>

- 修改文件或目录的所有者与参考文件相同：

`chown --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/参考文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录</span>
