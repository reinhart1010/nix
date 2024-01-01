---
layout: page
title: osx/xsltproc (中文)
description: "用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML）。"
content_hash: 35a56eaaf49bd9d755a42fd89b0a4bb1ed3b3e29
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/osx/xsltproc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xsltproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsltproc

用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML）。
更多信息：<http://www.xmlsoft.org/xslt/xsltproc.html>.

- 使用特定的 XSLT 样式表转换 XML 文件：

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">样式表.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml 文件.xml</span>

- 将值传递给样式表中的参数：

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">样式表.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml 文件.xml</span>
