---
layout: page
title: linux/rpm (English)
description: "RPM Package Manager."
content_hash: 4153997cfbc5e1a694d2bdd33b34096def5f4a70
---
# rpm

RPM Package Manager.
More information: <https://rpm.org/>.

- Show version of httpd package:

`rpm -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd</span>

- List versions of all matching packages:

`rpm -qa '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mariadb*</span>`'`

- Forcibly install a package regardless of currently installed versions:

`rpm -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name.rpm</span>` --force`

- Identify owner of a file and show version of the package:

`rpm -qf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/postfix/main.cf</span>

- List package-owned files:

`rpm -ql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel</span>

- Show scriptlets from an RPM file:

`rpm -qp --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name.rpm</span>

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm -Va '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php-*</span>`'`
