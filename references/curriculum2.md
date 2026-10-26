# SAP BTP Developer with CAP (Cloud Application Programming Model)

> **A 12-week program to build, secure and deploy enterprise cloud applications on SAP BTP**
>
> **Audience:** College students, fresh graduates and developers moving into the SAP ecosystem

Take learners from cloud and JavaScript fundamentals to a deployed, secured, full-stack SAP application. Learners build data models and services with CAP, create SAP Fiori user interfaces, connect to SAP HANA Cloud, and deploy to SAP BTP. They finish with three portfolio projects featuring real authentication, OData services, a database, tests and a live deployment.

**Key tags:** CAP (Node.js) · CDS · OData · SAP Fiori · SAP HANA Cloud · Cloud Foundry · XSUAA

[Enroll] · [Book a demo class]
*Fees and upcoming batch dates are shared in the demo class.*

---

## Program at a Glance

| Item | Detail |
|---|---|
| Recommended duration | **12 weeks** |
| Study time per day | **6 hours** |
| Training days per week | **5 days** |
| Total duration | **360 hours** |
| Primary language | JavaScript / Node.js (TypeScript introduced) |
| Optional track | CAP Java (awareness session) |
| Prerequisites | Basic programming logic. No prior SAP knowledge required |

**Quick navigation:** [Overview](#overview) · [Curriculum](#curriculum) · [Skills](#skills-you-will-have) · [Careers](#roles-you-can-apply-for) · [Assessment](#how-your-progress-is-judged) · [Outcomes](#what-you-will-be-able-to-do) · [Portfolio](#what-you-finish-with)

---

## Overview

### What this program is about

Build enterprise-grade cloud applications the SAP way. Learn the SAP Cloud Application Programming Model (CAP) end to end: model your domain with CDS, expose services with OData, build SAP Fiori interfaces, persist data in SAP HANA Cloud, secure the application and deploy it on SAP BTP.

### One project, start to finish

Learners work in one Git repository throughout. **Project 1** is guided, **Project 2** is built with a partner, and **Project 3** is the learner's own idea with mentor review, so the portfolio shows growing independence.

### How your time is spent

| Activity | Share |
|---|---|
| Concepts | 20% |
| Hands-on development | 65% |
| Reviews and projects | 15% |

### A typical 6-hour day

| Block | Time |
|---|---|
| Concept / instructor session | 1.5 h |
| Hands-on coding | 2.0 h |
| Project development | 1.5 h |
| AI-assisted development | 0.5 h |
| Review / assignment / discussion | 0.5 h |

---

## Curriculum

### 10 steps from basics to a deployed enterprise application

Each step ends with something learners can show.

### 01. Weeks 1–2: Foundations (Cloud, Web and JavaScript)

- What is cloud computing: IaaS, PaaS, SaaS
- SAP landscape overview: S/4HANA, SAP BTP, SAP Fiori, SAP Build
- Introduction to SAP BTP: global accounts, subaccounts, directories, entitlements, spaces
- BTP Trial account and Free Tier setup
- Git and GitHub basics
- JavaScript essentials: variables, functions, arrays, objects, ES6+, async/await, promises
- Node.js runtime and npm
- JSON and REST concepts
- TypeScript introduction

**You deliver:** BTP trial environment ready and a Node.js command-line mini app

### 02. Weeks 3–4: CAP Core: CDS Modeling and Services

- What is CAP and why it exists (opinionated, domain-driven, convention over configuration)
- CAP architecture: CDS, runtimes (Node.js and Java), SAP Cloud SDK
- Dev tools: SAP Business Application Studio, VS Code, `@sap/cds-dk`
- Project scaffolding with `cds init` and `cds add`
- Domain modeling with CDS: entities, types, aspects, enums
- Associations and compositions
- Managed aspects: `cuid`, `managed`, code lists (`sap.common`)
- Service definitions and projections
- Actions and functions
- Annotations (`@readonly`, `@mandatory`, `@assert`)
- Initial data with CSV files
- Local development with SQLite, `cds watch` and `cds deploy`
- Testing requests with REST Client and Postman

**You deliver:** Bookshop-style CAP service with a documented data model (Project 1, Part A)

### 03. Weeks 5–6: Custom Logic, OData and Integration

- OData V4 fundamentals: `$metadata`, `$filter`, `$select`, `$expand`, `$orderby`, `$top`, `$skip`, `$count`
- CRUD handlers: `before`, `on`, `after` event handlers
- Custom handlers in Node.js (`srv.on`, `req.error`, `req.reject`)
- Input validation and error handling
- Draft handling and `@odata.draft.enabled`
- Calling the database with CQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
- Transactions and the `cds.tx` API
- Localization (i18n) and logging (`cds.log`)
- Consuming external services: `cds import`, remote services, mocking
- Introduction to Cloud SDK (OData and HTTP clients)
- SAP Business Accelerator Hub and the API Business Hub
- Events and messaging (`emit`, event-driven design)
- Intro to SAP Event Mesh / SAP Advanced Event Mesh

**You deliver:** CAP backend with custom logic and an external API integration (Project 1, Part B)

### 04. Weeks 7–8: User Interfaces with SAP Fiori

- SAP Fiori design principles and floorplans
- Fiori Elements: List Report and Object Page
- UI annotations with CDS (`@UI.LineItem`, `@UI.SelectionFields`, `@UI.Facets`, `@UI.FieldGroup`)
- Value helps and `@Common.ValueList`
- Draft-enabled editing flows
- Fiori tools and the Application Generator
- Page Map and Guided Development
- Freestyle UI with SAPUI5: MVC, views, controllers, data binding
- XML views, routing, models (JSON, OData V4), formatters
- Custom controls and extension points in Fiori Elements
- SAPUI5 Controls and theming (SAP Horizon, UI Theme Designer)
- Fiori launchpad and app descriptors (`manifest.json`)
- Accessibility and responsive design basics

**You deliver:** Fiori Elements app and a small freestyle UI5 app on top of your CAP service (**Project 1**: guided CRUD application)

### 05. Weeks 8–9: Databases and SAP HANA Cloud

- Relational database concepts and SQL refresher
- SAP HANA Cloud overview and architecture
- SAP HANA Cloud provisioning on BTP and HDI containers
- Database-specific features: views, calculation views (awareness)
- CDS to SQL mapping, native HANA artifacts (`.hdbtable`, `.hdbview`)
- Using SQLite locally and HANA in the cloud (hybrid testing with `cds bind`)
- Performance basics: indexes, query tuning, Explain Plan
- Data migration and seeding
- Introduction to PostgreSQL support on BTP (awareness)

**You deliver:** Database design with seed data, running on SAP HANA Cloud

### 06. Weeks 9–10: Authentication, Authorization and Security

- SAP BTP security landscape: identity providers, SAP Cloud Identity Services (IAS and IPS)
- OAuth 2.0 and JWT fundamentals
- XSUAA and the `xs-security.json` file
- Scopes, roles, role templates and role collections
- CAP authorization annotations: `@requires`, `@restrict`
- Instance-based authorization (`@restrict` with `where`)
- Mock users for local development
- Testing secured services locally and in the cloud
- Application Router (approuter) basics
- CORS, CSRF, and the OWASP Top 10 overview
- Secrets and credentials handling, Credential Store (awareness)
- Personal data and privacy basics (GDPR awareness)

**You deliver:** Secured multi-role application with role-based access

### 07. Weeks 10–11: Deployment, MTA and BTP Services

- Cloud Foundry fundamentals: orgs, spaces, apps, services, buildpacks
- Cloud Foundry CLI (`cf`) commands
- Multitarget Applications (MTA): `mta.yaml`, MBT build tool
- Deploying to BTP Cloud Foundry (`cds add mta`, `mbt build`, `cf deploy`)
- Service bindings and `VCAP_SERVICES`
- Destination service and Connectivity service
- SAP Build Work Zone: publishing apps to the launchpad site
- HTML5 Application Repository and the Managed Application Router
- Kyma runtime overview (awareness)
- Cloud Foundry vs Kyma vs ABAP environment (when to use which)
- Multitenancy (SaaS) overview using `@sap/cds-mtxs` (awareness)
- Monitoring, logging and alerting: SAP Cloud Logging, Application Logging service, Cloud ALM (awareness)

**You deliver:** Fully deployed application in BTP and a Work Zone launchpad tile

### 08. Weeks 11–12: Team Project

- Planning with user stories and acceptance criteria
- Branching strategy, pull requests and code reviews
- Issue tracking and sprint basics
- Designing the domain model together
- Splitting work: data model, service logic, UI, security
- Integrating frontend and backend
- Daily stand-ups and demos

**You deliver:** Team application with roles and authentication (**Project 2**)

### 09. Week 12: Testing and Quality

- Unit testing with Jest and `@cap-js/cds-test` (`cds.test`)
- Testing handlers, validations and authorization
- API tests with Postman and Newman
- UI5 testing: OPA5 and QUnit (awareness)
- End-to-end testing with wdi5 or Playwright (awareness)
- Code linting with ESLint and `@sap/eslint-plugin-cds`
- Debugging in Business Application Studio and VS Code
- Code quality tools: SonarQube basics (awareness)

**You deliver:** Automated test suite with documented results

### 10. Weeks 12+: CI/CD, Extensibility, AI Tools and Capstone

- CI/CD concepts and SAP CI/CD service (awareness)
- GitHub Actions pipeline for build, test and deploy
- Extensibility concepts: key user, in-app and side-by-side extensions
- Clean Core principles and side-by-side extensions for S/4HANA
- Integration with SAP S/4HANA (OData consumption via Destination)
- Introduction to SAP Build (Process Automation, Apps) and where CAP fits
- Introduction to SAP AI Core and the Generative AI Hub (awareness)
- Using AI coding assistants responsibly (Joule for Developers, GitHub Copilot, Claude)
- Prompt engineering for CAP and CDS development
- Capstone build, documentation and demo

**You deliver:** Deployed capstone application (**Project 3**) and final presentation

---

## Skills You Will Have

Practical skills used on your own project, not just read about.

- JavaScript (ES6+), Node.js and TypeScript basics
- CDS data modeling and CQL
- CAP services, custom handlers and event-driven design
- OData V4 service design and consumption
- SAP Fiori Elements and SAPUI5 fundamentals
- SAP HANA Cloud and HDI containers
- XSUAA authentication, scopes, roles and authorization
- Application Router and Destination service
- Cloud Foundry, MTA build and deployment
- SAP Build Work Zone integration
- Consuming external and S/4HANA APIs
- Git, GitHub and pull request workflow
- Unit and API testing (Jest, Postman)
- CI/CD with GitHub Actions
- Prompt engineering for coding assistants
- Debugging and logging on SAP BTP

---

## Roles You Can Apply For

Job titles this curriculum prepares you for. They are examples, not a promise of placement.

| Role | What you do |
|---|---|
| **SAP BTP Developer** | Build and deploy cloud applications on SAP BTP |
| **SAP CAP Developer (Node.js)** | Build CDS models, services and business logic with CAP |
| **SAP Full-Stack Developer (CAP + Fiori)** | Deliver backend services and Fiori UIs together |
| **SAP Fiori / UI5 Developer** | Build Fiori Elements and freestyle SAPUI5 applications |
| **SAP Integration Developer (Associate)** | Connect SAP and non-SAP systems through APIs |
| **Associate Software Engineer (SAP)** | Entry-level roles in SAP product and services teams |
| **SAP S/4HANA Extension Developer** | Build side-by-side extensions following Clean Core |
| **SAP Application Support Engineer** | Debug, monitor and support cloud applications |

---

## How Your Progress Is Judged

Your work on the projects is what counts. Each area carries a share of the final result.

| Area | Weight |
|---|---|
| JavaScript, Node.js and cloud fundamentals | 10% |
| CAP: CDS modeling and services | 20% |
| SAP Fiori / UI5 | 15% |
| SAP HANA Cloud and databases | 10% |
| Authentication and security | 10% |
| Deployment (MTA, Cloud Foundry, Work Zone) | 10% |
| Testing and quality | 5% |
| Final project and presentation | 20% |
| **Total** | **100%** |

---

## What You Will Be Able To Do

- Explain the SAP BTP landscape, environments and account model
- Model business domains in CDS with entities, associations and aspects
- Design and expose OData V4 services with CAP
- Write custom handlers, validations and event-driven logic in Node.js
- Build SAP Fiori Elements applications using annotations
- Create basic freestyle SAPUI5 applications
- Persist data in SQLite locally and SAP HANA Cloud in the cloud
- Secure applications with XSUAA, roles and instance-based authorization
- Consume external and S/4HANA APIs through the Destination service
- Build MTA archives and deploy to SAP BTP Cloud Foundry
- Publish applications to an SAP Build Work Zone launchpad
- Write unit and API tests and automate them in a CI/CD pipeline
- Use Git, pull requests and code review in a team workflow
- Use AI coding assistants responsibly and review what they produce
- Explain design choices and demonstrate a live project

---

## What You Finish With

**Portfolio**

- Node.js command-line mini app
- Guided CAP + Fiori CRUD application (**Project 1**)
- Documented CDS data model and OData service
- Database design and seed data (SAP HANA Cloud)
- Team application with roles and authentication (**Project 2**)
- Secured application with XSUAA configuration
- Automated test suite
- Deployed capstone application on SAP BTP (**Project 3**)
- CI/CD pipeline configuration
- Project README and architecture diagram
- Final project presentation

---

## Suggested Project Ideas

| Project | Idea options |
|---|---|
| **Project 1 (Guided)** | Bookshop, Leave Request Manager, Product Catalog |
| **Project 2 (Team)** | Employee Onboarding Tracker, Purchase Request Approval, Helpdesk Ticketing |
| **Project 3 (Capstone)** | Inventory and Order Management with S/4HANA API integration, Sales Dashboard with role-based access, Travel Expense Management (inspired by SAP Fiori Travel sample) |

---

## Tools and Environment

| Category | Tools |
|---|---|
| Cloud platform | SAP BTP Trial / Free Tier, Cloud Foundry environment |
| IDE | SAP Business Application Studio, VS Code |
| CAP tooling | `@sap/cds-dk`, SAP Fiori tools, MBT, `cf` CLI |
| Databases | SQLite (local), SAP HANA Cloud (cloud) |
| API testing | Postman, REST Client |
| Version control | Git, GitHub |
| Testing | Jest, Newman, ESLint |
| CI/CD | GitHub Actions |

---

## Learning Resources (for trainers)

- SAP Help Portal: *Cloud Application Programming Model* (cap.cloud.sap)
- SAP Developer Center (developers.sap.com): tutorials and missions
- SAP Learning (learning.sap.com): learning journeys
- SAP Business Accelerator Hub (api.sap.com)
- SAPUI5 Demo Kit (ui5.sap.com)
- SAP Samples on GitHub: `cap-sample`, `cloud-cap-samples`, `cloud-cap-samples-java`

---

## Ready to Start Building?

Enroll to register your interest, or book a free demo class. Fees and batch dates are shared by our team.

[Enroll] · [Book a demo class]
