---
layout: page
title: common/unrar (中文)
description: "提取 RAR 压缩档案。"
content_hash: c9009a3bd599d30f5fd2b7f3c895e654cb82a49e
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/unrar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/unrar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unrar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unrar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unrar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unrar

提取 RAR 压缩档案。
更多信息：<https://manned.org/unrar>.

- 提取文件并保留原始目录结构：

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.rar</span>

- 将文件提取到指定路径，并保留原始目录结构：

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/解压目录</span>

- 提取文件到当前目录，但不保留档案中的目录结构：

`unrar e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.rar</span>

- 测试档案内每个文件的完整性：

`unrar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.rar</span>

- 列出档案内的文件并不解压：

`unrar l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩包.rar</span>
