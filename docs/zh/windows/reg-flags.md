---
layout: page
title: windows/reg-flags (中文)
description: "显示或设置注册表键的标志。"
content_hash: 25626478f85368faab4809dfe8dd18bfbbb92afa
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/reg-flags.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg flags

显示或设置注册表键的标志。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- 显示当前指定键的标志：

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` query`

- 显示帮助和可用的标志类型：

`reg flags /?`

- 为特定键设置指定以空格分隔的标志，并取消设置未提及的标志：

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标志 1 标志 2 ..</span>

- 为指定的键和其子键设置标志：

`reg flags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标志</span>` /s`
