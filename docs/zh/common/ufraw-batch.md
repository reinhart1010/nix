---
layout: page
title: common/ufraw-batch (中文)
description: "将来自相机的 RAW 文件转换为标准图像文件。"
content_hash: 12005490d72567559dcb1358a5cc26164dda47cb
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/ufraw-batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ufraw-batch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ufraw-batch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ufraw-batch

将来自相机的 RAW 文件转换为标准图像文件。
更多信息：<https://manned.org/ufraw-batch>.

- 简单地将 RAW 文件转换为 JPEG：

`ufraw-batch --out-type=jpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">（或多个）输入文件</span>

- 简单地将 RAW 文件转换为 PNG：

`ufraw-batch --out-type=png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">（或多个）输入文件</span>

- 从 RAW 文件中提取预览图像：

`ufraw-batch --embedded-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">（或多个）输入文件</span>

- 将文件保存为不超过给定的最大尺寸 MAX1 和 MAX2：

`ufraw-batch --size=MAX1,MAX2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">（或多个）输入文件</span>
