---
layout: page
title: common/czkawka-cli (한국어)
description: "중복 항목, 빈 폴더, 유사한 이미지 등을 찾는 다양한 기능의 앱 `czkawka`의 명령어 입력 버전."
content_hash: 0e5575e53f79c1f9d19877ecb57abc3031a7d925
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/czkawka-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/czkawka-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># czkawka-cli

중복 항목, 빈 폴더, 유사한 이미지 등을 찾는 다양한 기능의 앱 `czkawka`의 명령어 입력 버전.
더 많은 정보: <https://github.com/qarmin/czkawka>.

- 특정 디렉토리에 중복되거나 유사한 파일을 나열:

`czkawka-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dup|image</span>` --directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- 특정 디렉터리에서 중복 파일을 찾아 삭제 (기본값: `NONE`):

`czkawka-cli dup --directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>` --delete-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AEN|AEO|ON|OO|HARD|NONE</span>
