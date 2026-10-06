# Current documentary state — EYA — AutoLive2D demo

Reviewed: 2026-10-01. Baseline commit: `35a8dd6a394948cc5227f6c5fcdf7283d8a6bd7a`. Execution owner for Wave A: Codex. Semantic/identity arbitration owner: Yannick.

## Verified at the audit boundary

- GitHub repository inventory, default branch and complete recursive tree read (no truncated tree).
- Root README/PROJECT/AGENTS and documentary map normalized against the committed YOS standard.
- Existing code, creative corpus, source evidence and paths retained.
- Observed workflow files: 0; presence does not prove successful CI.

## Limitations and next action

This demo is not the whole EYA project. EYA is distinct from EIA; no promotion to a new canonical EYA repository.

Builds, dependency compatibility, complete document-by-document semantic reconciliation, runtime, deployment and physical acceptance were not revalidated by this entrypoint audit. Review the affected module before implementation work. No new feature acceptance follows from metadata normalization.

## Resume

Read [PROJECT](../../PROJECT.md) and [documentation map](../README.md), then the observed payload paths in [architecture](../architecture/OVERVIEW.md). Record future durable decisions in [the ledger](../decisions/DECISION-LEDGER.md). Wave B/C is a separate migration scope requiring lineage and rollback evidence; this handoff does not authorize it.

## Technical follow-up — 2026-10-05

The retained native HTML and six image assets matched their acquisition baseline before this change. A mobile-only CSS addition fixes the table overflow observed at 390 px. Chromium checks at 320, 390, 768 and 1440 px load all six images, retain six workflow cards, and show no horizontal overflow or JavaScript error. Separate HTTP probes return the exact current source and asset bytes.

[Verification receipt](../../evidence/MOBILE-LAYOUT-2026-10-05.json) records source preservation, browser protocol and limitations. The baseline remains recoverable through the remote tag `archive/pre-mobile-layout-2026-10-05`. This is local static-demo validation; no hosted CI, rigging/editor acceptance or provider deployment is claimed. Engineering and execution owner: Codex.

## Existing-host release preparation — 2026-10-06

Fresh Vercel inspection finds the existing manual production deployment still serving the original HTML, without a Git SHA. The corrected mobile source is present on `master`. Four packaging-boundary tests pass locally; the new read-only CI checks the exact eight-file static output. [Release contract](../operations/STATIC-RELEASE.md). Existing Vercel project Git reconnection requires an authenticated native session: the browser currently reaches login. No duplicate project, promotion, protection change or rigging/publication acceptance is asserted.

## Verified existing-project Production release — 2026-10-06

The authenticated Vercel connector now supports pinned-Git deployment in the existing project, superseding the earlier native-login-only blocker for this release. Preview `dpl_4Hmop5GvmqGYhS2jzHPe5qETyR6q` was verified before the Production build `dpl_BV7hGXbVL2qwrzDtPmcLJ7FmvJzd`, both from source SHA `16b37f9c305d52100639fd7edfe9f15516803da8`. All eight public files match the source SHA256 manifest. At 390 px all six images/cards load without horizontal overflow. All three existing aliases now map to the verified release; protections and original rollback deployment remain unchanged. Docs/AGENTS/rigging paths return 404. [Production receipt](../../evidence/PRODUCTION-RELEASE-2026-10-06.json). No persistent Git connection, automatic future deployment or fresh rigging/editor acceptance is claimed.
