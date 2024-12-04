---
layout: page
title: common/zoxide (中文)
description: "记录最常使用的目录。"
content_hash: 8ce9cf62616ba0cd09dbd2af5c2f729207983cb2
last_modified_at: 2024-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/zoxide.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zoxide.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zoxide.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zoxide.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zoxide.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zoxide

记录最常使用的目录。
使用一个排序算法来导航到最佳匹配。
更多信息：<https://github.com/ajeetdsouza/zoxide>.

- 转到名称中包含 "foo" 的排名最高的目录：

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 转到名称中依次包含 "foo" 和 "bar" 的排名最高的目录：

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- 启动一个交互式目录搜索（需要 `fzf`）：

`zoxide query --interactive`

- 添加一个目录或提升其排名：

`zoxide add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 从 `zoxide` 的数据库中交互式地移除一个目录：

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` --interactive`

- 为命令别名生成 shell 配置（`z`, `za`, `zi`, `zq`, `zr`）：

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
