---
layout: page
title: common/zopflipng (中文)
description: "PNG 压缩工具。"
content_hash: 518d95b26e54007c272eab47d9782caf567462b1
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zopflipng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zopflipng.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zopflipng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zopflipng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zopflipng

PNG 压缩工具。
更多信息：<https://github.com/google/zopfli>.

- 优化一个 PNG 文件：

`zopflipng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出.png</span>

- 优化多个 PNG 文件并使用给定的前缀保存：

`zopflipng --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">前缀</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像3.png</span>
