---
layout: page
title: linux/raw (한국어)
description: "Unix 원시 문자 장치를 블록 장치에 바인드합니다."
content_hash: 8bbdf5476daff4232fdb2f9c283dc62418bda8be
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/raw.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/raw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># raw

Unix 원시 문자 장치를 블록 장치에 바인드합니다.
더 많은 정보: <https://manned.org/raw.8>.

- 원시 문자 장치를 블록 장치에 바인드:

`raw /dev/raw/raw`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/block_device</span>

- 새로운 바인딩을 설정하는 대신 기존 바인딩 조회:

`raw /dev/raw/raw`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 바인드된 모든 원시 장치 조회:

`raw -qa`
