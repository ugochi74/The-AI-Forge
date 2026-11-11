# Verification results

- Python demo: exit 0; CSV/JSON round trips, disjoint 320/80 split, batching, centroids and timing/memory reports saved.
- All 31 supplied Python tests passed.
- TypeScript demo via tsx: exit 0. The sandbox blocked tsx IPC; final execution used approved escalation. Python and TypeScript use different random generators, so their scores can differ.
- All five added Python exercises ran: seeded demo comparison; median checked against statistics.median; 200,000-row CSV stream; NumPy/pure-Python matrix-vector comparison; local AST scan.
- Stream peak: 48,225 bytes; full-load peak: 95,707,587 bytes on this run.
- NumPy matched the Python answers at sizes 4, 64 and 1024, and was faster at each measured size. These timings are specific to this run.
- AST counts cover only local files, not the complete upstream repository.
- Quiz: learner scored 2/2 (D, A).
- Source hashes verified; original course files unmodified.

See environment.txt and package-lock.json for dependency versions. npm dependencies are ignored in Git. The recorded final TypeScript report replaces the earlier failed direct-Node attempt.
