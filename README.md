# EYA — AutoLive2D demo

AutoLive2D/Stretchy demonstration and rigging artifacts for EYA.

**Repository role:** `MANIFESTATION`. **Canonical object:** `YW-000414`.

This demo is not the whole EYA project. EYA is distinct from EIA; no promotion to a new canonical EYA repository.

## Start here

| Need | Entry |
|---|---|
| Identity and authority | [PROJECT.md](PROJECT.md) |
| Agent operating contract | [AGENTS.md](AGENTS.md) |
| Canon and document authority | [Documentation map](docs/README.md#canon) |
| Architecture | [Observed structure](docs/architecture/OVERVIEW.md) |
| Key decisions | [Decision ledger](docs/decisions/DECISION-LEDGER.md) |
| Current state | [CURRENT](docs/status/CURRENT.md) |
| Specifications | [Specs map](docs/README.md#specs) |
| Resume / handoff | [Resume map](docs/README.md#handoffs) |

## Validation

Check workflow_demo.html locally; inspect retained .stretch assets in the relevant tool. No root software build manifest is tracked.

Commands are pointers from tracked manifests or existing runbooks, not test results from this audit. Deployment and live acceptance require their own evidence.

The [mobile layout verification](evidence/MOBILE-LAYOUT-2026-10-05.json) records the October 5 static browser checks and preserves the native asset hashes.

The [static release contract](docs/operations/STATIC-RELEASE.md) prepares the current mobile-corrected demo at `/` and `/workflow_demo.html`, with six unchanged images. Read-only CI verifies the exact eight-file package; production promotion remains independently verified.
