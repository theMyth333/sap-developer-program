## Curriculum

### 12 steps from basics to a deployed enterprise application

Each step ends with something learners can show.

### 01. Weeks 1–2: Programming Fundamentals and Developer Workflow

- How software works: programs, compilers, interpreters, runtimes
- Programming logic: variables, data types, operators, conditions, loops
- Functions, arrays and objects (problem-solving practice)
- Reading error messages and basic debugging
- Command line / terminal basics
- VS Code setup and productivity tips
- Git and GitHub basics: repositories, commits, branches, push and pull
- Professional skills: asking good questions, reading documentation, daily stand-up habits

**You deliver:** A GitHub repository with logic-building exercises and a clean commit history

### 02. Weeks 3–4: JavaScript Essentials and Web Basics

- JavaScript fundamentals: ES6+ syntax, scope, closures, array methods
- Objects, classes and modules
- Asynchronous JavaScript: callbacks, Promises, async/await
- Error handling with try/catch
- JSON and working with data
- HTML and CSS basics
- DOM basics and browser DevTools
- How the web works: HTTP, requests and responses, client vs server

**You deliver:** A small interactive web page that consumes data from a public API

### 03. Weeks 5–6: Node.js, REST, Cloud and SAP BTP Foundations

- Node.js runtime, npm and package management
- Building a simple REST API with Node.js (Express basics)
- REST concepts, status codes and testing with Postman / Bruno
- TypeScript introduction
- What is cloud computing: IaaS, PaaS, SaaS
- SAP landscape overview: S/4HANA, SAP BTP, SAP Fiori, SAP Build
- Introduction to SAP BTP: global accounts, subaccounts, directories, entitlements, spaces
- BTP Trial account and Free Tier setup
- SQL refresher: tables, queries, joins, constraints

**You deliver:** BTP trial environment ready, a Node.js command-line mini app and a simple REST API

### 04. Weeks 7–8: CAP Core: CDS Modeling and Services

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

### 05. Weeks 9–10: Custom Logic, OData and Integration

- OData V4 fundamentals
- CRUD handlers and event handlers
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

### 06. Weeks 11–12: User Interfaces with SAP Fiori

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
- SAPUI5 controls and theming (SAP Horizon, UI Theme Designer)
- Fiori launchpad and app descriptors
- Accessibility and responsive design basics
- Mid-program review: Project 1 demo, code walkthrough and knowledge assessment

**You deliver:** Fiori Elements app and a small freestyle UI5 app on top of your CAP service (**Project 1**: guided CRUD application)

### 07. Weeks 13–14: Databases and SAP HANA Cloud

- Relational database concepts and advanced SQL
- SAP HANA Cloud overview and architecture
- SAP HANA Cloud provisioning on BTP and HDI containers
- Database-specific features: views, calculation views (awareness)
- CDS to SQL mapping, native HANA artifacts
- Using SQLite locally and HANA in the cloud
- Performance basics: indexes, query tuning, Explain Plan
- Data migration and seeding
- Introduction to PostgreSQL support on BTP (awareness)

**You deliver:** Database design with seed data, running on SAP HANA Cloud

### 08. Weeks 15–16: Authentication, Authorization and Security

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

### 09. Weeks 17–18: Deployment, MTA and BTP Services

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
- Multitenancy (SaaS) overview (awareness)
- Monitoring, logging and alerting: SAP Cloud Logging, Application Logging service, Cloud ALM (awareness)

**You deliver:** Fully deployed application in BTP and a Work Zone launchpad tile

### 10. Weeks 19–20: Team Project

- Planning with user stories and acceptance criteria
- Branching strategy, pull requests and code reviews
- Issue tracking and sprint basics
- Designing the domain model together
- Splitting work: data model, service logic, UI, security
- Integrating frontend and backend
- Daily stand-ups, sprint reviews and demos
- Team communication and giving or receiving feedback

**You deliver:** Team application with roles and authentication (**Project 2**)

### 11. Weeks 21–22: Testing, CI/CD, Extensibility and AI Tools

- Unit testing with Jest and CDS Test
- Testing handlers, validations and authorization
- API tests with Postman and Newman
- UI5 testing: OPA5 and QUnit (awareness)
- Code linting with ESLint
- Debugging in Business Application Studio and VS Code
- Code quality tools: SonarQube basics (awareness)
- CI/CD concepts and SAP CI/CD service (awareness)
- GitHub Actions pipeline for build, test and deploy
- Extensibility concepts: key user, in-app and side-by-side extensions
- Clean Core principles and side-by-side extensions for S/4HANA
- Integration with SAP S/4HANA (OData consumption via Destination)
- Introduction to SAP Build (Process Automation, Apps) and where CAP fits
- Introduction to SAP AI Core and the Generative AI Hub (awareness)
- Using AI coding assistants responsibly (Joule for Developers, GitHub Copilot, Claude)
- Prompt engineering for CAP and CDS development
- Capstone planning: scope, architecture and mentor approval

**You deliver:** Automated test suite with documented results, a working CI/CD pipeline and an approved capstone plan

### 12. Weeks 23–24: Capstone Project

- Capstone build: data model, services, UI, security
- Integration, testing and deployment to SAP BTP
- Documentation: README and architecture diagram
- Mentor code review and refinement
- Final demo preparation and presentation practice
- Interview preparation and portfolio review

**You deliver:** Deployed capstone application (**Project 3**) and final presentation
