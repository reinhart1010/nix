---
layout: page
title: linux/paccache (한국어)
description: "`pacman` 캐시 정리 도구."
content_hash: 4285112bfa5350bcfc804522732a219bc191c886
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/paccache.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paccache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paccache

`pacman` 캐시 정리 도구.
더 많은 정보: <https://manned.org/paccache>.

- `pacman` 캐시에서 가장 최근의 3개 버전을 제외한 모든 패키지 버전 제거:

`paccache -r`

- 유지할 패키지 버전 수 설정:

`paccache -rk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전_수</span>

- 시뮬레이션을 수행하고 삭제 후보 패키지 수 표시:

`paccache -d`

- 삭제 대신 후보 패키지를 특정 폴더로 이동:

`paccache -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
