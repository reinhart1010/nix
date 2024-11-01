---
layout: page
title: common/tlmgr-option (한국어)
description: "TeX Live 설정 관리자."
content_hash: 2e7d259558bce59c592553e352cb7449c6c5050b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-option.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-option.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr option

TeX Live 설정 관리자.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 모든 TeX Live 설정 나열:

`tlmgr option showall`

- 현재 설정된 모든 TeX Live 설정 나열:

`tlmgr option show`

- 모든 TeX Live 설정을 JSON 형식으로 출력:

`tlmgr option showall --json`

- 특정 TeX Live 설정의 값 표시:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정</span>

- 특정 TeX Live 설정의 값 수정:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- DVD로 설치 후 인터넷에서 향후 업데이트를 받도록 TeX Live 설정:

`tlmgr option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mirror.ctan.org/systems/texlive/tlnet</span>
