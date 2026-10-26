# SAP BTP Developer Training for Freshers — CAPM

*A practical, project-based program to build, secure, test, and deploy enterprise applications on SAP Business Technology Platform.*

## Program Overview

### SAP BTP Development with CAPM

A 14-week training program designed to take freshers from programming fundamentals to building and deploying enterprise-grade applications using SAP Cloud Application Programming Model (CAPM).

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
| Recommended duration | 14 weeks |
| Training days | 5 days per week |
| Study time | 6 hours per day |
| Total learning hours | 420 hours |
| Learning approach | Concepts, coding, assignments, reviews, and projects |
| Primary development language | JavaScript |
| Backend framework | SAP CAP with Node.js |
| Deployment platform | SAP BTP, Cloud Foundry |
| Final outcome | Deployed CAP application with project documentation |

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

## 2. Curriculum — 10 Steps from Fundamentals to Deployment

Each module includes hands-on exercises and a tangible deliverable.

### Step 1: Programming Foundations and Developer Tools

**Suggested duration:** Week 1

**Topics covered**

- Introduction to software development and enterprise applications
- Understanding client-server architecture
- Programming fundamentals: variables, data types, operators, and expressions
- Conditional statements, loops, and functions
- Arrays, objects, and basic data structures
- Introduction to JavaScript and ES6+
- Error handling and debugging fundamentals
- Introduction to Visual Studio Code
- Terminal and command-line fundamentals
- Git and GitHub: repositories, commits, branches, and pull requests
- Introduction to JSON and HTTP concepts

**Hands-on exercises**

- Build small JavaScript programs.
- Manipulate arrays and objects representing business data.
- Read and write JSON data.
- Create a Git repository and push code to GitHub.

**You deliver:** A collection of JavaScript exercises and a GitHub repository containing your first programs.

### Step 2: JavaScript, Node.js, and Asynchronous Programming

**Suggested duration:** Week 2

**Topics covered**

- JavaScript functions, scope, and modules
- Object-oriented JavaScript fundamentals
- Array methods: `map`, `filter`, `find`, and `reduce`
- Destructuring, spread syntax, and template literals
- Promises, `async`, and `await`
- Asynchronous programming and error handling
- Node.js runtime and npm
- Package management and `package.json`
- Environment variables and configuration
- Basic file operations and JSON processing
- Introduction to HTTP clients and API calls

**Hands-on exercises**

- Develop reusable JavaScript modules.
- Process employee, supplier, and sales data.
- Consume a public REST API.
- Build a small Node.js command-line application.

**You deliver:** A modular Node.js application with asynchronous data processing and error handling.

### Step 3: SAP BTP Fundamentals and CAPM Introduction

**Suggested duration:** Week 3

**Topics covered**

- Introduction to SAP BTP and cloud-native development
- SAP BTP global accounts, directories, and subaccounts
- Understanding entitlements, quotas, and service instances
- SAP BTP environments: Cloud Foundry and Kyma overview
- Applications, services, destinations, and connectivity concepts
- Introduction to SAP Cloud Application Programming Model
- CAP architecture: models, services, and runtime
- CAP Node.js versus CAP Java overview
- Installing and using the CDS development kit
- Creating a CAP project using the command line
- Project structure and configuration files
- Running a CAP application locally
- Introduction to the SAP Business Application Studio or compatible local development tools

**Hands-on exercises**

- Set up the development environment.
- Create a CAP project using `cds init`.
- Run the application locally using `cds watch`.
- Explore the generated project structure and service endpoints.

**You deliver:** A working CAP project running locally, with a clear understanding of its architecture.

### Step 4: CDS Modeling and Data Persistence

**Suggested duration:** Weeks 4–5

**Topics covered**

- Introduction to CDS (Core Data Services)
- Defining entities, elements, keys, and data types
- Namespaces and reusable types
- Associations and compositions
- Managed and unmanaged relationships
- Annotations and their purpose
- Modeling master data and transactional data
- Referential integrity and relationship design
- Data constraints and validation concepts
- CSV-based initial data and test data
- SQLite for local development
- SAP HANA Cloud fundamentals
- Database deployment and schema generation
- Database configuration and persistence
- Introduction to migrations and data evolution

**Hands-on exercises**

- Model employees, departments, suppliers, and purchase orders.
- Create associations and compositions.
- Load sample data using CSV files.
- Run database queries and inspect generated schemas.
- Test persistence using SQLite locally.

**You deliver:** A business domain model with relationships, sample data, and a working persistence layer.

### Step 5: CAP Services, OData V4, and Business Logic

**Suggested duration:** Weeks 6–7

**Topics covered**

- Defining service projections using CDS
- Exposing entities through service definitions
- Understanding OData V4
- CRUD operations and HTTP methods
- OData metadata and entity sets
- Query options: `$select`, `$filter`, `$expand`, `$orderby`, and `$top`
- CAP generic providers and generated CRUD operations
- Custom actions and functions
- Service handlers in Node.js
- CAP request lifecycle and event handlers
- `before`, `on`, and `after` handlers
- Input validation and business rules
- Transactions and error handling
- Associations and deep operations
- Draft-enabled services: concepts and introduction
- API testing with Postman or equivalent tools
- Reading application logs and debugging service handlers

**Hands-on exercises**

- Expose a business entity through an OData service.
- Implement custom validation and business logic.
- Create an action for submitting a purchase order.
- Test CRUD operations and query options.
- Return meaningful errors for invalid business requests.

**You deliver:** A documented CAP OData service with CRUD operations, custom business logic, and validation.

### Step 6: SAP Fiori Elements and UI Integration

**Suggested duration:** Week 8

**Topics covered**

- Introduction to SAP Fiori and SAP Fiori Elements
- Understanding metadata-driven user interfaces
- OData service consumption
- UI annotations and their purpose
- List Report and Object Page
- Tables, forms, filters, and actions
- Search, sorting, and filtering
- Value help and selection fields
- Field groups and facets
- Basic navigation between application pages
- UI adaptation and extension concepts
- Introduction to SAPUI5 and custom UI development
- Connecting a CAP service to a generated application
- Troubleshooting metadata and UI annotation issues

**Hands-on exercises**

- Generate a Fiori Elements application from a CAP service.
- Configure List Report and Object Page layouts.
- Add filters, value help, and action buttons.
- Test create, edit, and display operations from the UI.

**You deliver:** A functional business application with a Fiori Elements interface connected to CAP services.

### Step 7: Security, Authentication, and Authorization

**Suggested duration:** Week 9

**Topics covered**

- Authentication versus authorization
- Identity and access management fundamentals
- SAP Cloud Identity Services overview
- XSUAA and application security concepts
- Role collections and role templates
- Defining roles and restricting service access
- Role-based access control in CAP
- Restricting entity and operation access
- User context and authenticated requests
- Securing service endpoints
- Destination-based authentication concepts
- Secrets and environment configuration
- Common security misconfigurations
- Secure error handling and sensitive data protection

**Hands-on exercises**

- Configure authentication for a deployed CAP application.
- Define business roles such as employee, manager, and administrator.
- Restrict selected operations based on roles.
- Test access with different users and permissions.

**You deliver:** A secured business application with role-based authorization and documented access rules.

### Step 8: Enterprise Integration and Advanced CAP Concepts

**Suggested duration:** Week 10

**Topics covered**

- Enterprise application integration fundamentals
- REST APIs and external service consumption
- CAP remote services and service bindings
- Destinations and connectivity concepts
- Consuming external OData and REST APIs
- Handling remote service errors and timeouts
- Pagination and data transformation
- Event-driven architecture fundamentals
- Messaging and asynchronous processing overview
- SAP Event Mesh concepts
- Introduction to SAP S/4HANA API integration
- Communication arrangements and API access concepts
- SAP BTP connectivity to enterprise systems
- Introduction to multitenancy
- CAP extensibility and reusable service patterns
- Clean code, separation of concerns, and maintainability

**Hands-on exercises**

- Consume an external REST API from CAP.
- Configure a destination for a remote service.
- Transform external data into a business response.
- Implement appropriate error handling for remote calls.
- Document a proposed S/4HANA integration design.

**You deliver:** A CAP application that consumes an external service, with integration configuration and error handling.

### Step 9: Testing, Quality, Git Workflow, and Troubleshooting

**Suggested duration:** Week 11

**Topics covered**

- Unit testing fundamentals
- Testing CAP services and event handlers
- Node.js testing tools and assertions
- Mocking external services
- Integration and API testing
- Postman collections and reusable test cases
- Testing successful and failed requests
- Authorization testing
- Input validation and negative test cases
- Test data management
- Logging and debugging
- Code formatting and linting
- Git branching strategies
- Pull requests and code reviews
- Defect tracking and root-cause analysis
- Performance and scalability fundamentals

**Hands-on exercises**

- Write automated tests for service handlers.
- Test validation and authorization scenarios.
- Create a reusable API test collection.
- Review a teammate's code and resolve defects.
- Document and fix a production-style issue.

**You deliver:** An automated test suite, API test collection, code review checklist, and defect report.

### Step 10: SAP BTP Deployment, CI/CD, and Capstone Project

**Suggested duration:** Weeks 12–14

**Topics covered**

- Preparing a CAP application for deployment
- SAP BTP Cloud Foundry architecture
- Cloud Foundry CLI fundamentals
- Application manifests and deployment descriptors
- MTA projects and `mta.yaml`
- Build and deployment processes
- Configuring environment variables and service bindings
- Deploying to SAP BTP
- SAP HANA Cloud integration
- Application authentication and role configuration
- Application logs, monitoring, and troubleshooting
- Introduction to SAP Continuous Integration and Delivery
- CI/CD pipeline fundamentals
- GitHub Actions or comparable pipeline concepts
- Managing configuration across environments
- Deployment verification and smoke testing
- Rollback and release management fundamentals
- Project documentation and architecture diagrams
- Technical presentation and project demonstration

**Hands-on exercises**

- Package a CAP application for deployment.
- Deploy it to an authorized SAP BTP environment.
- Connect it to the configured database service.
- Configure authentication and role assignments.
- Execute smoke tests and inspect application logs.
- Present the architecture and demonstrate the completed application.

**You deliver:** A deployed capstone application, deployment configuration, test evidence, project README, and final presentation.

---

## 3. Skills You Will Develop

By completing the program, learners will have practical experience with:

- JavaScript and modern ES6+ programming
- Node.js application development
- SAP BTP architecture and service concepts
- SAP Cloud Application Programming Model
- CDS data modeling and annotations
- OData V4 service development
- CAP event handlers and business logic
- SQLite and SAP HANA Cloud fundamentals
- SAP Fiori Elements and UI annotations
- REST API integration
- Authentication and role-based authorization
- SAP BTP destinations and service bindings
- Unit testing, API testing, and debugging
- Git, GitHub, and collaborative development
- SAP BTP Cloud Foundry deployment
- MTA packaging and CI/CD fundamentals
- Technical documentation and architecture design

## 4. Career Paths

The program provides a foundation for pursuing entry-level roles such as:

- **Junior SAP BTP Developer** — Builds and maintains cloud applications on SAP BTP.
- **SAP CAP Developer** — Develops domain models, services, and business logic using CAP.
- **SAP Extension Developer** — Builds side-by-side extensions for SAP applications.
- **SAP Fiori Elements Developer** — Develops metadata-driven business interfaces.
- **SAP Integration Developer (Junior)** — Works with APIs, destinations, and application connectivity.
- **Associate SAP Technical Consultant** — Supports SAP application development and technical implementation.
- **Junior Cloud Application Developer** — Applies cloud-native development concepts to enterprise applications.

*These are potential career directions, not a guarantee of employment or placement.*

## 5. Assessment and Evaluation

Learners are assessed through practical implementation, technical understanding, code quality, and project demonstrations.

| Assessment area | Weight |
|---|---:|
| JavaScript and Node.js fundamentals | 10% |
| SAP BTP and CAP architecture | 10% |
| CDS data modeling and persistence | 15% |
| OData services and business logic | 15% |
| Fiori Elements and UI integration | 10% |
| Security and authorization | 10% |
| Integration and automated testing | 10% |
| Deployment and DevOps fundamentals | 10% |
| Capstone project and presentation | 10% |
| **Total** | **100%** |

### Assessment methods

- Weekly coding assignments
- Practical module-end exercises
- CDS modeling and API implementation tasks
- Code reviews and debugging exercises
- Technical quizzes and discussions
- Project demonstrations
- Final capstone evaluation

## 6. Learning Outcomes

By the end of the program, learners should be able to:

- Explain the architecture and core services of SAP BTP.
- Set up a local CAP development environment.
- Develop Node.js applications using modern JavaScript.
- Model business entities and relationships using CDS.
- Expose and consume OData V4 services.
- Implement business rules, validations, actions, and event handlers.
- Configure a Fiori Elements application for a CAP service.
- Implement authentication and role-based authorization.
- Consume external REST and OData services.
- Write automated tests for service logic and APIs.
- Deploy a CAP application to SAP BTP Cloud Foundry.
- Configure persistence, service bindings, and application settings.
- Diagnose common development and deployment issues.
- Explain application architecture and demonstrate a working project.

## 7. Project Portfolio

Learners finish the program with three progressive projects and supporting technical artifacts.

### Project 1: Employee Management Application

**Level:** Beginner

**Features**

- Employee and department data modeling
- CRUD operations
- CDS entities and associations
- OData V4 service exposure
- Basic Fiori Elements interface
- Input validation and sample data

**Portfolio deliverable:** A working employee management application with source code and API documentation.

### Project 2: Procurement and Purchase Order Management

**Level:** Intermediate

**Features**

- Supplier and purchase order management
- Header-item relationships
- Purchase order creation and submission
- Business validations and custom actions
- Role-based access control
- Fiori Elements List Report and Object Page
- Automated service tests
- Collaborative development using Git

**Portfolio deliverable:** A multi-user procurement application with business logic, security, and test evidence.

### Project 3: Enterprise CAP Application — Capstone

**Level:** Advanced

**Suggested business scenarios**

- Sales order management
- Inventory and stock monitoring
- Supplier onboarding
- Expense approval workflow
- Purchase requisition management
- SAP S/4HANA extension application

**Expected features**

- Well-structured CDS domain model
- Multiple service entities and relationships
- Business logic and custom actions
- Authentication and authorization
- External API integration
- Persistent storage
- Fiori Elements user interface
- Automated tests and error handling
- Deployment to SAP BTP
- Technical documentation and architecture diagram

**Portfolio deliverable:** A deployed enterprise-style application with source code, test suite, deployment configuration, README, and final demonstration.

## 8. Development Tools and Learning Environment

| Area | Tools and technologies |
|---|---|
| Programming | JavaScript, Node.js, npm |
| CAP development | SAP CDS development kit, CAP Node.js |
| IDE | Visual Studio Code or SAP Business Application Studio |
| Data modeling | CDS |
| Local database | SQLite |
| Cloud database | SAP HANA Cloud, subject to environment access |
| API testing | Postman or equivalent |
| UI development | SAP Fiori Elements, SAPUI5 fundamentals |
| Version control | Git and GitHub |
| Cloud platform | SAP BTP, Cloud Foundry |
| Deployment | Cloud Foundry CLI, MBT, MTA |
| Testing | Node.js testing tools and CAP test utilities |
| CI/CD | SAP Continuous Integration and Delivery or equivalent tooling |

*Tool versions, platform entitlements, and deployment exercises should be aligned with the SAP BTP environment available to the training batch.*

## 9. Recommended Prerequisites

This program is designed for freshers and graduates with little or no previous SAP experience.

Learners should have:

- Basic computer and file management skills
- An interest in programming and enterprise application development
- Familiarity with installing and using developer tools
- Willingness to practice coding daily
- Access to a development computer and a reliable internet connection

Prior SAP ABAP, SAPUI5, or SAP BTP experience is not mandatory.

## 10. What Learners Finish With

At the end of the program, each learner should have:

- JavaScript and Node.js exercise repository
- CAP project created and run locally
- CDS domain model and sample datasets
- OData V4 service with custom business logic
- Fiori Elements application
- Secured application with role definitions
- External API integration example
- Automated tests and API test collection
- Deployed CAP application, subject to platform access
- Three project repositories or documented project milestones
- Architecture diagram and project README
- Final technical presentation
- A portfolio suitable for demonstrating practical skills during interviews

---

## Suggested Next Step

The curriculum can be delivered as a structured 14-week program with weekly learning objectives, practical assignments, instructor reviews, and milestone-based project evaluations. The emphasis should remain on building working applications rather than memorizing SAP concepts.

**Program positioning:** *Learn SAP BTP development by building real applications — from your first CAP service to a deployed enterprise solution.*
