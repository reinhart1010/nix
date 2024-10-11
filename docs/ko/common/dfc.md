---
layout: page
title: common/dfc (한국어)
description: "색상과 그래프를 통해 파일 시스템 디스크 공간 사용량 요약을 확인."
content_hash: b8793b20cdd46588b540e2048693b68fffe12c35
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/dfc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dfc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dfc

색상과 그래프를 통해 파일 시스템 디스크 공간 사용량 요약을 확인.
더 많은 정보: <https://github.com/Rolinh/dfc>.

- 색상과 그래프를 통해 사람이 읽을 수 있는 형식으로 파일 시스템과 디스크 사용량을 표시:

`dfc`

- 의사적인, 중복 및 액세스할 수 없는 파일 시스템을 포함한 모든 파일 시스템을 표시:

`dfc -a`

- 색상 없이 파일 시스템 표시:

`dfc -c never`

- 파일 시스템 유형에 "ext"가 포함된 파일 시스템 표시:

`dfc -t ext`
