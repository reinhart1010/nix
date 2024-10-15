---
layout: page
title: common/magick-import (한국어)
description: "X 서버 화면의 일부 또는 전체를 캡처하여 파일로 저장."
content_hash: bbf64616343374e9790d3824f9dc0c2fa6c8995c
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/magick-import.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-import.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick import

X 서버 화면의 일부 또는 전체를 캡처하여 파일로 저장.
같이 보기: `magick`.
더 많은 정보: <https://imagemagick.org/script/import.php>.

- 전체 X 서버 화면을 PostScript 파일로 캡처:

`magick import -window root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.ps</span>

- 원격 X 서버 화면의 내용을 PNG 이미지로 캡처:

`magick import -window root -display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">화면</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.png</span>

- `xwininfo`로 표시된 ID를 가진 특정 창을 JPEG 이미지로 캡처:

`magick import -window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.jpg</span>
