---
layout: page
title: common/immich-go (한국어)
description: "Immich-Go는 대규모 사진 컬렉션을 자체 호스팅 Immich 서버에 업로드하는 작업을 간소화하도록 설계된 오픈소스 도구."
content_hash: 36a587eadd22f8e63d7ba879fe530f62349e52ad
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/immich-go.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/immich-go.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/immich-go.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># immich-go

Immich-Go는 대규모 사진 컬렉션을 자체 호스팅 Immich 서버에 업로드하는 작업을 간소화하도록 설계된 오픈소스 도구.
참고: `immich-cli`.
더 많은 정보: <https://github.com/simulot/immich-go>.

- Google 사진 테이크아웃 파일을 Immich 서버에 업로드:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_키</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테이크아웃_파일.zip</span>

- 앨범을 자동 생성하면서 2019년 6월에 촬영한 사진을 가져옴:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_키</span>` upload -create-albums -google-photos -date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2019-06</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테이크아웃_파일.zip</span>

- 구성 파일의 서버 및 키를 사용하여 테이크아웃 파일 업로드:

`immich-go -use-configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.immich-go/immich-go.json</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테이크아웃_파일.zip</span>

- Immich 서버 콘텐츠를 검사하고, 품질이 낮은 이미지를 제거하고, 엘범을 보존:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_키</span>` duplicate -yes`

- "YYYY-MM-DD" 패턴으로 생성된 모든 앨범 삭제:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_주소</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_키</span>` tool album delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\d{4}-\d{2}-\d{2}</span>
