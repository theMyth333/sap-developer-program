# SAP BTP Developer with CAP (Cloud Application Programming Model)

*A practical, project-based program to build, secure, test, and deploy enterprise applications on SAP Business Technology Platform.*

## Program Overview

### SAP BTP Development with CAPM

A 12-week training program designed to take freshers from programming fundamentals to building and deploying enterprise-grade applications using SAP Cloud Application Programming Model (CAPM).

Learn to develop cloud-native applications using **JavaScript, Node.js, CDS, OData, SAP HANA Cloud, SAP BTP, and SAP Fiori Elements**. Work through guided assignments, collaborative development, and a final capstone project based on real-world SAP business scenarios.

**Technology stack**

- SAP Business Technology Platform (BTP)
- SAP Cloud Application Programming Model (CAPM)
- JavaScript and Node.js
- CDS (Core Data Services)
- OData V4 and REST APIs
- SAP HANA Cloud and SQLite
- SAP Fiori Elements and SAPUI5 fundamentals
- SAP Cloud Identity Services and XSUAA concepts
- Git and GitHub
- SAP BTP Cloud Foundry
- Automated testing and CI/CD fundamentals

## Program at a Glance

| Attribute | Details |
|---|---|
| Recommended duration | 12 weeks |
| Training days | 5 days per week |
| Study time | 6 hours per day |
| Total learning hours | 360 hours |
| Learning approach | Concepts, coding, assignments, reviews, and projects |
| Primary development language | JavaScript / Node.js (TypeScript introduced) |
| Backend framework | SAP CAP with Node.js |
| Frontend framework | SAP UI5 with Fiori Elements |
| Deployment platform | SAP BTP, Cloud Foundry |
| Final outcome | Deployed CAP application with project documentation |
| Prerequisites | Basic programming logic. No prior SAP knowledge required |

## 1. Program Overview

### What this program is about

This program introduces freshers to enterprise application development using SAP BTP and CAPM. Learners progress from programming fundamentals to data modeling, service development, application security, user interface integration, testing, and cloud deployment.

The goal is not just to learn SAP terminology. Learners will develop applications, understand the architecture behind them, debug issues, and demonstrate working software.

### How the learning journey works

- **Project 1 — Guided project:** Build a basic business application with CRUD operations.
- **Project 2 — Collaborative project:** Develop a multi-user business application with authorization and Fiori Elements.
- **Project 3 — Capstone project:** Design, build, test, and deploy an end-to-end CAP application with mentor review.

### How learning time is allocated

- 20% — Concepts and instructor-led sessions
- 60% — Hands-on coding and technical exercises
- 15% — Project development and integration
- 5% — Code reviews, assessments, and technical discussions

### A typical six-hour training day

- Concepts and demonstrations — 1.5 hours
- Guided coding exercises — 2 hours
- Project development — 1.5 hours
- Code review and debugging — 0.5 hours
- Assignments and knowledge checks — 0.5 hours

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
- JavaScript essentials
- Node.js runtime and npm
- JSON and REST concepts
- TypeScript introduction

**You deliver:** BTP trial environment ready and a Node.js command-line mini app

### 02. Weeks 3–4: CAP Core: CDS Modeling and Services

- What is CAP and why it exists (opinionated, domain-driven, convention over configuration)
- CAP architecture: CDS, runtimes (Node.js and Java), SAP Cloud SDK
- Dev tools: SAP Business Application Studio, VS Code
- Project scaffolding 
- Domain modeling with CDS: entities, types, aspects, enums
- Associations and compositions
- Service definitions and projections
- Actions and functions
- Annotations 
- Initial data with CSV files
- Local development with SQLite
- Testing requests with REST Client and Postman

**You deliver:** Bookshop-style CAP service with a documented data model (Project 1, Part A)

### 03. Weeks 5–6: Custom Logic, OData and Integration

- OData V4 fundamentals
- CRUD handlers, Event Handlers
- Custom handlers in Node.js 
- Input validation and error handling
- Draft handling 
- Calling the database with CQL 
- Localization (i18n) and logging 
- Consuming external services, remote services, mocking
- Introduction to Cloud SDK (OData and HTTP clients)
- SAP Business Accelerator Hub and the API Business Hub
- Events and messaging 
- Intro to SAP Event Mesh / SAP Advanced Event Mesh

**You deliver:** CAP backend with custom logic and an external API integration (Project 1, Part B)

### 04. Weeks 7–8: User Interfaces with SAP Fiori

- SAP Fiori design principles and floorplans
- Fiori Elements: List Report and Object Page
- UI annotations with CDS 
- Value helps 
- Draft-enabled editing flows
- Fiori tools and the Application Generator
- Page Map and Guided Development
- Freestyle UI with SAPUI5: MVC, views, controllers, data binding
- XML views, routing, models (JSON, OData V4), formatters
- Custom controls and extension points in Fiori Elements
- SAPUI5 Controls and theming (SAP Horizon, UI Theme Designer)
- Fiori launchpad and app descriptors 
- Accessibility and responsive design basics

**You deliver:** Fiori Elements app and a small freestyle UI5 app on top of your CAP service (**Project 1**: guided CRUD application)

### 05. Weeks 8–9: Databases and SAP HANA Cloud

- Relational database concepts and SQL refresher
- SAP HANA Cloud overview and architecture
- SAP HANA Cloud provisioning on BTP and HDI containers
- Database-specific features: views, calculation views (awareness)
- CDS to SQL mapping, native HANA artifacts 
- Using SQLite locally and HANA in the cloud 
- Performance basics: indexes, query tuning, Explain Plan
- Data migration and seeding
- Introduction to PostgreSQL support on BTP (awareness)

**You deliver:** Database design with seed data, running on SAP HANA Cloud

### 06. Weeks 9–10: Authentication, Authorization and Security

- SAP BTP security landscape: identity providers, SAP Cloud Identity Services (IAS and IPS)
- OAuth 2.0 and JWT fundamentals
- XSUAA 
- Scopes, roles, role templates and role collections
- CAP authorization annotations
- Instance-based authorization 
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
- Multitarget Applications, MBT build tool
- Deploying to BTP Cloud Foundry 
- Service bindings 
- Destination service and Connectivity service
- SAP Build Work Zone: publishing apps to the launchpad site
- HTML5 Application Repository and the Managed Application Router
- Kyma runtime overview (awareness)
- Cloud Foundry vs Kyma vs ABAP environment (when to use which)
- Multitenancy (SaaS) overview using (awareness)
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

- Unit testing with Jest adn CDS Test
- Testing handlers, validations and authorization
- API tests with Postman and Newman
- UI5 testing: OPA5 and QUnit (awareness)
- Code linting with ESLint
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
| **Project 1 (Guided)** | In Progress  |
| **Project 2 (Team)** | In Progress  |
| **Project 3 (Capstone)** | In Progress |

---

## Tools and Environment

| Category | Tools |
|---|---|
| Cloud platform | SAP BTP Trial / Free Tier, Cloud Foundry environment |
| IDE | SAP Business Application Studio, VS Code |
| CAP tooling |  SAP Fiori tools, MBT, Cloud Foundry CLI |
| Databases | SQLite (local), SAP HANA Cloud (cloud) |
| API testing | Postman/Bruno, REST Client |
| Version control | Git, GitHub |
| Testing | Jest, ESLint |
| CI/CD | GitHub Actions |

---