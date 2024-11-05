---
layout: page
title: common/phpspec (한국어)
description: "PHP용 행동 주도 개발 도구."
content_hash: 3d48548a48e4e8f7b43519267ae0571345be4a87
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpspec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpspec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpspec

PHP용 행동 주도 개발 도구.
더 많은 정보: <https://phpspec.net>.

- 클래스에 대한 사양 작성:

`phpspec describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름</span>

- "spec" 폴더의 모든 사양 실행:

`phpspec run`

- 단일 사양 실행:

`phpspec run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/클래스_사양_파일</span>

- 특정 구성 파일을 사용하여 사양 실행:

`phpspec run -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>

- 특정 부트스트랩 파일을 사용하여 사양 실행:

`phpspec run -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/부트스트랩_파일</span>

- 코드 생성 프롬프트 비활성화:

`phpspec run --no-code-generation`

- 가짜 반환 값 활성화:

`phpspec run --fake`
