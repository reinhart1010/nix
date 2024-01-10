---
layout: page
title: common/perldoc (English)
description: "Look up Perl documentation in `.pod` format."
content_hash: b9f1d2fbade7e7507c4265fef7cae266a68d4c90
last_modified_at: 2024-01-10
tldri18n_status: 2
---
# perldoc

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
