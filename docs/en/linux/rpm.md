---
layout: page
title: linux/rpm (English)
description: "RPM Package Manager."
content_hash: 7f54a17edf85e6ad3821ec66fb3eebcda412a6a7
---
# rpm

RPM Package Manager.
More information: <https://rpm.org/>.

- Show version of httpd package:

`rpm --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd</span>

- List versions of all matching packages:

`rpm --query --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mariadb*</span>`'`

- Forcibly install a package regardless of currently installed versions:

`rpm --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name.rpm</span>` --force`

- Identify owner of a file and show version of the package:

`rpm --query --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/postfix/main.cf</span>

- List package-owned files:

`rpm --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel</span>

- Show scriptlets from an RPM file:

`rpm --query --package --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name.rpm</span>

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm --verify --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php-*</span>`'`

- Display the changelog of a specific package:

`rpm --query --changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
