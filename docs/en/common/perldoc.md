---
layout: page
title: common/perldoc (English)
description: "Look up Perl documentation in `.pod` format."
content_hash: b9f1d2fbade7e7507c4265fef7cae266a68d4c90
last_modified_at: 2024-01-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/perldoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># perldoc

Look up Perl documentation in `.pod` format.
More information: <https://perldoc.perl.org/perldoc>.

- View documentation for a builtin [f]unction, a [v]ariable or an [a]PI:

`perldoc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|v|a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Search in the the question headings of Perl FAQ:

`perldoc -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>

- Send output directly to `stdout` (by default, it is send to a pager):

`perldoc -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page|module|program|URL</span>

- Specify the language code of the desired translation:

`perldoc -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language_code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page|module|program|URL</span>
