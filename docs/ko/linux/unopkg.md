---
layout: page
title: linux/unopkg (한국어)
description: "LibreOffice 확장 관리자."
content_hash: 2a6938d2b258421280e6f98df8b432c69319b94b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/unopkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/unopkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unopkg

LibreOffice 확장 관리자.
확장 프로그램 다운로드: <https://extensions.libreoffice.org>.
같이 보기: `libreoffice`.
더 많은 정보: <https://manned.org/unopkg>.

- 지정된 확장을 추가하고 배포:

`unopkg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/확장</span>

- 확장 제거:

`unopkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_ID</span>

- 배포된 확장에 대한 정보 표시:

`unopkg list`

- 확장 대화 상자(GUI) 열기:

`unopkg gui`

- 모든 배포된 확장 재설치:

`unopkg reinstall`

- 도움말 표시:

`unopkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
