---
layout: page
title: windows/reg-export (中文)
description: "将指定的子键和值导出到文件中。"
content_hash: dc8efe375ec955a6a85478b1ef9a67cb7f2df44a
related_topics:
  - title: English version
    url: /en/windows/reg-export.html
    icon: bi bi-globe
---
# reg export

将指定的子键和值导出到文件中。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- 导出指定键下所有的子键和值：

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导出文件的路径.reg</span>

- 在没有提示的情况下强制覆盖现有文件：

`reg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">导出文件的路径.reg</span>` /y`
