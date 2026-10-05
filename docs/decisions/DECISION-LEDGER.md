# Durable decision ledger — EYA — AutoLive2D demo

## WA-2026-10-01 — Common documentary entry contract

Status: accepted for the user-authorized Wave A navigation/metadata scope.
Decision owner: Yannick (Wave A instruction). Engineering and sole execution owner: Codex.

Expose README, PROJECT, AGENTS, a documentary map, observed architecture and CURRENT while preserving existing payload paths and Git history. Use explicit repository roles from the YOS crosswalk. No semantic identity merge, physical consolidation, repo rename or archive is decided here.

Authority boundary: This demo is not the whole EYA project. EYA is distinct from EIA; no promotion to a new canonical EYA repository.

Rationale: humans and agents need the same clear entry without reconstructing authority from historical README or source transcripts.
Alternatives: forced directory migration or blanket canon promotion — outside this scope.
Consequences: existing domain documents retain their provenance and acceptance status; missing classes stay explicit.
Evidence: the baseline commit in [CURRENT](../status/CURRENT.md), the [YOS standard](https://github.com/yj000018/YOS/blob/main/00_META/GITHUB-REPOSITORY-ARCHITECTURE-STANDARD-v1.md), and the per-repository remote receipt in the YOS Wave A audit.
Rollback: revert the Wave A commit; do not reset or rewrite history.

## REL-2026-10-06 — Existing-project static release package

Accepted engineering implementation within the user-authorized deployment continuation. Sole execution owner: Codex. Preserve identity, native HTML/media, existing domain and protections; build only eight reviewed output files without replacing any existing release. Separate hosted CI, preview, production and rigging/human acceptance. [Contract and rollback](../operations/STATIC-RELEASE.md).
