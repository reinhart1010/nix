---
layout: page
title: linux/sport (한국어)
description: "SlackBuilds 검색 및 설치."
content_hash: acb7b8123daedf0e45b3c117d3b88940e5b8d114
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sport.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/sport.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sport.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sport

SlackBuilds 검색 및 설치.
더 많은 정보: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- `sport`를 처음 실행하기 위해 SlackBuild 목록 가져오기:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- `rsync`를 통해 시스템 트리의 업데이트 가져오기:

`sudo sport rsync`

- 이름으로 패키지 검색:

`sport search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>`"`

- 패키지가 설치되었는지 확인:

`sport check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지의 README 및 `.info` 파일 표시:

`sport cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 의존성이 해결된 후 패키지 설치:

`sudo sport install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 파일에 있는 패키지 목록 설치 (형식: 공백으로 구분된 패키지):

`sudo sport install $(< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목록</span>`)`
