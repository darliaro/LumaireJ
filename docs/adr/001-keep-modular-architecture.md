# ADR-001: Keep Modular Architecture for MVP

## Status
**Accepted** - 2026-01-17

## Context

The LumaireJ project currently has a modular folder structure designed for scalability:

```
app/
├── core/          # config, database
├── dependencies/  # session injection
├── models/        # SQLModel definitions
├── schemas/       # Pydantic validation
├── crud/          # database operations
├── api/v1/        # endpoint routers
├── constants.py   # validation limits
└── main.py
```

With only 1 POST endpoint currently implemented, the question arose whether this structure is over-engineered for the current MVP scope.

## Decision

**Keep the current modular architecture.**

## Rationale

### Planned Features Support Current Structure

Per the README roadmap, the following features are planned:
- View, edit, and delete journal entries (GET, PATCH, DELETE endpoints)
- Visualization of emotional trends
- Potential Telegram bot integration

These features will require:
- Additional CRUD operations → `crud/` folder will grow
- More API endpoints → `api/v1/endpoints/` will have more routers
- Possibly more models → `models/` folder justified
- Additional schemas (JournalUpdate, etc.) → `schemas/` folder justified

### Benefits of Current Structure

1. **Separation of Concerns** - Each layer has a single responsibility
2. **Testability** - Easy to mock dependencies and test in isolation
3. **Scalability** - Adding new features doesn't require restructuring
4. **Onboarding** - Standard FastAPI patterns familiar to new contributors
5. **CI/CD Ready** - Structure supports incremental testing and deployment

### Considered Alternatives

| Alternative | Pros | Cons |
|-------------|------|------|
| Flatten to single files | Simpler for current state | Requires restructuring when growing |
| Partial simplification | Removes unused abstractions | Still requires future changes |
| Keep as-is (chosen) | Ready for growth | Slight overhead for current MVP |

## Consequences

### Positive
- No refactoring needed when adding planned features
- Consistent architecture throughout project lifecycle
- Clear patterns for contributors to follow

### Negative
- Some abstraction layers (e.g., `crud/`) currently contain minimal code
- New contributors may question the structure given current feature set

### Mitigations
- Document architecture decisions (this ADR)
- Add inline comments explaining the purpose of each layer
- Reference planned features in code comments where appropriate

## References
- Issue #53: Evaluate and simplify architecture for MVP scope
- README.md: Features (MVP) section
