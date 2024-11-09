---
layout: page
title: linux/tuned-adm (한국어)
description: "Linux에서 시스템 성능 튜닝 프로필을 관리하고 최적화."
content_hash: ddc37c9916dbb511993f2272fbbb5961214c3d75
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tuned-adm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tuned-adm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tuned-adm

Linux에서 시스템 성능 튜닝 프로필을 관리하고 최적화.
더 많은 정보: <https://tuned-project.org>.

- 사용 가능한 프로필 나열:

`tuned-adm list`

- 현재 활성화된 프로필 표시:

`tuned-adm active`

- 특정 튜닝 프로필 설정:

`tuned-adm profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>

- 현재 시스템에 적합한 프로필 추천:

`tuned-adm recommend`

- 튜닝 비활성화:

`tuned-adm off`
