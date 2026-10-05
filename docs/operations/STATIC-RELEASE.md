# Static release from verified Git source

Engineering and sole execution owner: Codex. Semantic identity and visual acceptance: Yannick.

The existing Vercel project is `eya-autolive2d-demo` (`prj_Pm4WEFgcy4noLHWvQqdEyvXa5tvj`), in team `yjos-projects`. Its previously observed manual production deployment serves the original HTML; the corrected mobile HTML is already merged in the Git `master` branch. A deployment without commit metadata must not be reported as the current Git release.

`python3 scripts/build_static.py` packages only the current `workflow_demo.html` at `/` and `/workflow_demo.html`, plus the six images it references. It preserves all bytes and refuses an existing output directory. The `.stretch` file, source documentation, root screenshots and evidence are excluded from the static output. `.vercelignore` also limits uploaded input; no project identity or access protection changes are required.

Run `python3 -m unittest discover -s scripts -p 'test_*.py' -v` and the build in a clean checkout. The read-only CI publishes a hash manifest of all eight outputs. Four tests cover the real allowlist/bytes, determinism, existing release preservation and symlink rejection. No package installation, provider invocation or remote deployment occurs in these commands.

Before release, connect the existing Vercel project to `yj000018/eya-autolive2d-demo` with production branch `master`, or use its authenticated CLI path. Preserve the current project/domain/protection settings; do not create a competing project. Verify a preview against the CI output and its exact source SHA before promotion. Record the deployment ID/SHA, root and `/workflow_demo.html` responses, all six asset hashes and mobile layout. If access is unavailable, retain this prepared source release and report the gap.

Rollback: promote the prior deployment `dpl_gVqqGwPGbqxSygZiiN99ffv9Amyk` on the same existing project/domain; it remains unchanged. Source rollback is a normal Git revert of these packaging changes. Rigging/editor and human acceptance remain separate from this static demonstration release.

Upload allowlist follows the [official `.vercelignore` contract](https://vercel.com/docs/deployments/vercel-ignore); output packaging independently enforces the reviewed HTML/media boundary.
