---
layout: page
title: linux/trust (한국어)
description: "신뢰 정책 저장소를 운영합니다."
content_hash: 12f6efad4ad1a8bda98e20917d31bc585a27cae3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/trust.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/trust.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trust

신뢰 정책 저장소를 운영합니다.
더 많은 정보: <https://manned.org/trust>.

- 신뢰 정책 저장소 항목 나열:

`trust list`

- 신뢰 정책 저장소의 특정 항목에 대한 정보 나열:

`trust list --filter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blocklist|ca-anchors|certificates|trust-policy</span>

- 특정 신뢰 앵커를 신뢰 정책 저장소에 저장:

`trust anchor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.crt</span>

- 특정 앵커를 신뢰 정책 저장소에서 제거:

`trust anchor --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.crt</span>

- 공유 신뢰 정책 저장소에서 신뢰 정책 추출:

`trust extract --format=x509-directory --filter=ca-anchors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 하위 명령에 대한 도움말 표시:

`trust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
