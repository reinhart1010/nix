---
layout: page
title: common/json5 (中文)
description: "将 JSON5 文件转换为 JSON。"
content_hash: 3254f8fad7040c0d8e59f3f0ec930b45dca53f83
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/json5.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/json5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# json5

将 JSON5 文件转换为 JSON。
更多信息：<https://json5.org>.

- 将 JSON5 `标准输入` 转换为 JSON 并输出到 `标准输出`：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入</span>` | json5`

- 将 JSON5 文件转换为 JSON 并输出到 `标准输出`：

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.json5</span>

- 将 JSON5 文件转换为指定的 JSON 文件：

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.json5</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件.json</span>

- 验证一个 JSON5 文件：

`json5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件.json5</span>` --validate`

- 指定缩进的空格数（或使用 "t" 表示制表符）：

`json5 --space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">缩进量</span>

- 显示帮助：

`json5 --help`
