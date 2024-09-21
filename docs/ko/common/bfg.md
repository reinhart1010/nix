---
layout: page
title: common/bfg (한국어)
description: "git-filter-branch와 같은 Git 기록에서 대용량 파일이나, 비밀번호를 제거."
content_hash: 63c59bf7275b245650643e371054b864e8edf2fd
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bfg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bfg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bfg

git-filter-branch와 같은 Git 기록에서 대용량 파일이나, 비밀번호를 제거.
참고: 저장소가 원격 장치에 연결되어 있으면, 강제로 푸시해야 함.
더 많은 정보: <https://rtyley.github.io/bfg-repo-cleaner/>.

- 민감한 데이터가 포함된 파일을 제거하되 최신 커밋은 그대로 유지:

`bfg --delete-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">민감한_데이터가_포함된_파일</span>

- 저장소 기록에서 찾을 수 있는 특정 파일에 언급된 모든 텍스트를 제거:

`bfg --replace-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>
