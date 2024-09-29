---
layout: page
title: common/chafa (한국어)
description: "터미널에서 이미지 출력."
content_hash: 7b4515667426c704b276ec5da412e5eaaba66518
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/chafa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chafa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chafa

터미널에서 이미지 출력.
참고: `catimg`, `pixterm`.
더 많은 정보: <https://hpjansson.org/chafa/man>.

- 터미널에서 직접 이미지를 렌더링:

`chafa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 24비트 색깔([c]olor) 이미지 렌더링:

`chafa -c full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디더링을 사용하여 작은 색상 팔레트로 이미지 렌더링을 개선:

`chafa -c 16 --dither ordered `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 이미지를 렌더링하여, 픽셀화된 것처럼 보이게 만듬:

`chafa --symbols vhalf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 점자 문자만 사용하여 흑백 이미지를 렌더링:

`chafa -c none --symbols braille `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
