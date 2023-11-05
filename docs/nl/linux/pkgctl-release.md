---
layout: page
title: linux/pkgctl-release (Nederlands)
description: "Release stap om bouw artefacten te committen, taggen en uploaden."
content_hash: ebb24affaecfa1a278f17ff65b829c980970dd20
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/pkgctl-release.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl release

Release stap om bouw artefacten te committen, taggen en uploaden.
Meer informatie: <https://man.archlinux.org/man/pkgctl-release.1>.

- Release een bouw artefact:

`pkgctl release --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>
