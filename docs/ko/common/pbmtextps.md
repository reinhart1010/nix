---
layout: page
title: common/pbmtextps (한국어)
description: "텍스트를 PostScript를 사용하여 PBM 이미지로 렌더링."
content_hash: 0630b2995987ac4b0d292898626d220945eb71ad
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtextps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtextps

텍스트를 PostScript를 사용하여 PBM 이미지로 렌더링.
같이 보기: `pbmtext`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtextps.html>.

- 한 줄의 텍스트를 PBM 이미지로 렌더링:

`pbmtextps "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 폰트와 폰트 크기 지정:

`pbmtextps -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times-Roman</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 원하는 좌측 및 상단 여백 지정:

`pbmtextps -leftmargin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">70</span>` -topmargin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">162</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 렌더링된 텍스트를 PBM 이미지로 출력하지 않고, 이 이미지를 생성할 PostScript 프로그램으로 출력:

`pbmtextps -dump-ps "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ps</span>
