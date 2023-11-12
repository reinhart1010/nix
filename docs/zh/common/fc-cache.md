---
layout: page
title: common/fc-cache (中文)
description: "扫描字体目录，以便建立字体缓存文件。"
content_hash: f7015214e3b7a4cecb29768bb1dd6b63e71a405f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fc-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc-cache

扫描字体目录，以便建立字体缓存文件。
更多信息：<https://manned.org/fc-cache>.

- 生成字体缓存文件：

`fc-cache`

- 强制重建所有字体缓存文件，而不检查缓存是否为最新版本：

`fc-cache -f`

- 删除字体缓存文件，然后生成新的字体缓存文件：

`fc-cache -r`
