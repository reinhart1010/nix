---
layout: page
title: osx/xsltproc (中文)
description: "用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML）。"
content_hash: b24a4847187867f6c4e0d66550945a10b0eacf5c
related_topics:
  - title: English version
    url: /en/osx/xsltproc.html
    icon: bi bi-globe
---
# xsltproc

用 XSLT 转换 XML 以生成输出（通常是 HTML 或 XML）。
更多信息：<http://www.xmlsoft.org/xslt/xsltproc.html>.

- 使用特定的 XSLT 样式表转换 XML 文件：

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">样式表.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml 文件.xml</span>

- 将值传递给样式表中的参数：

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.html</span>` --stringparam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">样式表.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml 文件.xml</span>
