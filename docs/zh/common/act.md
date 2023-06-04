---
layout: page
title: common/act (中文)
description: "使用 Docker 本地运行 GitHub Actions."
content_hash: 1d24654e1bc25f20ae9479bc2b5c9b35bbd4c327
last_modified_at: 2023-06-04
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/act.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># act

使用 Docker 本地运行 GitHub Actions.
更多信息：<https://github.com/nektos/act>.

- 列出可用的 actions 清单：

`act -l`

- 运行默认 event：

`act`

- 运行指定 event：

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- 运行指定 action：

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- 非实际运行 actions（也就是 dry-run 模式）：

`act -n`

- 展示详细记录：

`act -v`

- 运行指定 workflow：

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workflow 的路径</span>
