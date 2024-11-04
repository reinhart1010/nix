---
layout: page
title: common/atuin (中文)
description: "存储您的 shell 历史记录到可搜索的数据库。"
content_hash: 92e3623941e2afd4d6dac01e512e2588cf777b43
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/atuin.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/atuin.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atuin.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atuin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atuin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atuin

存储您的 shell 历史记录到可搜索的数据库。
可选择在机器之间同步加密历史记录。
更多信息：<https://atuin.sh/docs/commands>.

- 安装 atuin 到您的 shell:

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- 从 shell 默认历史记录文件导入：

`atuin import auto`

- 搜索 shell 历史记录中指定的命令：

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 使用指定的用户名，邮箱和密码在默认同步服务器注册账号：

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">邮箱</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 登录默认同步服务器：

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 与同步服务器同步历史记录：

`atuin sync`
