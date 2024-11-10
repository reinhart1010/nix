---
layout: page
title: linux/restorecon (한국어)
description: "SELinux 보안 컨텍스트를 파일/디렉토리의 지속적인 규칙에 따라 복원."
content_hash: cc2b13dd8be0396dc52cac8b26ee2a5bd9c6179f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/restorecon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# restorecon

SELinux 보안 컨텍스트를 파일/디렉토리의 지속적인 규칙에 따라 복원.
같이 보기: `semanage-fcontext`.
더 많은 정보: <https://manned.org/restorecon>.

- 파일 또는 디렉토리의 현재 보안 컨텍스트 보기:

`ls -dlZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일 또는 디렉토리의 보안 컨텍스트 복원:

`restorecon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 디렉토리의 보안 컨텍스트를 재귀적으로 복원하고 변경된 레이블 모두 표시:

`restorecon -R -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉토리의 보안 컨텍스트를 재귀적으로 복원하며, 모든 사용 가능한 스레드를 이용하고 진행 상황 표시:

`restorecon -R -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 적용하지 않고 변경될 레이블 미리 보기:

`restorecon -R -n -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
