# Project's Architecture Diagram

```mermaid
flowchart TB
    subgraph "Client Layer"
        UI[Web UI]
        MobileApp[Mobile App]
        WebWidget[Website Widget]
    end

    subgraph "API Gateway"
        APIGateway[API Gateway/Load Balancer]
    end

    subgraph "Service Layer"
        AuthService[Authentication Service]
        ChatService[Chat Engine Service]
        KBService[Knowledge Base Service]
        AnalyticsService[Analytics Service]
        LeadService[Lead Management Service]
        NotificationService[Notification Service]
    end

    subgraph "Data Processing"
        NLP[NLP Engine]
        ML[Machine Learning Models]
        ETL[ETL Processes]
    end

    subgraph "Data Storage"
        MongoDB[(Document DB - MongoDB)]
        Redis[(Cache - Redis)]
        Postgres[(Relational DB - PostgreSQL)]
        ElasticSearch[(Search - Elasticsearch)]
    end

    subgraph "External Integrations"
        CRM[CRM Systems]
        Messaging[Messaging Platforms]
        Payment[Payment Gateways]
    end

    UI --> APIGateway
    MobileApp --> APIGateway
    WebWidget --> APIGateway
    
    APIGateway --> AuthService
    APIGateway --> ChatService
    APIGateway --> KBService
    APIGateway --> AnalyticsService
    APIGateway --> LeadService
    APIGateway --> NotificationService
    
    ChatService --> NLP
    AnalyticsService --> ML
    AnalyticsService --> ETL
    
    NLP --> MongoDB
    ChatService --> Redis
    ChatService --> MongoDB
    KBService --> ElasticSearch
    KBService --> MongoDB
    LeadService --> Postgres
    AnalyticsService --> Postgres
    
    LeadService --> CRM
    ChatService --> Messaging
```
## Notes

### Knowledge Base Management System
- A structured database to store FAQs, documentation, product info, and policies.
- The content editing interface should be WYSIWYG for non-technical users to add/edit content. 
- Version control, to track changes and roll back when needed.

### The Chatbots
- Essentially the same as rasa, ManyChat, etc (A drag-and-drop interface for creating convo paths).
- Built with rasa API.

### Lead Automation & Conversion
- Data should be gathered naturally in conversations. Leads could be grouped by interests, needs, stage in funnel, etc.
- The product then should be integrated with CRMs.
