---
layout: page
title: common/fly (한국어)
description: "concourse-ci용 명령줄 도구."
content_hash: 6923dcdb918080df19238f7e965f5d710697b329
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fly.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fly.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fly

concourse-ci용 명령줄 도구.
더 많은 정보: <https://concourse-ci.org/fly.html>.

- concourse 대상으로 인증 및 저장:

`fly --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` login --team-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">팀_이름</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ci.example.com</span>

- 타겟 나열:

`fly targets`

- 파이프라인 나열:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` pipelines`

- 파이프라인 업로드 또는 업데이트:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` set-pipeline --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipeline.yml</span>` --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>

- 파이프라인 일시중지 해제:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` unpause-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>

- 파이프라인 구성 표시:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` get-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>

- fly의 로컬 사본 업데이트:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` sync`

- 파이프라인 삭제:

`fly -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_이름</span>` destroy-pipeline --pipeline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프라인_이름</span>
