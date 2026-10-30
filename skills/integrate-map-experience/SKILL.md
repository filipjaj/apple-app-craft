---
name: integrate-map-experience
description: "Implement or refine MapKit search, geocoding, place details and app-to-Maps links. Use for geographic discovery and place interactions."
---

# Integrate Map Experience

## Goal

Let people find and identify the intended place with trustworthy map context and useful recovery.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Identify whether the task needs an address, point of interest, route or current location. Use only the permissions needed and preserve useful manual search without location access.

2. Choose the appropriate current geocoding/search API for the supported SDK. Cancel or discard obsolete results when queries change and disambiguate plausible matches. An address geocode is not automatically a richly identified point of interest.

3. Retain stable place identity where available and show supported native place details or app annotations consistently. Keep app-owned selection separate from map labels and respect dismissal or loading/error events.

4. Provide intentional links to Maps with the correct place or destination and an appropriate web alternative where supported. Do not silently turn an approximate geocode into a precise destination or invent missing place metadata.

5. Test denied location, ambiguous names, stale query completion, no results and missing details. Exercise place selection and external handoff with the supported map presentation, including accessible discovery of essential destinations.

## Verify the outcome

- The selected place matches the intended address or entity.
- Old results cannot replace a newer query.
- Permission denial and ambiguous matches have useful paths.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
