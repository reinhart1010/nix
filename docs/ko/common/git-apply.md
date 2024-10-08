---
layout: page
title: common/git-apply (한국어)
description: "커밋을 생성하지 않고 파일 및/또는 색인에 패치를 적용합니다."
content_hash: 9a8fee238d04884b5feb2b0b166b7e8b2eed5ca9
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-apply.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git apply

커밋을 생성하지 않고 파일 및/또는 색인에 패치를 적용합니다.
같이 보기: `git am` (패치를 적용하고 커밋도 생성).
더 많은 정보: <https://git-scm.com/docs/git-apply>.

- 패치된 파일에 대한 메시지 출력:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패치를 적용하고 패치된 파일을 색인에 추가:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 원격 패치 파일 적용:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- 입력에 대한 diffstat을 출력하고 패치를 적용:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패치를 역방향으로 적용:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 작업 트리를 수정하지 않고 패치 결과를 색인에 저장:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
