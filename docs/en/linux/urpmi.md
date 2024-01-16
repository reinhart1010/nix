---
layout: page
title: linux/urpmi (English)
description: "Install packages in Mageia."
content_hash: fa0d4eabbc1a49461f94c092621d4ff9b8fc9ce7
last_modified_at: 2024-01-16
tldri18n_status: 2
---
# urpmi

Install packages in Mageia.
See also: `urpm.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
More information: <https://wiki.mageia.org/en/URPMI#urpmi>.

- Install a package from the repository or from a local RPM file:

`sudo urpmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package|path/to/file.rpm</span>

- Download a package without installing it:

`urpmi --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update all installed packages (run `urpmi.update -a` to get the available updates):

`sudo urpmi --auto-select`

- Update a package of one or more machines on the network according to `/etc/urpmi/parallel.cfg`:

`sudo urpmi --parallel local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Mark all orphaned packages as manually installed:

`sudo urpmi $(urpmq --auto-orphans -f)`
