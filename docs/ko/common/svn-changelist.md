---
layout: page
title: common/svn-changelist (한국어)
description: "파일 세트에 변경 목록을 연결."
content_hash: f0ba4c97122bdcfc84237398612f4eaadd4b4099
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/svn-changelist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/svn-changelist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svn changelist

파일 세트에 변경 목록을 연결.
더 많은 정보: <https://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>.

- 파일을 변경 목록에 추가하며, 변경 목록이 존재하지 않을 경우 생성:

`svn changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변경목록_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 파일을 변경 목록에서 제거:

`svn changelist --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 전체 변경 목록을 한 번에 제거:

`svn changelist --remove --recursive --changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변경목록_이름</span>` .`

- 공백으로 구분된 디렉토리 목록의 내용을 변경 목록에 추가:

`svn changelist --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변경목록_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 변경 목록 커밋:

`svn commit --changelist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변경목록_이름</span>
