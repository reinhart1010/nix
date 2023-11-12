---
layout: page
title: common/git-instaweb (English)
description: "Helper to launch a GitWeb server."
content_hash: 7b1f00eaf85d86322a6f51eac7aeeecb51e8b28f
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-instaweb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-instaweb.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-instaweb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git instaweb

Helper to launch a GitWeb server.
More information: <https://git-scm.com/docs/git-instaweb>.

- Launch a GitWeb server for the current Git repository:

`git instaweb --start`

- Listen only on localhost:

`git instaweb --start --local`

- Listen on a specific port:

`git instaweb --start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Use a specified HTTP daemon:

`git instaweb --start --httpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lighttpd|apache2|mongoose|plackup|webrick</span>

- Also auto-launch a web browser:

`git instaweb --start --browser`

- Stop the currently running GitWeb server:

`git instaweb --stop`

- Restart the currently running GitWeb server:

`git instaweb --restart`
