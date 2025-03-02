---
layout: page
title: common/jello (中文)
description: "一个使用 Python 语法的命令行 JSON 处理器。"
content_hash: ae453fe0ea88a2daa3eb4bd068ed54a2b6cad223
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jello.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jello.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jello

一个使用 Python 语法的命令行 JSON 处理器。
更多信息：<https://github.com/kellyjonbrazil/jello>.

- 将 `stdin` 中的 JSON 或 JSON-Lines 数据进行美化打印到 `stdout`：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello`

- 输出 `stdin` 中的 JSON 或 JSON Lines 数据的模式到 `stdout`（对 grep 有用）：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello -s`

- 输出 `stdin` 中数组的所有元素（或对象的所有值）为 JSON 或 JSON-Lines 数据到 `stdout`：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello -l`

- 输出 `stdin` 中的 JSON 或 JSON-Lines 数据的第一个元素到 `stdout`：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello _[0]`

- 输出 `stdin` 中 JSON 或 JSON-Lines 数据中每个元素的给定键的值到 `stdout`：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello '[i.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` for i in _]'`

- 输出多个键的值作为新的 JSON 对象（假设输入 JSON 拥有键 `key_name1` 和 `key_name2`）：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello '{"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键1</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名1</span>`, "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>`": _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名2}</span>`'`

- 输出给定键的值为字符串（并禁用 JSON 输出）：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jello -r '"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">一些文本</span>`: " + _.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>`'`
