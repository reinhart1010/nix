---
layout: page
title: linux/toolbox-enter (한국어)
description: "대화형 사용을 위해 `toolbox` 컨테이너에 진입."
content_hash: e6ea87bf01a96dfe6652ede8a7a7bb3c8644ae8e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/toolbox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox enter

대화형 사용을 위해 `toolbox` 컨테이너에 진입.
같이 보기: `toolbox run`.
더 많은 정보: <https://manned.org/toolbox-enter.1>.

- 특정 배포판의 기본 이미지를 사용하여 `toolbox` 컨테이너에 진입:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포판</span>

- 현재 배포판의 특정 릴리스의 기본 이미지를 사용하여 `toolbox` 컨테이너에 진입:

`toolbox enter --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스</span>

- Fedora 39의 기본 이미지를 사용하여 toolbox 컨테이너에 진입:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
