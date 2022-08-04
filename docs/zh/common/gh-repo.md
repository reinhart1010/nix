---
layout: page
title: common/gh-repo (中文)
description: "在命令行上操作 GitHub 仓库。"
content_hash: 697e5e859e71007a40c94fef375e98504731f451
related_topics:
  - title: English version
    url: /en/common/gh-repo.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-repo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh repo

在命令行上操作 GitHub 仓库。
更多信息：<https://cli.github.com/manual/gh_repo>.

- 创建一个新的仓库（如果没有设置仓库名称，默认将为当前目录的名称）：

`gh repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 克隆一个仓库：

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>

- 复刻并克隆一个仓库：

`gh repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>` --clone`

- 在网络浏览器中查看仓库：

`gh repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>` --web`
