---
layout: page
title: linux/setenforce (한국어)
description: "SELinux를 강제 모드와 허용 모드 사이에서 전환."
content_hash: a2302aaf9053296bbe63de5572bac6914e35b13e
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setenforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setenforce

SELinux를 강제 모드와 허용 모드 사이에서 전환.
SELinux를 활성화하거나 비활성화하려면 `/etc/selinux/config`를 편집하세요.
같이 보기: `getenforce`, `semanage-permissive`.
더 많은 정보: <https://manned.org/setenforce>.

- SELinux를 강제 모드로 설정:

`setenforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|Enforcing</span>

- SELinux를 허용 모드로 설정:

`setenforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|Permissive</span>
