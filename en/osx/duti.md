---
layout: page
title: osx/duti (English)
description: "Set default applications for document types and URL schemes on macOS."
content_hash: cea4542d327327f231a306d12bac9159bc6df0e4
related_topics:
  - title: 中文 version
    url: /zh/osx/duti.html
    icon: bi bi-globe
---
# duti

Set default applications for document types and URL schemes on macOS.
More information: <https://github.com/moretension/duti>.

- Set Safari as the default handler for HTML documents:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Safari</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.html</span>` all`

- Set VLC as the default viewer for files with `.m4v` extensions:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.videolan.vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m4v</span>` viewer`

- Set Finder as the default handler for the ftp:// URL scheme:

`duti -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.Finder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp</span>

- Display information about the default application for a given extension:

`duti -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext</span>

- Display the default handler for a given UTI:

`duti -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>

- Display all handlers of a given UTI:

`duti -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uti</span>
