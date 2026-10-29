---
title: Dock Watch — Bikeshare Dock Availability Tracker
category: Six Sigma Hackathon
year: "2026"
order: 1
summary: "A quality-control dashboard and REST API that tracks bikeshare dock availability, forecasts empty and full stations, and tells maintenance vans where to go — built in 24 hours."
tags: [Python, FastAPI, FMEA, Control Charts, Claude Code]
thumbnail: /static/images/thumbs/dockwatch-map.jpg
---

**Live dashboard:** [zoebishop16.github.io/hackathonapplejazz](https://zoebishop16.github.io/hackathonapplejazz/) · **Code:** [github.com/zoebishop16/hackathonapplejazz](https://github.com/zoebishop16/hackathonapplejazz)

## Project Overview

Built for the Cornell Six Sigma Hackathon (on-campus, 24-hour track) in response to the **Urban Systems: Bikeshare Fleets** prompt. At rush hour, a city bikeshare runs out of bikes in residential districts and out of open docks downtown, while maintenance vans are dispatched blind. Our team built **Dock Watch**, a tool for the network planner and the van crew lead that shows which stations are unusable, when and where; which dock counts are misleading because of broken docks; which stations will run empty or full in the next two hours; and which van should move bikes where.

The tool runs on synthetic data shaped like a real GBFS feed: 30 stations at real Boston locations across six neighborhoods, eight vans, and station polls every five minutes for three weeks, including the morning and evening commuter rush.

![Network Overview: stations empty, full, or out of service right now, and the top stations at risk](/static/images/dockwatch-overview.jpg)

## Quality Engineering Methods

Every number on the dashboard comes from one tested statistics module, and each function is checked against a hand-calculated known answer and a degenerate case.

- **FMEA:** six failure modes (station empty, station full, disabled docks, silent data feed, kiosk offline, slow van response) with Occurrence scored from observed rates, RPN = Severity × Occurrence × Detection, and an editable Pareto chart. Slow van response ranked highest (RPN 240).
- **X-bar control chart** of percent open docks in hourly subgroups across the three weeks, showing the full operating day and flagging blocks that break their usual weekly pattern.
- **p-chart** of the share of unusable stations per poll, with Phase I limits from a Tuesday baseline and Phase II monitoring on Thursday.
- **Effective capacity and misleading-fill flags:** fill is calculated against working docks only, so a station that "looks" half full but has broken docks is flagged.
- **Reliability and availability** (series, parallel, and MTBF / MTTR) from repair work orders, plus a repeat-offender report for stations needing frequent unplanned repairs.

![FMEA table and Pareto chart ranking failure modes by RPN](/static/images/dockwatch-analysis.jpg)

## Map and Dispatch

The map shows every station colored and shaped by fill level, the van fleet, and an hour-by-weekday heatmap that makes the rush-hour pattern visible. The Dispatch page forecasts bikes at each station 30 minutes to 2 hours ahead from historical averages, ranks stations by priority and impact, recommends pickup and drop-off moves, and only offers vans that are idle and have room.

![Map of Boston stations colored by fill level, with filters and the rush-hour heatmap](/static/images/dockwatch-map.jpg)

![Dispatch forecast ranking at-risk stations by priority and expected impact](/static/images/dockwatch-dispatch.jpg)

## My Contributions

Work was split evenly across the team. My focus was building and refining the software:

- Developed the dashboard and API through AI-assisted coding ("vibe coding") with Claude Code, translating the team's design document and statistical methods into working pages.
- Debugged the application, including the data pipeline, control-chart subgroups, and deployment.
- Edited and refined the website: page layout, plain-language wording, color system, and the Network Overview landing page.
- Deployed the dashboard to GitHub Pages and the FastAPI REST API to Posit Connect.
