---
layout: page
title: linux/konsole (中文)
description: "Konsole: KDE 终端模拟器。"
content_hash: 9ba86394888d69b5f23a00e919735b2b84515320
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/linux/konsole.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/konsole.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># konsole

Konsole: KDE 终端模拟器。
更多信息：<https://docs.kde.org/trunk5/en/konsole/konsole/command-line-options.html>.

- 在特定目录中打开一个新的 Konsole：

`konsole --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 运行特定命令，退出窗口后不要关闭窗口：

`konsole --noclose -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 打开新标签页：

`konsole --new-tab`

- 在后台打开 Konsole 并在按下 Ctrl+Shift+F12（默认）时显示在最前面：

`konsole --background-mode`

- 使用紧急备冗配置文件打开 Konsole：

`konsole --fallback-profile`
