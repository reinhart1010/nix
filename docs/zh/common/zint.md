---
layout: page
title: common/zint (中文)
description: "生成条形码和二维码。"
content_hash: df9ca2486d53228da351e7bb8dc869744874164c
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zint.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zint

生成条形码和二维码。
更多信息：<https://www.zint.org.uk/manual/chapter/4>.

- 生成一个条形码并保存：

`zint --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 数据</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 指定生成的编码类型：

`zint --barcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">编码类型</span>` --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 数据</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 列出所有支持的编码类型：

`zint --types`
