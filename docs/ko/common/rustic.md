---
layout: page
title: common/rustic (한국어)
description: "빠르고 암호화된 중복 제거 백업을 Rust로 생성."
content_hash: 710ca689c302fb9e40fea9708c85b092ba989600
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustic

빠르고 암호화된 중복 제거 백업을 Rust로 생성.
더 많은 정보: <https://github.com/rustic-rs/rustic>.

- 새 저장소 초기화:

`rustic init --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/srv/rustic-repo</span>

- 파일/디렉토리의 새 백업을 저장소에 생성:

`rustic backup --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/srv/rustic-repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
