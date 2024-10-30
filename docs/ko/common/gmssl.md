---
layout: page
title: common/gmssl (한국어)
description: "GmSSL은 SM1, SM2, SM3, SM4, SM9 및 ZUC/ZUC256을 지원하는 암호화 툴킷."
content_hash: d541e2a1b2a569323867fc4616d327a0caec9173
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gmssl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gmssl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gmssl

GmSSL은 SM1, SM2, SM3, SM4, SM9 및 ZUC/ZUC256을 지원하는 암호화 툴킷.
더 많은 정보: <http://gmssl.org/english.html>.

- 파일에 대한 SM3 해시를 생성:

`gmssl sm3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- SM4 암호를 사용하여 파일을 암호화:

`gmssl sms4 -e -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sms4</span>

- SM4 암호를 사용하여 파일을 복호화:

`gmssl sms4 -d -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sms4</span>

- SM2 개인키를 생성:

`gmssl sm2 -genkey -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pem</span>

- 기존 개인 키에서 SM2 공개키를 생성:

`gmssl sm2 -pubout -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pem</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pem.pub</span>

- ZUC 암호를 사용하여 파일을 암호화:

`gmssl zuc -e -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zuc</span>

- ZUC 암호를 사용하여 파일을 복호화:

`gmssl zuc -d -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zuc</span>

- 버전 정보 출력:

`gmssl version`
