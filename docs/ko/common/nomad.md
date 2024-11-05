---
layout: page
title: common/nomad (한국어)
description: "분산형, 고가용성, 데이터센터 인식 스케줄러."
content_hash: a0a31b02a3d714fdc38fce4e273dbbdc8469c0f8
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nomad.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nomad.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nomad

분산형, 고가용성, 데이터센터 인식 스케줄러.
더 많은 정보: <https://www.nomadproject.io/docs/commands/>.

- 클러스터 내 노드의 상태 표시:

`nomad node status`

- 작업 파일 유효성 검사:

`nomad job validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nomad</span>

- 클러스터에서 실행할 작업 계획:

`nomad job plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nomad</span>

- 클러스터에서 작업 실행:

`nomad job run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.nomad</span>

- 현재 클러스터에서 실행 중인 작업의 상태 표시:

`nomad job status`

- 특정 작업에 대한 상세 상태 정보 표시:

`nomad job status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 특정 할당의 로그를 지속적으로 팔로우:

`nomad alloc logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할당_id</span>

- 스토리지 볼륨의 상태 표시:

`nomad volume status`
