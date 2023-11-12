---
layout: page
title: common/go-doc (中文)
description: "显示包或符号的文档。"
content_hash: 943c0f9c919b306dfa961d0eea64bae2a86d90b9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-doc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go doc

显示包或符号的文档。
更多信息：<https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- 显示当前包的文档：

`go doc`

- 显示包文档及导出符号：

`go doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 同时显示符号的文档：

`go doc -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 同时显示源代码：

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- 显示指定的符号：

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json.Number</span>
