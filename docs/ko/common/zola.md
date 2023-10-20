---
layout: page
title: common/zola (한국어)
description: "단일 실행 파일에 모든 기능이 들어있는 정적 사이트 생성기."
content_hash: 5283d95df1b1ef685250a744c20caad4b2ee5b7b
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/zola.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zola.html
    icon: bi bi-globe
---
# zola

단일 실행 파일에 모든 기능이 들어있는 정적 사이트 생성기.
더 많은 정보: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- 주어진 디렉토리에 Zola가 사용하는 디렉토리 구조를 생성:

`zola init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_사이트_이름</span>

- `public` 디렉토리에 전체 사이트를 빌드 (이미 존재하는 디렉토리가 있다면 삭제):

`zola build`

- 별도의 디렉토리에 전체 사이트를 빌드:

`zola build --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/</span>

- 사이트를 빌드하고 로컬 서버를 사용하여 제공 (기본 주소는 `127.0.0.1:1111`):

`zola serve`

- `build` 명령어와 같이 모든 페이지를 빌드하지만, 그 결과를 디스크에 기록하지는 않음:

`zola check`
