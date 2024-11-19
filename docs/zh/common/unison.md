---
layout: page
title: common/unison (中文)
description: "双向文件同步工具。"
content_hash: 1e1cfacafdb9cdf916cffe39d4632023ce323ca1
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/unison.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unison.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unison.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unison

双向文件同步工具。
更多信息：<https://github.com/bcpierce00/unison>.

- 同步两个目录（第一次同步这两个目录时会创建日志）：

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录2</span>

- 自动接受（无冲突的）默认值：

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录2</span>` -auto`

- 使用模式忽略某些文件：

`unison `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录2</span>` -ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模式</span>

- 查看文档：

`unison -doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主题</span>
