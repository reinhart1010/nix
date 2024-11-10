---
layout: page
title: common/stdbuf (한국어)
description: "표준 스트림에 대한 버퍼링 작업을 수정하여 명령을 실행."
content_hash: 6311984ce554d71d5d565795b41dbe17b2d652c3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stdbuf.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/stdbuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stdbuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stdbuf

표준 스트림에 대한 버퍼링 작업을 수정하여 명령을 실행.
더 많은 정보: <https://www.gnu.org/software/coreutils/stdbuf>.

- `stdin` 버퍼 크기를 512 KiB로 변경:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- `stdout` 버퍼를 라인 버퍼로 변경:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- `stderr` 버퍼를 버퍼링하지 않도록 변경:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
