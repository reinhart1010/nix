---
layout: page
title: windows/assoc (中文)
description: "显示或修改文件扩展名关联。"
content_hash: 91097dba257d2236c5b008ab6d4db27098582cea
related_topics:
  - title: English version
    url: /en/windows/assoc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
---
# assoc

显示或修改文件扩展名关联。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- 显示所有当前文件扩展名关联的列表：

`assoc`

- 显示指定扩展名的关联文件类型：

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- 将文件扩展名与特定的文件类型关联：

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txtfile</span>
