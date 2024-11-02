---
layout: page
title: common/kate (한국어)
description: "KDE의 고급 텍스트 편집기."
content_hash: c00e377edc953d641848dae5d8bf46958386bc4c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kate

KDE의 고급 텍스트 편집기.
더 많은 정보: <https://kate-editor.org/>.

- 특정 파일 열기:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 원격 파일 열기:

`kate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/경로/대상/파일1 https://example.com/경로/대상/파일2 ...</span>

- 이미 열려 있는 경우에도 새 편집기 인스턴스 생성:

`kate --new`

- 특정 줄에 커서를 놓고 파일 열기:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 줄과 열에 커서를 놓고 파일 열기:

`kate --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 파일 생성:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | kate --stdin`

- 도움말 표시:

`kate --help`
