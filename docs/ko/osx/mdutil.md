---
layout: page
title: osx/mdutil (한국어)
description: "Spotlight의 색인을 위한 메타데이터 저장소 관리 도구."
content_hash: 39d57c22e42d32768701f9f811c50a76cd97daae
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/mdutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mdutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdutil

Spotlight의 색인을 위한 메타데이터 저장소 관리 도구.
더 많은 정보: <https://keith.github.io/xcode-man-pages/mdutil.1.html>.

- 시작 볼륨의 색인 상태 표시:

`mdutil -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- 특정 볼륨의 Spotlight 색인 기능 켜기/끄기:

`mdutil -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨</span>

- 모든 볼륨의 색인 기능 켜기/끄기:

`mdutil -a -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 메타데이터 저장소를 지우고 색인 프로세스 재시작:

`mdutil -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/볼륨</span>
