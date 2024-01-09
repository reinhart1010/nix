---
layout: page
title: common/perlbrew (English)
description: "Manage Perl installations in the home directory."
content_hash: ea84b2cc5d07c8e8cbb465004c3649e17b083846
last_modified_at: 2024-01-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/perlbrew.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># perlbrew

Manage Perl installations in the home directory.
See also: `asdf`.
More information: <https://github.com/gugod/App-perlbrew>.

- Initialize a `perlbrew` environment:

`perlbrew init`

- List available Perl versions:

`perlbrew available`

- Install/uninstall a Perl version:

`perlbrew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- List perl installations:

`perlbrew list`

- Switch to an installation and set it as default:

`perlbrew switch perl-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Use the system Perl again:

`perlbrew off`

- List installed CPAN modules for the installation in use:

`perlbrew list-modules`

- Clone CPAN modules from one installation to another:

`perlbrew clone-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_installation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_installation</span>
