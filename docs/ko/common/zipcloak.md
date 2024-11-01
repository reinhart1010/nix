---
layout: page
title: common/zipcloak (한국어)
description: "Zip 아카이브 내의 내용을 암호화."
content_hash: 86f69e3f8db7157248662be3b7dad53416d00f60
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zipcloak.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zipcloak.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zipcloak.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zipcloak

Zip 아카이브 내의 내용을 암호화.
더 많은 정보: <https://manned.org/zipcloak>.

- Zip 아카이브의 내용을 암호화:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- Zip 아카이브의 내용을 [d]복호화:

`zipcloak -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 암호화된 내용을 새로운 Zip 아카이브로 [O]출력:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화됨.zip</span>
