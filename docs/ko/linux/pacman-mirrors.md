---
layout: page
title: linux/pacman-mirrors (한국어)
description: "Manjaro Linux용 `pacman` 미러 리스트 생성."
content_hash: 771645299a95ac644b680722bc652b4d1f1538e4
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-mirrors.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-mirrors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-mirrors

Manjaro Linux용 `pacman` 미러 리스트 생성.
`pacman-mirrors`를 실행할 때마다 데이터베이스를 동기화하고 `sudo pacman -Syyu`를 사용하여 시스템을 업데이트해야 합니다.
같이 보기: `pacman`.
더 많은 정보: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- 기본 설정을 사용하여 미러 리스트 생성:

`sudo pacman-mirrors --fasttrack`

- 현재 미러 상태 확인:

`pacman-mirrors --status`

- 현재 브랜치 표시:

`pacman-mirrors --get-branch`

- 다른 브랜치로 전환:

`sudo pacman-mirrors --api --set-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|unstable|testing</span>

- 거주 국가의 미러만 사용하여 미러 리스트 생성:

`sudo pacman-mirrors --geoip`
