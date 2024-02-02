---
layout: page
title: common/perl (English)
description: "The Perl 5 language interpreter."
content_hash: 9573f03238be8f44913aabadf15894698cddb249
last_modified_at: 2024-02-02
related_topics:
  - title: français version
    url: /fr/common/perl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# perl

The Perl 5 language interpreter.
More information: <https://www.perl.org>.

- Print lines from `stdin` [m/] matching regex1 and case insensitive [/i] regex2:

`perl -n -e 'print if m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex1</span>`/ and m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex2</span>`/i'`

- Say [-E] first match group, using a regexp, ignoring space in regex [/x]:

`perl -n -E 'say $1 if m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">before</span>` (  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_regex</span>`  ) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">after</span>`/x'`

- [-i]n-place, with backup, [s/] substitute all occurrence [/g] of regex with replacement:

`perl -i'.bak' -p -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replacement</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/files</span>

- Use perl's inline documentation, some pages also available via manual pages on Linux:

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`
