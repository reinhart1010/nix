---
layout: page
title: common/yq (中文)
description: "一个轻量级且可移植的命令行 YAML 处理器。"
content_hash: 3c2a2c49f130f14936ed1ae01279b8d4db419ee1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yq

一个轻量级且可移植的命令行 YAML 处理器。
更多信息：<https://mikefarah.gitbook.io/yq/>.

- 以漂亮打印格式输出 YAML 文件（v4+）：

`yq eval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>

- 以漂亮打印格式输出 YAML 文件（v3）：

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>` --colors`

- 输出仅包含数组的 YAML 文件中的第一个元素（v4+）：

`yq eval '.[0]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>

- 输出仅包含数组的 YAML 文件中的第一个元素（v3）：

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>` '[0]'`

- 在文件中设置（或覆盖）键的值（v4+）：

`yq eval '.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>`"' --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>

- 在文件中设置（或覆盖）键的值（v3）：

`yq write --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file.yaml</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>`'`

- 合并两个文件并打印到 `stdout`（v4+）：

`yq eval-all 'select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file1.yaml</span>`") * select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file2.yaml</span>`")' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file2.yaml</span>

- 合并两个文件并打印到 `stdout`（v3）：

`yq merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file2.yaml</span>` --colors`
