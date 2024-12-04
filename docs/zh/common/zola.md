---
layout: page
title: common/zola (中文)
description: "一个静态站点生成器，一个二进制文件内包含所有功能。"
content_hash: 3bdab68b1582031c59522af7eef64a55f19e733f
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zola.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zola.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zola.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zola.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zola

一个静态站点生成器，一个二进制文件内包含所有功能。
更多信息：<https://www.getzola.org/documentation/getting-started/cli-usage/>.

- 在指定目录下创建 Zola 使用的目录结构：

`zola init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">我的站点</span>

- 在删除 `public` 目录后构建整个站点：

`zola build`

- 将整个站点构建到另一个目录中：

`zola build --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出_目录/</span>

- 使用本地服务器构建并服务站点（默认是 `127.0.0.1:1111`）：

`zola serve`

- 构建所有页面，就像构建命令一样，但不将结果写入磁盘：

`zola check`
