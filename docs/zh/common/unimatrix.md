---
layout: page
title: common/unimatrix (中文)
description: "使用 Unicode 字符模拟《黑客帝国》的视觉效果。"
content_hash: 75dd57bde3eea1e9c86ab43e7ad8a8cb9dfba2b5
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/unimatrix.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unimatrix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unimatrix

使用 Unicode 字符模拟《黑客帝国》的视觉效果。
请参阅：`cmatrix`。
更多信息：<https://github.com/will8211/unimatrix>.

- 模仿 `cmatrix` 的默认输出（无 Unicode，适用于 TTY）：

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">96</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>

- 无粗体字符，缓慢地显示，使用表情符号、数字和少量符号：

`unimatrix --no-bold --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens</span>

- 更改字符的颜色：

`unimatrix --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red|green|blue|white|...</span>

- 使用字母代码选择字符集（可用字符集请参阅 `unimatrix --help`）：

`unimatrix --character-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">character_sets</span>

- 更改滚动速度：

`unimatrix --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>
