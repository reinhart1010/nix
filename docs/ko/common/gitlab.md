---
layout: page
title: common/gitlab (한국어)
description: "GitLab API용 Ruby 래퍼."
content_hash: 4fdc2c546b72b6d40bfb61e87bccf7848d412c1e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/common/gitlab.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitlab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitlab

GitLab API용 Ruby 래퍼.
`ctl`과 같은 일부 하위 명령에는 자체 사용법 문서가 존재.
더 많은 정보: <https://narkoz.github.io/gitlab/>.

- 새로운 프로젝트를 생성:

`gitlab create_project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 특정 커밋에 대한 정보를 얻기:

`gitlab commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시</span>

- CI 파이프라인의 작업에 대한 정보를 얻기:

`gitlab pipeline_jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_아이디</span>

- 특정 CI 작업을 시작:

`gitlab job_play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>
