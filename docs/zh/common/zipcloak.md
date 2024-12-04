---
layout: page
title: common/zipcloak (中文)
description: "加密 Zip 压缩档案内的内容。"
content_hash: 830a821aae663afc13e5f1c067370ef0ff6c03c3
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zipcloak.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zipcloak.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zipcloak.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipcloak.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipcloak

加密 Zip 压缩档案内的内容。
更多信息：<https://manned.org/zipcloak>.

- 加密一个 Zip 压缩档案的内容：

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩档案.zip</span>

- [d]解密一个 Zip 压缩档案的内容：

`zipcloak -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩档案.zip</span>

- [O]将加密内容输出到一个新的 Zip 压缩档案中：

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩档案.zip</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/加密.zip</span>
