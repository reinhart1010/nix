---
layout: page
title: linux/blkpr (English)
description: "Register, reserve, release, preempt, and clear persistent reservations on a block device that supports Persistent Reservations."
content_hash: 3afb2ddf4e4f6d0508a2ce8a1353ffb150d33769
last_modified_at: 2024-04-14
tldri18n_status: 2
---
# blkpr

Register, reserve, release, preempt, and clear persistent reservations on a block device that supports Persistent Reservations.
More information: <https://manned.org/blkpr>.

- Register ([c]ommand) a new reservation with a given [k]ey on a given device:

`blkpr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--command</span>` register --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reservation_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Set the [t]ype of an existing reservation to exclusive access:

`blkpr -c reserve -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reservation_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--type</span>` exclusive-access `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Preempt the existing reservation with a given [K]ey and replace it with a new reservation:

`blkpr -c preempt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-K|--oldkey</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key</span>` -t write-exclusive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Release a reservation with a given [k]ey and [t]ype on a given device:

`blkpr -c release --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reservation_key</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reservation_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>

- Clear all reservations from a given device:

`blkpr -c clear -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/device</span>
