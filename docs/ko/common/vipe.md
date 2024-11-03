---
layout: page
title: common/vipe (한국어)
description: "UNIX 파이프라인 중간에서 텍스트 편집기를 실행합니다."
content_hash: 166b908f89c850317addfdcb6ea885ebf9132c32
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vipe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vipe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vipe

UNIX 파이프라인 중간에서 텍스트 편집기를 실행합니다.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- `command1`의 출력을 편집한 후 `command2`로 파이핑:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | vipe | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>

- 구문 강조를 돕기 위해 지정된 파일 확장자로 임시 파일에 `command1`의 출력을 버퍼링:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | vipe --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>

- 지정된 텍스트 편집기 사용:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>` vipe | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>
