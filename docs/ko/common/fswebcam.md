---
layout: page
title: common/fswebcam (한국어)
description: "작고 간단한 \*nix용 웹캠."
content_hash: 5b1b05b8585c0468e175100a8997046b683ffa2c
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/fswebcam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fswebcam

작고 간단한 \*nix용 웹캠.
더 많은 정보: <https://www.sanslogic.co.uk/fswebcam>.

- 사진을 찍음:

`fswebcam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>

- 사용자 정의 해상도로 사진 찍기:

`fswebcam -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>

- 선택한 장치에서 사진을 찍음(기본값 `/dev/video0`):

`fswebcam -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>

- 타임스탬프가 있는 사진을 찍음(타임스탬프 문자열은 strftime로 형식화됨):

`fswebcam --timestamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임스탬프</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>
