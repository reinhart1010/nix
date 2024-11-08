---
layout: page
title: linux/dropbearkey (한국어)
description: "Dropbear 형식으로 SSH 키를 생성합니다."
content_hash: c774a676a6a221bfae9ad3c7ee42a4594ae9b3f7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dropbearkey.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dropbearkey.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dropbearkey

Dropbear 형식으로 SSH 키를 생성합니다.
더 많은 정보: <https://manned.org/dropbearkey.1>.

- [t]유형 ed25519의 SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>

- [t]유형 ecdsa의 SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ecdsa</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>

- 4096비트 키 [s]크기의 [t]유형 RSA SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>

- 키 [f]파일의 개인 키 지문과 공개 키 출력:

`dropbearkey -y -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>
