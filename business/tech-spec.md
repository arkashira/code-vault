```markdown
# Technical Specification for Code Vault

## Stack
- **Language**: TypeScript
- **Framework**: NestJS (for building scalable server-side applications)
- **Runtime**: Node.js (v14 or higher)

## Hosting
- **Free Tier**: 
  - **Platform**: Vercel (for frontend deployment)
  - **Platform**: Heroku (for backend deployment)
- **Production**: 
  - **Platform**: AWS (using EC2 for backend and S3 for storage)
  - **Platform**: DigitalOcean (for scalable droplets)

## Data Model
### Tables/Collections
1. **Users**
   - `user_id`: UUID (Primary Key)
   - `email`: String (Unique)
   - `password_hash`: String
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

2. **Projects**
   - `project_id`: UUID (Primary Key)
   - `user_id`: UUID (Foreign Key to Users)
   - `name`: String
   - `description`: String
   - `created_at`: Timestamp
   - `updated_at`: Timestamp

3. **Deliverables**
   - `deliverable_id`: UUID (Primary Key)
   - `project_id`: UUID (Foreign Key to Projects)
   - `file_path`: String
   - `timestamp`: Timestamp
   - `status`: Enum (Pending, Released, Disputed)

4. **Milestones**
   - `milestone_id`: UUID (Primary Key)
   - `project_id`: UUID (Foreign Key to Projects)
   - `amount`: Decimal
   - `due_date`: Timestamp
   - `status`: Enum (Pending, Completed)

5. **Transactions**
   - `transaction_id`: UUID (Primary Key)
   - `milestone_id`: UUID (Foreign Key to Milestones)
   - `user_id`: UUID (Foreign Key to Users)
   - `amount`: Decimal
   - `timestamp`: Timestamp
   - `status`: Enum (Pending, Completed, Disputed)

## API Surface
1. **User Registration**
   - **Method**: POST
   - **Path**: `/api/users/register`
   - **Purpose**: Register a new user.

2. **User Login**
   - **Method**: POST
   - **Path**: `/api/users/login`
   - **Purpose**: Authenticate user and return a JWT.

3. **Create Project**
   - **Method**: POST
   - **Path**: `/api/projects`
   - **Purpose**: Create a new project.

4. **Upload Deliverable**
   - **Method**: POST
   - **Path**: `/api/deliverables`
   - **Purpose**: Upload a new deliverable to a project.

5. **Create Milestone**
   - **Method**: POST
   - **Path**: `/api/milestones`
   - **Purpose**: Create a new milestone for a project.

6. **Release Payment**
   - **Method**: POST
   - **Path**: `/api/transactions/release`
   - **Purpose**: Release payment for a completed milestone.

7. **Dispute Transaction**
   - **Method**: POST
   - **Path**: `/api/transactions/dispute`
   - **Purpose**: Initiate a dispute for a transaction.

8. **Get Project Details**
   - **Method**: GET
   - **Path**: `/api/projects/:project_id`
   - **Purpose**: Retrieve details of a specific project.

9. **Get Deliverables**
   - **Method**: GET
   - **Path**: `/api/projects/:project_id/deliverables`
   - **Purpose**: List all deliverables for a project.

10. **Get User Transactions**
    - **Method**: GET
    - **Path**: `/api/users/:user_id/transactions`
    - **Purpose**: Retrieve all transactions for a user.

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for user sessions.
- **Secrets Management**: Use AWS Secrets Manager for storing sensitive information (e.g., database credentials).
- **IAM**: Role-based access control (RBAC) to manage user permissions for different actions within the application.

## Observability
- **Logs**: Use Winston for logging application events and errors.
- **Metrics**: Integrate Prometheus for collecting metrics on application performance.
- **Traces**: Use OpenTelemetry for distributed tracing to monitor requests across services.

## Build/CI
- **Continuous Integration**: Use GitHub Actions for automated testing and deployment.
- **Build Process**: 
  - Linting: ESLint
  - Testing: Jest
  - Build Command: `npm run build`
- **Deployment**: Automated deployment to Heroku and Vercel upon merging to the main branch.
```
