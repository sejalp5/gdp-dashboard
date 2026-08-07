# Data Initiatives Roadmap

Each initiative below is framed as a testable hypothesis using the format:

> **We believe that** [this Feature] **will result in** [this outcome] **for** [these users]. **We'll know we're successful when** [this measurable result].

## Overall Roadmap Outcome

**We believe that** executing this data initiatives roadmap — reliable on-time delivery, unified GCP source data, expanded stream integrations (Inventory EOP, Hours of Operations, OMNI/RFID/VIBE/CRAVE, Medallia, CB4), AI-assisted access, and governed, secure platform access — **will result in** a single, trusted, and timely source of truth that shifts the business from reactive firefighting to proactive, data-driven decision-making **for** store leaders, merchants, operations, WFM, CX, and analytics teams across all regions. **We'll know we're successful when** stakeholders consistently act on same-day data (100% of scheduled jobs/reports delivered by 8:00 AM PST), manual reconciliation and ad-hoc analyst requests drop by 25%+ as self-serve and integrated sources go live, and the platform operates under a single, secure, globally consistent permissions model with zero access-control incidents.

## Roadmap at a Glance

| Feature / Initiative | Priority | Owner |
|---|---|---|
| Meet all SLAs by 8am PST | High | Data Eng |
| GCP Sources — Sales, Traffic, Inv. | High | Data Eng |
| Inventory EOP | High | Data Eng |
| Hours of Operations | Medium | Data Eng |
| WFM – Success Metrics | Medium | WFM / BI |
| Medallia | Medium | CX / Data |
| Gamification | Medium | Product |
| OMNI, RFID, VIBE, CRAVE | High | Data Eng |
| AI Chatbot Integration | High | AI / Product |
| Peak Metrics in MI360 | Medium | Analytics |
| Cleanup the Distros | Low | Ops |
| Permissions – Global Equity Admin | High | Platform |
| CB4 Integration | Medium | Data Eng |

---

## High Priority

### Meet all SLAs by 8am PST
*Ensure all scheduled data jobs and reports complete and are delivered to stakeholders no later than 8:00 AM PST each day.*

**We believe that** meeting all SLAs by 8am PST **will result in** eliminated stakeholder frustration from delayed data and faster daily decision-making **for** store leaders and downstream stakeholders. **We'll know we're successful when** 100% of scheduled jobs and reports are delivered by 8:00 AM PST daily, with zero SLA breaches over a rolling 30-day period.

- **Priority:** High
- **Owner:** Data Eng

### GCP Sources — Sales, Traffic, Inv.
*Onboard and validate three new GCP data sources: Sales transactions, store Traffic, and Inventory feeds. Includes schema mapping, pipeline build, and DQ checks.*

**We believe that** onboarding the Sales, Traffic, and Inventory GCP sources **will result in** a single source of truth across the three most critical retail dimensions, reducing manual reconciliation **for** cross-functional analytics and BI teams. **We'll know we're successful when** all three sources are live in production with passing DQ checks and manual reconciliation effort is reduced by a measurable, agreed-upon percentage (e.g., 50%+).

- **Priority:** High
- **Owner:** Data Eng

### Inventory EOP
*End-of-Period inventory reporting module providing accurate stock snapshots at period close. Integrates with GCP Inventory source.*

**We believe that** the Inventory EOP reporting module **will result in** reliable period-close stock positions that reduce over-ordering, shrinkage blind spots, and markdown risk **for** merchants and operations teams. **We'll know we're successful when** EOP snapshots are published within an agreed SLA of period close (e.g., same-day) with stock-position accuracy variance under an agreed threshold (e.g., <2%).

- **Priority:** High
- **Owner:** Data Eng

### OMNI, RFID, VIBE, CRAVE
*Integrate four additional streams: Omnichannel (OMNI), RFID inventory tracking, VIBE, and CRAVE demand-sensing.*

**We believe that** integrating the OMNI, RFID, VIBE, and CRAVE data streams **will result in** a holistic operational picture spanning channels, inventory accuracy, people, and demand — enabling proactive rather than reactive decisions **for** business and operations leaders. **We'll know we're successful when** all four streams are onboarded and available in the platform, and at least one cross-stream (proactive) use case is in active use by the business.

- **Priority:** High
- **Owner:** Data Eng

### AI Chatbot Integration
*AI-powered chatbot enabling natural-language data queries, ad-hoc report generation, and guided analytics. Spans Q3 → Q4.*

**We believe that** the AI chatbot integration **will result in** democratized data access and reduced dependency on analysts for routine queries **for** non-technical business users. **We'll know we're successful when** the chatbot is adopted by a target share of business users (e.g., 30%+ of platform users querying it monthly) and analyst time spent on routine ad-hoc requests drops by a measurable percentage (e.g., 25%+).

- **Priority:** High
- **Owner:** AI / Product

### Permissions – Global Equity Admin
*Global equity-based admin permissions model ensuring consistent access controls across all regions and user roles.*

**We believe that** a global equity-based admin permissions model **will result in** consistent access controls and reduced data security exposure **for** all regional platform users and administrators. **We'll know we're successful when** 100% of regions operate on the unified permissions model with zero access-control-related security incidents post-rollout.

- **Priority:** High
- **Owner:** Platform

---

## Medium Priority

### Hours of Operations
*Surface store hours-of-operations data within the reporting platform to enable context-aware analysis of traffic and sales patterns.*

**We believe that** surfacing store hours-of-operations data **will result in** contextualized traffic and sales benchmarks and improved labor planning accuracy **for** regional and labor planning teams. **We'll know we're successful when** hours-of-operations data is integrated for 100% of stores and per-store benchmark distortion (open-hours-adjusted vs. raw) is measurably reduced in reporting.

- **Priority:** Medium
- **Owner:** Data Eng

### WFM – Success Metrics
*Workforce Management success metrics dashboard tracking scheduling efficiency, adherence, and labor cost KPIs.*

**We believe that** a WFM success metrics dashboard **will result in** faster identification of labor cost leakages and improved associate schedule satisfaction **for** WFM teams. **We'll know we're successful when** the dashboard is adopted as the primary WFM reporting tool and time-to-identify labor cost leakage drops by an agreed target (e.g., 20%+).

- **Priority:** Medium
- **Owner:** WFM / BI

### Medallia
*Integrate Medallia CX data into the platform, enabling correlation of customer feedback scores with operational metrics.*

**We believe that** integrating Medallia CX data **will result in** the ability to connect customer satisfaction signals to operational drivers (wait times, inventory, staffing) **for** CX and operations teams. **We'll know we're successful when** Medallia data is live in the platform, correlation reports are in regular use, and at least one targeted improvement tied to the correlation shows a measurable NPS gain.

- **Priority:** Medium
- **Owner:** CX / Data

### Gamification
*Gamification layer within team dashboards — leaderboards, achievement badges, and performance streaks — to drive engagement with metrics.*

**We believe that** a gamification layer (leaderboards, badges, streaks) **will result in** increased daily active usage of the analytics platform and a healthier performance culture **for** store and regional teams. **We'll know we're successful when** daily active usage of team dashboards increases by an agreed target (e.g., 25%+) after rollout.

- **Priority:** Medium
- **Owner:** Product

### Peak Metrics in MI360
*Surface peak-period performance metrics within the MI360 suite to support seasonal planning and in-season execution.*

**We believe that** surfacing peak-period metrics in MI360 **will result in** real-time peak performance visibility and more agile responses to volume surges **for** planning and operations teams. **We'll know we're successful when** peak metrics are live in MI360 ahead of the next peak season and are actively used during peak trading to inform in-season decisions.

- **Priority:** Medium
- **Owner:** Analytics

### CB4 Integration
*Integrate CB4 AI-driven task management and operational insights data into the reporting ecosystem.*

**We believe that** integrating CB4 AI-driven task data **will result in** field teams focusing on the highest-impact actions and improved task completion rates **for** store execution teams. **We'll know we're successful when** CB4 insights are live in the reporting ecosystem and store task completion rates improve by a measurable target (e.g., 10%+).

- **Priority:** Medium
- **Owner:** Data Eng

---

## Low Priority

### Cleanup the Distros
*Audit and remove stale, duplicate, or outdated report distribution lists. Establish ongoing distro governance process.*

**We believe that** auditing and cleaning up report distribution lists **will result in** reduced noise, improved report open rates, and lower compliance risk **for** report recipients and the business. **We'll know we're successful when** stale/duplicate distros are removed, a governance process is documented and adopted, and report open rates improve measurably post-cleanup.

- **Priority:** Low
- **Owner:** Ops
