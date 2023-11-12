---
layout: page
title: common/chgrp (한국어)
description: "파일 및 디렉토리의 그룹 소유권 변경."
content_hash: fcf13d3ca2e44d7016f7b368d1ede1f4f8e02466
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/chgrp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chgrp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chgrp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chgrp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chgrp

파일 및 디렉토리의 그룹 소유권 변경.
더 많은 정보: <https://www.gnu.org/software/coreutils/chgrp>.

- 파일/디렉토리의 소유 그룹 변경:

`chgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명_또는_디렉토리명</span>

- 디렉토리 및 해당 컨텐츠의 소유 그룹 변경:

`chgrp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/디렉토리명</span>

- 심볼릭 링크의 소유 그룹 변경:

`chgrp -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/심볼릭_링크</span>

- 참조 파일과 일치하도록 파일/디렉토리의 소유 그룹 변경:

`chgrp --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/참조_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명_또는_디렉토리명</span>
