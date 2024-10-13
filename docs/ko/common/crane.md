---
layout: page
title: common/crane (한국어)
description: "컨테이너 이미지 관리 도구."
content_hash: 9cdea4a067c843d41944113995e68e4bad6d2c06
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane

컨테이너 이미지 관리 도구.
`pull`, `push`, `copy` 등과 같은 일부 하위 명령에는 자체 사용 설명서가 있음.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- `crane` 하위 명령을 실행:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 배포할 수 없는 (외부) 레이어 푸시를 허용:

`crane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- TLS 없이 이미지 참조를 가져오록 허용:

`crane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` 형식으로 플랫폼을 지정 (e.g. linux/amd64). (기본값 모두):

`crane  --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 하위 명령에 대한 디버그 로그 활성화:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 하위 명령에 대한 도움말 표시:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>
