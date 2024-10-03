---
layout: page
title: common/cargo-yank (한국어)
description: "색인에서 밀린 상자를 제거, 이 방법은 실수로 심하게 파손된 크레이트를 놓은 경우에만 사용해야 함."
content_hash: 652b569b36d12f2c527004e5e57e3e9e2f1b7061
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-yank.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-yank.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-yank.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo yank

색인에서 밀린 상자를 제거, 이 방법은 실수로 심하게 파손된 크레이트를 놓은 경우에만 사용해야 함.
참고: 데이터를 제거하지 않음. 크레이트는 가져온 후에도 여전히 존재, 새 프로젝트에서 상자를 사용하는 것을 방해할 뿐.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- 정해진 버전의 상자를 꺼냄:

`cargo yank `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 꺼내는 실행 취소 (i.e. 다시 다운로드 허용):

`cargo yank --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo yank --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>
