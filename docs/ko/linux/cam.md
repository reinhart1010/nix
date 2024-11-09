---
layout: page
title: linux/cam (한국어)
description: "`libcamera`의 프론트엔드 도구."
content_hash: a6c906bbf6d890215aeed6af55ee5e14ed245ab4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cam

`libcamera`의 프론트엔드 도구.
더 많은 정보: <https://libcamera.org/docs.html>.

- 사용 가능한 카메라 나열:

`cam --list`

- 카메라의 컨트롤 나열:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">카메라_인덱스</span>` --list-controls`

- 프레임을 폴더에 저장:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">카메라_인덱스</span>` --capture=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캡처할_프레임_수</span>` --file`

- 창에 카메라 피드 표시:

`cam --camera `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">카메라_인덱스</span>` --capture --sdl`
