---
layout: page
title: common/zapier-build (中文)
description: "构建一个可推送的 Zapier 集成 `zip` 文件。"
content_hash: 861d7ea6c650b44df03d3bede3ef3ba6d0e1fb59
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zapier-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zapier-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zapier build

构建一个可推送的 Zapier 集成 `zip` 文件。
更多信息：<https://platform.zapier.com/reference/cli#build>.

- 创建一个构建：

`zapier build`

- 禁用智能文件包含（只会包含 `index.js` 所需的文件）：

`zapier build --disable-dependency-detection`

- 显示额外的调试输出：

`zapier build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
