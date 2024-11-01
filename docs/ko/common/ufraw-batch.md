---
layout: page
title: common/ufraw-batch (한국어)
description: "카메라의 RAW 파일을 표준 이미지 파일로 변환."
content_hash: 230e1a0d035513d5b84da562b0ef11de09a77a67
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/ufraw-batch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ufraw-batch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ufraw-batch

카메라의 RAW 파일을 표준 이미지 파일로 변환.
더 많은 정보: <https://manned.org/ufraw-batch>.

- RAW 파일을 JPEG로 변환:

`ufraw-batch --out-type=jpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일(들)</span>

- RAW 파일을 PNG로 변환:

`ufraw-batch --out-type=png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일(들)</span>

- RAW 파일에서 미리보기 이미지 추출:

`ufraw-batch --embedded-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일(들)</span>

- 파일을 최대 크기 MAX1 및 MAX2로 저장:

`ufraw-batch --size=MAX1,MAX2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일(들)</span>
