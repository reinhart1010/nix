---
layout: page
title: windows/reg-save (中文)
description: "将注册表键、子键的所有值保存到一个文件中。"
content_hash: 6ace2a2f16e65da7379fd88f932fc1fb89cd1b73
related_topics:
  - title: English version
    url: /en/windows/reg-save.html
    icon: bi bi-globe
---
# reg save

将注册表键、子键的所有值保存到一个文件中。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- 将注册表键、子键的所有值保存到一个文件中：

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 在没有提示的情况下强制覆盖现有文件：

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>` /y`
