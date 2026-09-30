# Sanskrit Programming Repo Audit

Audit date: 2026-04-05

## Status Snapshot

- GitHub repo: `MontyCraig/sanskrit_programming`
- Remote last update: 2025-11-26
- Local checkout: `main` is ahead of `origin/main` by 1 commit
- Current shape: documentation-heavy research repo with prototype `.sam` source and test files, but no runnable compiler/runtime toolchain yet

## What Is In Good Shape

- The conceptual foundation is substantial: philosophy, specifications, roadmap material, and phase-based task planning are all present.
- The repo already has a strong `CLAUDE.md`, contribution guidance, and a coherent high-level structure for future language work.
- The new TDDaaS and CGaaS workflow files give the project a baseline CI posture instead of relying only on markdown linting.

## Current Gaps

- The implementation surface is still a prototype. `src/core/number.sam` and `tests/core/number_test.sam` are illustrative, but there is no parser, interpreter, compiler entrypoint, or executable validation path.
- Phase plans remain almost entirely open, which means roadmap documents are ahead of implementation reality.
- There was no repo-level test automation for repository contracts before this refresh, so CI confidence was low.

## Next Development Priorities

1. Define an executable MVP for the language.
   Decide what the first runnable milestone is: tokenizer, parser, interpreter, or transpiler. Without that boundary, the repo will keep accumulating concepts without a delivery path.

2. Build a real toolchain scaffold.
   Add a minimal CLI, parser skeleton, and fixture-based golden tests so `.sam` examples can be validated automatically.

3. Convert prototype examples into acceptance criteria.
   The current `number.sam` example and its paired test should become explicit language contracts that drive grammar and runtime implementation.

4. Tighten documentation around implementation order.
   Reduce ambiguity between visionary long-range goals and near-term milestones. The next public roadmap should show what can be built in weeks, not just in phases.

5. Expand repo automation once executable code exists.
   The next step after this refresh is to add real source-level linting, typed Python tooling for the compiler/runtime scaffold, and artifact publishing.

## Immediate Recommended Backlog

- Create `src/compiler/` or `src/interpreter/` with a minimal executable entrypoint.
- Write parser acceptance tests for literals, identifiers, and arithmetic expressions.
- Add one end-to-end example that proves the repo can execute or transpile a `.sam` file.
- Update the README once the first runnable milestone exists so the project is not presented as more complete than it is.
