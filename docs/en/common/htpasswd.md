---
layout: page
title: common/htpasswd (English)
description: "Create and manage htpasswd files to protect web server directories using basic authentication."
content_hash: 58ab11b15dd6f31b8041918676631939deb1e55f
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/htpasswd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htpasswd

Create and manage htpasswd files to protect web server directories using basic authentication.
More information: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

- Create/overwrite htpasswd file:

`htpasswd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Add user to htpasswd file or update existing user:

`htpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Add user to htpasswd file in batch mode without an interactive password prompt (for script usage):

`htpasswd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Delete user from htpasswd file:

`htpasswd -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Verify user password:

`htpasswd -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display a string with username (plain text) and password (md5):

`htpasswd -nbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
