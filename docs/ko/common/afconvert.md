---
layout: page
title: common/afconvert (한국어)
description: "AFF와 원시 파일 형식 간의 변환."
content_hash: 79b51931ebb8c29782e9cbedea19aad34ccb6c4a
last_modified_at: 2023-12-05
related_topics:
  - title: English version
    url: /en/common/afconvert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/afconvert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/afconvert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/afconvert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/afconvert.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/afconvert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/afconvert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># afconvert

AFF와 원시 파일 형식 간의 변환.
더 많은 정보: <https://manned.org/afconvert.1>.

- 특정 확장자 사용(기본값: `aff`):

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일1 경로/대상/출력_파일2 ...</span>

- 특정 압축 단계 사용(기본값: `7`):

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일1 경로/대상/출력_파일2 ...</span>
