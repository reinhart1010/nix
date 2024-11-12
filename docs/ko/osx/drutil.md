---
layout: page
title: osx/drutil (한국어)
description: "DVD 버너와 상호 작용."
content_hash: afc20fcc28c9ca593fc986e030f633db12c57e2d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/drutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/drutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/drutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# drutil

DVD 버너와 상호 작용.
더 많은 정보: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- 드라이브에서 디스크 배출:

`drutil eject`

- 디렉토리를 ISO9660 파일 시스템으로 DVD에 굽기. 검증하지 않고 완료 시 배출:

`drutil burn -noverify -eject -iso9660`
