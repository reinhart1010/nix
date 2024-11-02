---
layout: page
title: common/pbmupc (한국어)
description: "범용 상품 코드(UPC)의 PBM 이미지를 생성합니다."
content_hash: 175f109b1202812dd84efc1d4fb3ea7a2c51e1ec
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmupc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmupc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmupc

범용 상품 코드(UPC)의 PBM 이미지를 생성합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmupc.html>.

- 지정된 상품 유형, 제조사 코드 및 상품 코드를 위한 UPC 이미지 생성:

`pbmupc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상품_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제조사_코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상품_코드</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 체크섬을 표시하지 않는 대체 스타일 사용:

`pbmupc -s2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상품_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제조사_코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상품_코드</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
