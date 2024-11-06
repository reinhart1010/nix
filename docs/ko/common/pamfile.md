---
layout: page
title: common/pamfile (한국어)
description: "Netpbm (PAM 또는 PNM) 파일 설명."
content_hash: 484958d7df66ee0a504ac175a8f9b1368dd25e42
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamfile.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamfile

Netpbm (PAM 또는 PNM) 파일 설명.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- 지정된 Netpbm 파일 설명:

`pamfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 각 입력 파일의 모든 이미지를 설명(각 파일의 첫 번째 이미지만이 아닌 모든 이미지)하고 기계 판독 가능한 형식으로 출력:

`pamfile -allimages -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 입력 파일에 포함된 이미지 수를 표시:

`pamfile -count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
