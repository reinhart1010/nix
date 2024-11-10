---
layout: page
title: linux/matchpathcon (한국어)
description: "경로의 지속적인 SELinux 보안 컨텍스트 설정을 조회합니다."
content_hash: fb393a497cfca85544d68a1af0a97258c892bdcd
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/matchpathcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# matchpathcon

경로의 지속적인 SELinux 보안 컨텍스트 설정을 조회합니다.
같이 보기: `semanage-fcontext`, `secon`, `chcon`, `restorecon`.
더 많은 정보: <https://manned.org/matchpathcon.8>.

- 절대 경로의 지속적인 보안 컨텍스트 설정 조회:

`matchpathcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>

- 특정 파일 유형에 대한 설정으로 조회 제한:

`matchpathcon -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file|dir|pipe|chr_file|blk_file|lnk_file|sock_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>

- 경로의 지속적인 보안 컨텍스트와 현재 보안 컨텍스트가 일치하는지 [v]확인:

`matchpathcon -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/파일</span>
