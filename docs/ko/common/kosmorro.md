---
layout: page
title: common/kosmorro (한국어)
description: "특정 날짜 및 지구상의 위치에 대한 천체력 및 이벤트를 계산."
content_hash: e36630e491b7bd41a588f9ed271d4fc9950c94bf
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kosmorro.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kosmorro.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kosmorro

특정 날짜 및 지구상의 위치에 대한 천체력 및 이벤트를 계산.
더 많은 정보: <https://kosmorro.space>.

- 프랑스 파리의 천체력 얻기:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>

- UTC+2 시간대의 프랑스 파리의 천체력 얻기:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --timezone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 2020년 6월 9일의 프랑스 파리의 천체력 얻기:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-06-09</span>

- PDF 생성 (참고: TeXLive가 설치되어 있어야 함):

`kosmorro --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
