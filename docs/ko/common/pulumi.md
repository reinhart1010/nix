---
layout: page
title: common/pulumi (한국어)
description: "친숙한 프로그래밍 언어를 사용하여 어떤 클라우드에서도 인프라 정의."
content_hash: 66bfd1a813cec79339a1a2267f454d1882b3cea4
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pulumi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi

친숙한 프로그래밍 언어를 사용하여 어떤 클라우드에서도 인프라 정의.
`up`과 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://www.pulumi.com/docs/cli>.

- 템플릿을 사용하여 새 프로젝트 생성:

`pulumi new`

- 격리된 배포 대상을 사용하여 새 스택 생성:

`pulumi stack init`

- 변수를 대화식으로 구성 (예: 키, 지역 등):

`pulumi config`

- 프로그램 및/또는 인프라에 대한 변경 사항 미리보기 및 배포:

`pulumi up`

- 배포 변경 사항을 수행하지 않고 미리보기 (드라이런):

`pulumi preview`

- 프로그램 및 그 인프라 삭제:

`pulumi destroy`

- Pulumi Cloud와 독립적으로 Pulumi를 로컬에서 사용:

`pulumi login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--local</span>
