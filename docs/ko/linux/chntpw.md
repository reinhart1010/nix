---
layout: page
title: linux/chntpw (한국어)
description: "Windows 레지스트리를 편집하고, 사용자 암호를 재설정하며, 사용자를 관리자로 승격할 수 있는 도구입니다. Windows SAM을 수정하여 동작합니다."
content_hash: 5d13686d8e07d27754f4ba24a59bb306d5630d77
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/chntpw.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chntpw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chntpw

Windows 레지스트리를 편집하고, 사용자 암호를 재설정하며, 사용자를 관리자로 승격할 수 있는 도구입니다. Windows SAM을 수정하여 동작합니다.
Kali Linux와 같은 라이브 CD로 대상 머신을 부팅하고, 권한 상승 후 실행하십시오.
더 많은 정보: <https://pogostick.net/~pnh/ntpasswd>.

- SAM 파일에 있는 모든 사용자 나열:

`chntpw -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sam_파일</span>

- 사용자와 대화형으로 편집:

`chntpw -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sam_파일</span>

- chntpw를 대화형으로 사용:

`chntpw -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sam_파일</span>
