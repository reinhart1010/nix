---
layout: page
title: linux/chronyc (English)
description: "Query the Chrony NTP daemon."
content_hash: 4bf37a53ad739bebd629b3a628b94a3aa7bd3e9e
last_modified_at: 2023-06-28
---
# chronyc

Query the Chrony NTP daemon.
More information: <https://chrony.tuxfamily.org/doc/4.0/chronyc.html>.

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
