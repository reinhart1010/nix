---
layout: page
title: common/hg-status (한국어)
description: "작업 디렉토리에서 변경된 파일을 보여줍니다."
content_hash: 199bcb9c6094ca72b64aebea38eaa4adface9124
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hg-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hg status

작업 디렉토리에서 변경된 파일을 보여줍니다.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#status>.

- 변경된 파일의 상태 표시:

`hg status`

- 수정된 파일만 표시:

`hg status --modified`

- 추가된 파일만 표시:

`hg status --added`

- 제거된 파일만 표시:

`hg status --removed`

- 삭제되었지만 추적된 파일만 표시:

`hg status --deleted`

- 특정 변경 세트와 비교하여 작업 디렉토리의 변경 사항 표시:

`hg status --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전</span>

- 특정 글로브 패턴과 일치하는 파일만 표시:

`hg status --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 특정 글로브 패턴과 일치하지 않는 파일만 표시:

`hg status --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>
