---
layout: page
title: linux/repo-add (한국어)
description: "Pacman을 통해 해당 패키지의 설치를 가능하게 하는 패키지 데이터베이스 유지 관리 유틸리티."
content_hash: 65244638e48199e32a8fe678a41b4e7bd1fe71df
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/repo-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/repo-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># repo-add

Pacman을 통해 해당 패키지의 설치를 가능하게 하는 패키지 데이터베이스 유지 관리 유틸리티.
더 많은 정보: <https://manned.org/repo-add>.

- 빈 저장소 생성:

`repo-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.db.tar.gz</span>

- 현재 디렉토리의 모든 패키지 바이너리를 추가하고 기존 데이터베이스 파일 제거:

`repo-add --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- 경고 및 오류 메시지를 제외하고 조용한 모드로 현재 디렉토리의 모든 패키지 바이너리 추가:

`repo-add --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>

- 색상을 표시하지 않고 현재 디렉토리의 모든 패키지 바이너리 추가:

`repo-add --nocolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터베이스.db.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.pkg.tar.zst</span>
