---
layout: page
title: common/inkmake (한국어)
description: "Inkscape의 백엔드를 사용하여 GNU Makefile 스타일 SVG 내보내기."
content_hash: d460c27d9af2cebdb2226414bc04ac3d68a45b97
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/inkmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# inkmake

Inkscape의 백엔드를 사용하여 GNU Makefile 스타일 SVG 내보내기.
더 많은 정보: <https://github.com/wader/inkmake>.

- 지정된 Inkfile을 실행하는 SVG 파일 내보내기:

`inkmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Inkfile</span>

- Inkfile을 실행하고 자세한 정보를 표시:

`inkmake --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Inkfile</span>

- SVG 입력 파일과 출력 파일을 지정하여, Inkfile을 실행:

`inkmake --svg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.svg</span>` --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Inkfile</span>

- 사용자 정의 Inkscape 바이너리를 백엔드로 사용:

`inkmake --inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Applications/Inkscape.app/Contents/Resources/bin/inkscape</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Inkfile</span>

- 도움말 표시:

`inkmake --help`
