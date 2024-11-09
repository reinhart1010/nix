---
layout: page
title: common/tarsnap-keygen (한국어)
description: "Tarsnap, 온라인 백업 서비스에서 사용할 키 파일을 생성."
content_hash: ddd4cb9cde9627c98ba5a1e1d5def5e5663fac7f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tarsnap-keygen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tarsnap-keygen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tarsnap-keygen

Tarsnap, 온라인 백업 서비스에서 사용할 키 파일을 생성.
더 많은 정보: <https://www.tarsnap.com/man-tarsnap-keygen.1.html>.

- Tarsnap 서버에 컴퓨터 등록:

`sudo tarsnap-keygen --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.key</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이메일</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터_이름</span>

- 키 파일 암호화(암호문을 두 번 입력해야 함):

`sudo tarsnap-keygen --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.key</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이메일</span>` --machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컴퓨터_이름</span>` --passphrased`
