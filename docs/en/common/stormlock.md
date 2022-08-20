---
layout: page
title: common/stormlock (English)
description: "Centralized locking system."
content_hash: 98985c6ae19914aa8cd98295d3f6bad664efe2f8
---
# Stormlock

Centralized locking system.
More information: <https://github.com/tmccombs/stormlock>.

- Acquire a lease for resource:

`stormlock acquire `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>

- Release the given lease for the given resource:

`stormlock release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lease_id</span>

- Show information on the current lease for a resource, if any:

`stormlock current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>

- Test if a lease for given resource is currently active:

`stormlock is-held `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lease_id</span>
