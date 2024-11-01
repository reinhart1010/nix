---
layout: page
title: common/ssh-copy-id (한국어)
description: "원격 시스템의 authorized_keys에 공개 키 설치."
content_hash: be947334910e44fd55b5050071b9c9cdaf3c214c
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ssh-copy-id.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ssh-copy-id

원격 시스템의 authorized_keys에 공개 키 설치.
더 많은 정보: <https://manned.org/ssh-copy-id>.

- 키를 원격 시스템에 복사:

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 지정된 공개 키를 원격 시스템에 복사:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 포트로 지정된 공개 키를 원격 시스템에 복사:

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>
