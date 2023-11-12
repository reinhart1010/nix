---
layout: page
title: linux/rpm (English)
description: "RPM Package Manager."
content_hash: 27f164893329445be3113d214bb2034081f3efdc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rpm

RPM Package Manager.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://rpm.org/>.

- Show version of httpd package:

`rpm --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd</span>

- List versions of all matching packages:

`rpm --query --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mariadb*</span>`'`

- Forcibly install a package regardless of currently installed versions:

`rpm --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.rpm</span>` --force`

- Identify owner of a file and show version of the package:

`rpm --query --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/postfix/main.cf</span>

- List package-owned files:

`rpm --query --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kernel</span>

- Show scriptlets from an RPM file:

`rpm --query --package --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package.rpm</span>

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm --verify --all '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php-*</span>`'`

- Display the changelog of a specific package:

`rpm --query --changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
