---
layout: page
title: common/yadm-gitconfig (한국어)
description: "`git config`에 옵션을 전달하여 `yadm`으로 관리하는 저장소의 `.gitconfig`를 변경합니다."
content_hash: 5051ed590146d01e6a9ce90dcd003305f2b639ba
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yadm-gitconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yadm-gitconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yadm-gitconfig

`git config`에 옵션을 전달하여 `yadm`으로 관리하는 저장소의 `.gitconfig`를 변경합니다.
같이 보기: `git config`.
더 많은 정보: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- Git 구성 값을 업데이트하거나 설정:

`yadm gitconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키.내부키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- `yadm`의 Git 구성에서 값 가져오기:

`yadm gitconfig --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- `yadm`의 Git 구성에서 값 제거:

`yadm gitconfig --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- `yadm`의 Git 구성의 모든 값 나열:

`yadm gitconfig --list`
