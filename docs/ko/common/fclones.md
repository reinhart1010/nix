---
layout: page
title: common/fclones (한국어)
description: "효율적인 중복 파일 찾기 및 제거기."
content_hash: 34038738f45694d91f0a920994dc682951d98014
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fclones.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/fclones.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fclones

효율적인 중복 파일 찾기 및 제거기.
더 많은 정보: <https://github.com/pkolaczk/fclones>.

- 현재 디렉터리에서 중복 파일 검색:

`fclones group .`

- 여러 디렉터리에서 중복 파일을 검색하고 결과를 캐시:

`fclones group --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2</span>

- 하위 디렉터리를 건너 뛰고, 지정된 디렉터리에서만 중복 파일을 검색하고 결과를 파일에 저장:

`fclones group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` --depth 1 > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- TXT 파일의 중복 파일을 다른 디렉터리로 이동:

`fclones move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 실제로 연결하지 않고 TXT 파일의 소프트 링크에 대해 연습 실행을 수행:

`fclones link --soft < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` --dry-run 2 > /dev/null`

- 파일에 저장하지 않고 현재 디렉터리에서 최신 복사본을 삭제:

`fclones group . | fclones remove --priority newest`

- 중복 항목을 찾기 전에 EXIF 데이터를 제거하는 외부 명령을 사용하여 현재 디렉터리의 JPEG 파일을 전처리:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`
