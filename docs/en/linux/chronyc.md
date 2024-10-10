---
layout: page
title: linux/chronyc (English)
description: "Query the Chrony NTP daemon."
content_hash: d7bb93d354ad52ee0a494f59c5b6461b2e69cc0f
last_modified_at: 2024-10-10
tldri18n_status: 2
---
# chronyc

Query the Chrony NTP daemon.
More information: <https://chrony-project.org/doc/4.6.1/chronyc.html>.

- Start `chronyc` in interactive mode:

`chronyc`

- Display tracking stats for the Chrony daemon:

`chronyc tracking`

- Print the time sources that Chrony is currently using:

`chronyc sources`

- Display stats for sources currently used by chrony daemon as a time source:

`chronyc sourcestats`

- Step the system clock immediately, bypassing any slewing:

`chronyc makestep`

- Display verbose information about each NTP source:

`chronyc ntpdata`
