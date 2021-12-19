---
layout: page
title: common/bmaptool (한국어)
description: "블록 맵을 지능적으로 생성 및 복사( `cp` 혹은 `dd`보다 빠른 속도)."
content_hash: 3db164b1f181291ab4de55cd0a9388e4d9e259b6
related_topics:
  - title: English version
    url: /en/common/bmaptool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bmaptool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bmaptool.html
    icon: bi bi-globe
---
# bmaptool

블록 맵을 지능적으로 생성 및 복사( `cp` 혹은 `dd`보다 빠른 속도).
더 많은 정보: <https://source.tizen.org/documentation/reference/bmaptool>.

- 이미지 파일에서 블록 맵 생성:

`bmaptool create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블록맵.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지 파일</span>

- 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블록맵.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지 파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- 압축된 이미지 파일을 sdb로 복사:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블록맵.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">압축된 이미지 파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- 블록맵을 사용하지 않고 이미지 파일을 sdb로 복사:

`bmaptool copy --nobmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지 파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>
