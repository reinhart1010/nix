---
layout: page
title: linux/audit2allow (한국어)
description: "SELinux 로컬 정책 모듈을 생성하여 로그에 기록된 거부된 작업 기반의 규칙을 허용합니다."
content_hash: b4495e33aab8ee7ea91de69af79f6e6bcffb77c2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/audit2allow.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/audit2allow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audit2allow

SELinux 로컬 정책 모듈을 생성하여 로그에 기록된 거부된 작업 기반의 규칙을 허용합니다.
참고: audit2allow 사용 시 주의가 필요하며, 생성된 정책을 적용하기 전에 항상 검토하세요. 과도한 접근을 허용할 수 있습니다.
더 많은 정보: <https://manned.org/audit2allow>.

- 거부된 모든 서비스에 대한 접근을 허용하는 로컬 정책 생성:

`sudo audit2allow --all -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_정책_이름</span>

- 감사 로그에서 특정 프로세스/서비스/명령에 대한 접근을 허용하는 로컬 정책 모듈 생성:

`sudo grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` /var/log/audit/audit.log | sudo audit2allow -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_정책_이름</span>

- 로컬 정책의 Type Enforcement (.te) 파일을 검사하고 검토:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_정책_이름</span>`.te`

- 로컬 정책 모듈 설치:

`sudo semodule -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_정책_이름</span>`.pp`
