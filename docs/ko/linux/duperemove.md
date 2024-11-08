---
layout: page
title: linux/duperemove (한국어)
description: "중복 파일 시스템 익스텐트를 찾아 중복 제거를 예약합니다."
content_hash: b7d8071c1382e1a551203fbc5db2635c180f6e09
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/duperemove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/duperemove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># duperemove

중복 파일 시스템 익스텐트를 찾아 중복 제거를 예약합니다.
익스텐트는 파일 시스템 내 파일의 작은 부분입니다.
일부 파일 시스템에서는 파일의 내용이 동일할 경우 하나의 익스텐트를 여러 번 참조할 수 있습니다.
더 많은 정보: <https://markfasheh.github.io/duperemove/>.

- 디렉토리에서 중복 익스텐트를 검색하고 표시:

`duperemove -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- Btrfs 또는 XFS(실험적) 파일 시스템에서 중복 익스텐트를 중복 제거:

`duperemove -r -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 해시 파일을 사용하여 익스텐트 해시를 저장 (메모리 사용량 감소 및 이후 실행에서 재사용 가능):

`duperemove -r -d --hashfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- I/O 스레드(해싱 및 중복 제거 단계) 및 CPU 스레드(중복 익스텐트 찾기 단계) 제한:

`duperemove -r -d --hashfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시파일</span>` --io-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` --cpu-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
