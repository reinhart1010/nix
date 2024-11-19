---
layout: page
title: common/qtcreator (中文)
description: "跨平台的 Qt 应用程序集成开发环境。"
content_hash: 02c766c6e49976a9abf8a55321e0c2ba50a48c4d
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qtcreator.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qtcreator.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qtcreator.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qtcreator

跨平台的 Qt 应用程序集成开发环境。
更多信息：<https://doc.qt.io/qtcreator/creator-cli.html>.

- 启动 Qt Creator：

`qtcreator`

- 启动 Qt Creator 并恢复上次会话：

`qtcreator -lastsession`

- 启动 Qt Creator 并且不加载指定的插件：

`qtcreator -noload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定插件</span>

- 启动 Qt Creator 并且不加载任何插件：

`qtcreator -noload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>

- 在演示模式下启动 Qt Creator，并显示键盘快捷键的弹出提示：

`qtcreator -presentationMode`

- 启动 Qt Creator 并显示来自特定提交的差异：

`qtcreator -git-show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">提交</span>
