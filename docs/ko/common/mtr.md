---
layout: page
title: common/mtr (한국어)
description: "Matt's Traceroute: 트레이서라우트와 핑 도구를 결합한 도구."
content_hash: ace76521bce3dd28ddd0931c810122c8ed08e007
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mtr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mtr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mtr

Matt's Traceroute: 트레이서라우트와 핑 도구를 결합한 도구.
더 많은 정보: <https://www.bitwizard.nl/mtr/>.

- 호스트로 트레이서라우트를 수행하고 모든 중간 홉을 지속적으로 핑:

`mtr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 주소 및 호스트 이름 매핑 비활성화:

`mtr --no-dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 각 홉을 10번씩 핑한 후 출력 생성:

`mtr --report-wide `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IPv4 또는 IPv6 강제 사용:

`mtr -4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 동일한 홉에 또 다른 패킷을 보내기 전 주어진 시간(초) 대기:

`mtr --interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 각 홉에 대한 자율 시스템 번호(ASN) 표시:

`mtr --aslookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 주소와 역방향 DNS 이름 모두 표시:

`mtr --show-ips `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
