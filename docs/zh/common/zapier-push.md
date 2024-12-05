---
layout: page
title: common/zapier-push (中文)
description: "构建并上传一个 Zapier 集成。"
content_hash: 4e9e1e44dd6ac8a1492d84b00b86bb7b82a7bf2a
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zapier-push.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zapier-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zapier push

构建并上传一个 Zapier 集成。
更多信息：<https://platform.zapier.com/reference/cli#push>.

- 向 Zapier 推送一个集成：

`zapier push`

- 禁用智能文件包含（将只包含 `index.js` 所需的文件）：

`zapier push --disable-dependency-detection`

- 显示额外的调试输出：

`zapier push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
