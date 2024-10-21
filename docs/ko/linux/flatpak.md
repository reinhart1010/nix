---
layout: page
title: linux/flatpak (한국어)
description: "flatpak 애플리케이션 및 런타임을 빌드, 설치, 실행."
content_hash: f83853cbeed51de72183f7640fc5fecefffd1c8b
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/linux/flatpak.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/flatpak.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/flatpak.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flatpak.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/flatpak.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/flatpak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak

flatpak 애플리케이션 및 런타임을 빌드, 설치, 실행.
더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- 설치된 애플리케이션 실행:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- 원격 소스로부터 애플리케이션 설치:

`flatpak install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_소스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- 설치된 애플리케이션 목록 보기 (런타임 제외):

`flatpak list --app`

- 설치된 모든 애플리케이션 및 런타임 업데이트:

`flatpak update`

- 원격 소스 추가:

`flatpak remote-add --if-not-exists `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_소스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_소스_URL</span>

- 설치된 애플리케이션 제거:

`flatpak remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- 사용하지 않는 모든 애플리케이션 제거:

`flatpak remove --unused`

- 설치된 애플리케이션 정보 표시:

`flatpak info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
