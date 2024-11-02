---
layout: page
title: common/tlmgr-generate (한국어)
description: "로컬에 저장된 정보를 바탕으로 구성 파일을 다시 생성."
content_hash: e41f91287984186da240c2d5838c1711d3dd1828
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-generate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr generate

로컬에 저장된 정보를 바탕으로 구성 파일을 다시 생성.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 특정 위치에 구성 파일 저장 후 다시 생성:

`tlmgr generate --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 로컬 구성 파일을 사용하여 구성 파일 다시 생성:

`tlmgr generate --localcfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_구성_파일</span>

- 구성 파일 재구성 후 필요한 프로그램 실행:

`tlmgr generate --rebuild-sys`
