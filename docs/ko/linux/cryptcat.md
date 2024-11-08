---
layout: page
title: linux/cryptcat (한국어)
description: "Cryptcat은 암호화 기능을 갖춘 netcat입니다."
content_hash: f4d7666c7e50e8df5d153f56dfdad8a3e18913ee
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cryptcat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cryptcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cryptcat

Cryptcat은 암호화 기능을 갖춘 netcat입니다.
더 많은 정보: <https://cryptcat.sourceforge.net>.

- 지정된 [p]포트에서 [l]수신하고 받은 데이터를 출력:

`cryptcat -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 포트에 연결:

`cryptcat -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 타임아웃([w]) 지정:

`cryptcat -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초_단위_타임아웃</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 지정된 호스트의 열린 포트 [z]스캔:

`cryptcat -v -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 프록시로 작동하여 로컬 TCP 포트에서 지정된 원격 호스트로 데이터 전달:

`cryptcat -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` | cryptcat -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>
