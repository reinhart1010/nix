---
layout: page
title: common/vboxmanage-registervm (한국어)
description: "가상 머신(VM) 등록."
content_hash: 4b495206280a934faeb3be32cd9a843dc057fed9
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/vboxmanage-registervm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vboxmanage-registervm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vboxmanage-registervm

가상 머신(VM) 등록.
더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>.

- 기존 VM 등록:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.vbox</span>

- VM의 암호화 비밀번호 파일 제공:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.vbox</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>

- 명령줄에서 암호화 비밀번호 입력 요청:

`VBoxManage registervm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.vbox</span>` --password -`
