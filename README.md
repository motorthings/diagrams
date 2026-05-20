# IS AI Diagrams

Interactive HTML diagrams for AI strategy, architecture, and project planning.

Browse all diagrams: **https://charlie-fuller.github.io/diagrams/**

## Diagrams by Area

### Hire to Retire
| Diagram | Description |
|---------|-------------|
| [Index](hire-to-retire/index.html) | Hire-to-retire landing page |
| [Full Process Map](hire-to-retire/full-map.html) | End-to-end hire-to-retire process map |
| [Process Maps](hire-to-retire/process-maps.html) | Detailed process maps by stage |
| [Problem Map](hire-to-retire/problem-map.html) | Problem identification and mapping |
| [Workshop and Review Flags](hire-to-retire/flags.html) | Flags identified during workshop and review sessions |
| [JD Generator](hire-to-retire/jd-generator.html) | Job description generator flow |

### Procurement
| Diagram | Description |
|---------|-------------|
| [Process Map](procurement/process-map.html) | Procurement contracts process map |
| [AI Implementation Roadmap](procurement/ai-strategy.html) | AI implementation roadmap for procurement workflows |
| [ITFA Agent](procurement/itfa-agent.html) | IT/Finance approval agent flow |

### Deal Desk
| Diagram | Description |
|---------|-------------|
| [Process Maps](deal-desk/process-map.html) | Deal desk process maps |
| [Glean Actions Architecture](deal-desk/glean-actions-architecture.html) | Hybrid probabilistic/deterministic architecture for deal desk workflows |
| [Infrastructure Path](deal-desk/infrastructure-path.html) | Phased deployment plan: local validation, temp demo, Contentful sandbox (G07) |

### Strategic Account Planning
| Diagram | Description |
|---------|-------------|
| [To-Be Process Map](strategic-account-planning/process-map.html) | Target-state strategic account planning process |
| [Process Map with Data Mapping](strategic-account-planning/process-map-with-data.html) | Process map with data flow and system mapping |

### AI Platform
| Diagram | Description |
|---------|-------------|
| [Decision Tree v3.0](ai-platform/decision-tree.html) | AI platform selection decision tree |

### AESOP
| Diagram | Description |
|---------|-------------|
| [Hydra Process Map](aesop/hydra-process-map.html) | Process map for the Hydra adversarial evaluation swarm |

### Agent Factory
| Diagram | Description |
|---------|-------------|
| [Decision Flow](agent-factory/decision-flow.html) | Agent Factory decision flow diagram |

## G&A AI Initiative Dashboard

**[ga-ai/index.html](ga-ai/index.html)** -- Sortable table + kanban board for all G&A AI initiatives across Finance, Legal, People, and IS.

- **Data source**: PocketBase API at `ga-ai-dashboard.fly.dev` (Fly.io)
- **Collection**: `initiatives` -- fields: department, smt, kpi, initiative, impact, effort, strategic, score, status, jira_epic, notes, source_meeting
- **Kanban columns**: Backlog, On Deck, In Progress, In Beta, Done
- **JIRA link**: Cards with a `jira_epic` value link to `contentful.atlassian.net/browse/{key}`
- **Scores**: Composite of impact (1-5), effort (1-5 inverted), and strategic alignment (1-10)

## Adding Diagrams

Drop self-contained HTML files into the appropriate project folder (or create a new one). Update `index.html` with the new entry. All diagrams are single-file, self-contained HTML with no external dependencies beyond Google Fonts CDN.
