---
layout: page
title: common/middleman (한국어)
description: "Ruby로 작성된 정적 사이트 생성기."
content_hash: 4aa3c3847ef94e6507b29d881f475994f981de52
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/middleman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# middleman

Ruby로 작성된 정적 사이트 생성기.
더 많은 정보: <https://middlemanapp.com/>.

- 새 Middleman 프로젝트 생성:

`middleman init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>`"`

- 현재 프로젝트를 위한 로컬 서버를 포트 4567에서 시작:

`middleman server`

- 지정된 포트에서 현재 프로젝트를 위한 로컬 서버 시작:

`middleman server -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>`"`

- 현재 디렉토리의 프로젝트를 배포 준비를 위해 빌드:

`bundle exec middleman build`

- 현재 디렉토리의 Middleman 프로젝트 배포:

`middleman deploy`
