---
layout: page
title: linux/portageq (한국어)
description: "Gentoo Linux 패키지 관리자, Portage에 대한 정보를 조회합니다."
content_hash: 464f2163ec2f274a6680e96afca34c6a64cd7e19
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/portageq.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/portageq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/portageq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># portageq

Gentoo Linux 패키지 관리자, Portage에 대한 정보를 조회합니다.
조회 가능한 Portage 전용 환경 변수가 `/var/db/repos/gentoo/profiles/info_vars`에 나열되어 있습니다.
더 많은 정보: <https://wiki.gentoo.org/wiki/Portageq>.

- Portage 전용 환경 변수의 값을 표시:

`portageq envvar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>

- Portage로 구성된 저장소의 상세 목록 표시:

`portageq repos_config /`

- 우선순위에 따라 정렬된 저장소 목록 표시 (가장 높은 것부터):

`portageq get_repos /`

- 특정 원자(즉, 버전을 포함한 패키지 이름)에 대한 메타데이터 표시:

`portageq metadata / `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ebuild|porttree|binary|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">카테고리</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BDEPEND|DEFINED_PHASES|DEPEND|...</span>
