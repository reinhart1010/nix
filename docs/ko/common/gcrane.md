---
layout: page
title: common/gcrane (한국어)
description: "컨테이너 이미지 관리."
content_hash: f1dc20780b643df15196fc1d939ca95eb7829635
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gcrane.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcrane.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcrane

컨테이너 이미지 관리.
이 도구는 `gcr.io`와 관련된 추가 명령과 함께 `crane` 명령의 상위 집합을 구현.
`append`, `auth`, `copy` 등과 같은 일부 하위 명령에는 `crane` 아래에서 찾을 수 있는 자체 사용법 문서가 존재.
`completion`, `gc`, `help`와 같은 일부 하위 명령은 gcrane에만 해당되며 자체 사용 문서가 있음.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- `gcrane` 하위 명령을 실행:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 배포할 수 없는 (외부) 레이어 푸시를 허용:

`gcrane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- TLS 없이 이미지 참조를 가져오도록 허용:

`gcrane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` 형식으로 플랫폼을 지정 (예: linux/amd64). (기본값은 모두):

`gcrane --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 디버그 로그 활성화:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 도움말 표시:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
