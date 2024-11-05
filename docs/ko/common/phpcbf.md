---
layout: page
title: common/phpcbf (한국어)
description: "phpcs에서 감지된 위반 사항 수정."
content_hash: 872b35e5a7f8af7653ff5bba9f36da021d907a93
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpcbf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpcbf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpcbf

phpcs에서 감지된 위반 사항 수정.
더 많은 정보: <https://github.com/squizlabs/PHP_CodeSniffer>.

- 지정된 디렉터리의 문제 수정 (기본적으로 PEAR 표준 사용):

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 설치된 코딩 표준 목록 표시:

`phpcbf -i`

- 검사할 코딩 표준 지정:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표준</span>

- 쉼표로 구분된 파일 확장자를 지정하여 스니핑할 때 포함:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_확장자1,파일_확장자2,...</span>

- 처리 전에 로드할 쉼표로 구분된 파일 목록:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1,경로/대상/파일2,...</span>

- 하위 디렉터리로 재귀하지 않음:

`phpcbf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -l`
