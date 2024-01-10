---
layout: page
title: common/perlbrew (English)
description: "Manage Perl installations in the home directory."
content_hash: ea84b2cc5d07c8e8cbb465004c3649e17b083846
last_modified_at: 2024-01-10
tldri18n_status: 2
---
# perlbrew

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
