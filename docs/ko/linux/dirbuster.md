---
layout: page
title: linux/dirbuster (한국어)
description: "서버에서 디렉터리와 파일명을 무차별 대입으로 찾기."
content_hash: 00382fe116d54517da1091bc5c849d19c4de119d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dirbuster.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirbuster

서버에서 디렉터리와 파일명을 무차별 대입으로 찾기.
더 많은 정보: <https://www.kali.org/tools/dirbuster/>.

- GUI 모드로 시작:

`dirbuster -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 헤드리스(무 GUI) 모드로 시작:

`dirbuster -H -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 파일 확장자 목록 설정:

`dirbuster -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt,html</span>

- 자세한 출력 활성화:

`dirbuster -v`

- 보고서 위치 설정:

`dirbuster -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/보고서.txt</span>
