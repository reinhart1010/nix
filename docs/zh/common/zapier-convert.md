---
layout: page
title: common/zapier-convert (中文)
description: "将一个可视化构建器集成转换为 CLI 集成。"
content_hash: baf6b14a6ea7acbefb54cc64fc983d05e8b44d5f
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zapier-convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zapier-convert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-convert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier convert

将一个可视化构建器集成转换为 CLI 集成。
更多信息：<https://platform.zapier.com/reference/cli#convert>.

- 转换一个可视化构建器集成：

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">集成_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 使用特定版本转换一个可视化构建器集成：

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">集成_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 显示额外的调试输出：

`zapier convert --debug`
