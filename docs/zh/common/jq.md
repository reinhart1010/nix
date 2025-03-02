---
layout: page
title: common/jq (中文)
description: "一个使用特定领域语言（DSL）的 JSON 处理器。"
content_hash: 72e6d40e7019d237eab66a4ece32c2487cda30ad
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/jq.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jq.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/jq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jq

一个使用特定领域语言（DSL）的 JSON 处理器。
更多信息：<https://jqlang.github.io/jq/manual/>.

- 使用 `jq` 二进制执行特定的表达式（打印出彩色和格式化的 JSON 输出）：

`jq '.' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.json</span>

- 执行特定的脚本：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq --from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.jq</span>

- 传递特定的参数：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--arg "name1" "value1" --arg "name2" "value2" ...</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">. + $ARGS.named</span>`'`

- 通过来自多个文件的旧 JSON 对象创建新的 JSON 对象：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/多个_json_文件_*.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{newKey1: .key1, newKey2: .key2.nestedKey, ...}</span>`'`

- 打印特定的数组项：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[索引1], .[索引2], ...</span>`'`

- 打印所有数组/对象中的值：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq '.[]'`

- 打印具有双条件过滤的数组对象：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq '.[] | select((.key1=="value1") and .key2=="value2")'`

- 添加/移除特定的键：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 路径/到/文件.json</span>` | jq '. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"key1": "value1", "key2": "value2", ...}</span>`'`
