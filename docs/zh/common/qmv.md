---
layout: page
title: common/qmv (中文)
description: "使用默认文本编辑器定义文件名来移动文件和目录。"
content_hash: fe84c34ec08d22980d8c527dafb96c3b29dbc391
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qmv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qmv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qmv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qmv

使用默认文本编辑器定义文件名来移动文件和目录。
更多信息：<https://www.nongnu.org/renameutils/>.

- 移动单个文件（在编辑器中打开左侧为源文件名，右侧为目标文件名）：

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件</span>

- 移动多个 JPEG 文件：

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 移动多个目录：

`qmv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录3</span>

- 移动目录中的所有文件和目录：

`qmv --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 移动文件，但在编辑器中交换源文件名和目标文件名的位置：

`qmv --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- 重命名当前目录中的所有文件和文件夹，但在编辑器中仅显示目标文件名（可以将其视为一种简单模式）：

`qmv --format=do .`
