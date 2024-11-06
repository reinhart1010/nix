---
layout: page
title: common/pamenlarge (한국어)
description: "픽셀을 복제하여 PAM 이미지를 확대합니다."
content_hash: e85f69ab7a1794a14371b91db96c147562fd668c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamenlarge.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamenlarge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamenlarge

픽셀을 복제하여 PAM 이미지를 확대합니다.
같이 보기: `pbmreduce`, `pamditherbw`, `pbmpscale`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

- 지정된 이미지를 주어진 배율로 확대:

`pamenlarge -scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 지정된 이미지를 가로 및 세로로 주어진 배율로 확대:

`pamenlarge -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
