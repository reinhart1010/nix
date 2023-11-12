---
layout: page
title: osx/xattr (中文)
description: "用于扩展文件系统属性的实用程序。"
content_hash: 01a38e282256af4da74e59d9843cd6e479185bac
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xattr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xattr

用于扩展文件系统属性的实用程序。
更多信息：<https://ss64.com/osx/xattr.html>.

- 列出 键：值 列表，显示指定文件的值扩展属性：

`xattr -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 为给定文件写入属性：

`xattr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">属性键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">属性值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 从给定文件中删除属性：

`xattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.quarantine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 从给定文件中删除所有扩展属性：

`xattr -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 递归删除给定目录中文件的属性：

`xattr -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">属性键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录</span>
