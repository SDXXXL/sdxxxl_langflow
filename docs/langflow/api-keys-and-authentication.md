# API keys and authentication | Langflow Documentation

- Develop
- API keys and authentication

On this page# API keys and authentication

[data-ch-theme="github-dark"] {  --ch-t-colorScheme: dark;--ch-t-foreground: #c9d1d9;--ch-t-background: #0d1117;--ch-t-lighter-inlineBackground: #0d1117e6;--ch-t-editor-background: #0d1117;--ch-t-editor-foreground: #c9d1d9;--ch-t-editor-lineHighlightBackground: #6e76811a;--ch-t-editor-rangeHighlightBackground: #ffffff0b;--ch-t-editor-infoForeground: #3794FF;--ch-t-editor-selectionBackground: #264F78;--ch-t-focusBorder: #1f6feb;--ch-t-tab-activeBackground: #0d1117;--ch-t-tab-activeForeground: #c9d1d9;--ch-t-tab-inactiveBackground: #010409;--ch-t-tab-inactiveForeground: #8b949e;--ch-t-tab-border: #30363d;--ch-t-tab-activeBorder: #0d1117;--ch-t-editorGroup-border: #30363d;--ch-t-editorGroupHeader-tabsBackground: #010409;--ch-t-editorLineNumber-foreground: #6e7681;--ch-t-input-background: #0d1117;--ch-t-input-foreground: #c9d1d9;--ch-t-input-border: #30363d;--ch-t-icon-foreground: #8b949e;--ch-t-sideBar-background: #010409;--ch-t-sideBar-foreground: #c9d1d9;--ch-t-sideBar-border: #30363d;--ch-t-list-activeSelectionBackground: #6e768166;--ch-t-list-activeSelectionForeground: #c9d1d9;--ch-t-list-hoverBackground: #6e76811a;--ch-t-list-hoverForeground: #c9d1d9; }warningNever expose Langflow ports directly to the internet without proper security measures.
Set LANGFLOW_AUTO_LOGIN=False, use a non-default LANGFLOW_SECRET_KEY, and deploy your Langflow server behind a reverse proxy with authentication enabled.
For more information, see Start a Langflow server with authentication enabled.

Authentication credentials help prevent unauthorized access to your Langflow server, flows, and services connected through components.

There are three types of credentials that you use in Langflow:

- Langflow API keys: For authentication with the Langflow API and authorizing server-side Langflow actions like running flows and uploading files.
- Component API keys: For authentication between Langflow and a service connected through a component, such as a model provider or third-party API.
- Authentication environment variables: These environment variables configure how Langflow handles user authentication and authorization.

## Langflow API keys​

You can use Langflow API keys to interact with Langflow programmatically.

By default, most Langflow API endpoints, such as /v1/run/$FLOW_ID, require authentication with a Langflow API key.

Langflow validates API keys against keys stored in the database, but you can configure Langflow to validate API keys against an environment variable instead.
For more information, see LANGFLOW_API_KEY_SOURCE.

To require API key authentication for flow webhook endpoints, use the LANGFLOW_WEBHOOK_AUTH_ENABLE environment variable.
To configure authentication for Langflow MCP servers, see Use Langflow as an MCP server.

### Langflow API key permissions​

A Langflow API key adopts the privileges of the user who created it.
This means that API keys you create have the same permissions and access that you do, including access to your flows, components, and Langflow database.
A Langflow API key cannot be used to access resources outside of your own Langflow server.

In single-user environments, you are always a superuser, and your Langflow API keys always have superuser privileges.

In multi-user environments, users who aren't superusers cannot use their API keys to access other users' resources.
Superusers can only run their own flows, and cannot run flows owned by other users.
You must start your Langflow server with authentication enabled to allow superusers to manage users and create non-superuser accounts.

### Create a Langflow API key​

You can generate a Langflow API key in your Langflow Settings or with the Langflow CLI.

The CLI option is required if your Langflow server is running in --backend-only mode.

- Langflow Settings
- Langflow CLI

1. In the Langflow header, click your profile icon, and then select Settings.
2. Click Langflow API Keys, and then click Add New.
3. Name your key, and then click Create API Key.
4. Copy the API key and store it securely.

If you're serving your flow with --backend-only=true, you can't create API keys in your Langflow Settings because the frontend isn't running.
In this case, you must create API keys with the Langflow CLI.

1. Recommended: Start your Langflow server with authentication enabled.
The Langflow team recommends enabling authentication for security reasons to prevent unauthorized creation of API keys and superusers, especially in production environments.
If authentication isn't enabled (LANGFLOW_AUTO_LOGIN=True), all users are effectively superusers, and they can create API keys with the Langflow CLI.
2. Create an API key with langflow api-key:
_10uv run langflow api-key
All API keys created with the Langflow CLI have superuser privileges because the command requires superuser authentication, and Langflow API keys adopt the privileges of the user who created them.

### Use a Langflow API key​

To authenticate Langflow API requests, pass your Langflow API key an x-api-key header or query parameter.

- HTTP header
- Query parameter

`_10curl -X POST \_10  "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID?stream=false" \_10  -H "Content-Type: application/json" \_10  -H "x-api-key: $LANGFLOW_API_KEY" \_10  -d '{"inputs": {"text":""}, "tweaks": {}}'``_10curl -X POST \_10  "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID?x-api-key=$LANGFLOW_API_KEY" \_10  -H "Content-Type: application/json" \_10  -d '{"inputs": {"text":""}, "tweaks": {}}'`For more information about forming Langflow API requests, see Get started with the Langflow API and Trigger flows with the Langflow API.

### Track API key usage​

By default, Langflow tracks API key usage through total_uses and last_used_at records in your Langflow database.

To disable API key tracking, set LANGFLOW_DISABLE_TRACK_APIKEY_USAGE=True in your Langflow environment variables.
This can help avoid database contention during periods of high concurrency.

### Revoke an API key​

To revoke and delete an API key, do the following:

1. In the Langflow header, click your profile icon, and then select Settings.
2. Click Langflow API Keys.
3. Select the keys you want to delete, and then click  Delete.

This action immediately invalidates the key and prevents it from being used again.

## Component API keys​

Component API keys authorize access to external services that are called by components in your flows, such as model providers, databases, or third-party APIs.
These aren't Langflow API keys or general application credentials.

In Langflow, you can store component API keys in global variables in your Settings or import them from your runtime environment.
For more information, see Global variables.

You create and manage component API keys within the service provider's platform.
Langflow only stores the encrypted key value or a secure reference to a key stored elsewhere; it doesn't manage the actual credentials at the source.
This means that deleting a global variable from Langflow doesn't delete or invalidate the actual API key in the service provider's system.
You must delete or rotate component API keys directly using the service provider's interface or API.

For added security, you can set LANGFLOW_REMOVE_API_KEYS=True to omit API keys and tokens from flow data in your Langflow database.
Additionally, when exporting flows, you can choose to omit API keys from the exported flow JSON.

## Authentication environment variables​

This section describes the available authentication configuration variables.

You can use the .env.example file in the Langflow repository as a template for your own .env file.

### LANGFLOW_AUTO_LOGIN​

This variable controls whether authentication is required to access your Langflow server, including the visual editor, API, and Langflow CLI:

- If LANGFLOW_AUTO_LOGIN=False, automatic login is disabled. Users must sign in to the visual editor, authenticate as a superuser to run certain Langflow CLI commands, and use a Langflow API key for Langflow API requests.
If false, the Langflow team recommends that you also explicitly set LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD to avoid using the insecure default values.
- If LANGFLOW_AUTO_LOGIN=True (default), all API requests require authentication with a Langflow API key, but the visual editor automatically signs in all users as superusers, and Langflow uses only the default superuser credentials.
All users access the same visual editor environment without password protection, they can run all Langflow CLI commands as superusers, and Langflow automatically authenticates internal requests between the backend and frontend based on the users' superuser privileges.
If you also want to bypass authentication for Langflow API requests in addition to other bypassed authentication, see LANGFLOW_SKIP_AUTH_AUTO_LOGIN.

Langflow doesn't allow users to simultaneously edit the same flow in real time.
If two users edit the same flow, Langflow saves only the work of the most recent editor based on the state of that user's workspace. Any changes made by the other user in the interim are overwritten.

#### Default authentication enforcement and LANGFLOW_SKIP_AUTH_AUTO_LOGIN​

In Langflow version 1.6, the default settings are LANGFLOW_AUTO_LOGIN=True and LANGFLOW_SKIP_AUTH_AUTO_LOGIN=False.
This enforces authentication for API requests only, as explained in the preceding section.

For temporary backwards compatibility, you can revert to the fully unauthenticated behavior from earlier versions by setting both variables to true.
However, a future release will set LANGFLOW_AUTO_LOGIN=False and remove LANGFLOW_SKIP_AUTH_AUTO_LOGIN.
At that point, Langflow will strictly enforce API key authentication for API requests, and you can manually disable authentication for some features, like the visual editor, by setting LANGFLOW_AUTO_LOGIN=True.

Authentication enforcement in earlier versionsLangflow version 1.5 was the first version that could enforce authentication for Langflow API requests, regardless of the value of LANGFLOW_AUTO_LOGIN.
As a temporary bypass for backwards compatibility, this version added the LANGFLOW_SKIP_AUTH_AUTO_LOGIN environment variable and set both variables to true by default to preserve the fully unauthenticated behavior from earlier versions.
This allowed users to upgrade to version 1.5 with no change in the authentication behavior.

In Langflow versions earlier than 1.5, Langflow API requests didn't require authentication.
Additionally, the default setting of LANGFLOW_AUTO_LOGIN=True automatically granted all users superuser privileges in the visual editor, and it allowed all users to run all Langflow CLI commands as superusers.

### LANGFLOW_ENABLE_SUPERUSER_CLI​

Controls the availability of the langflow superuser command in the Langflow CLI.
The default is true, but false is recommended to prevent unrestricted superuser creation.
For more information, see langflow superuser.

### LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD​

These variables specify the username and password for the Langflow server's superuser.

`_10LANGFLOW_SUPERUSER=administrator_10LANGFLOW_SUPERUSER_PASSWORD=securepassword`They are required if LANGFLOW_AUTO_LOGIN=False.
Otherwise, they aren't relevant.

When you start a Langflow server with authentication enabled, if these variables are required but not set, then Langflow uses the default values of langflow and langflow.
These defaults don't apply when using the Langflow CLI command langflow superuser.

### LANGFLOW_SECRET_KEY​

This environment variable stores a secret key used for encrypting sensitive data like API keys.
Langflow uses the Fernet library for secret key encryption.

If no secret key is provided, Langflow automatically generates one.

However, you should generate and explicitly set your own key in production environments.
This is particularly important for multi-instance deployments like Kubernetes to ensure consistent encryption across instances.

To generate a secret encryption key for LANGFLOW_SECRET_KEY, do the following:

1. Run the command to generate and copy a secret to the clipboard.
macOS or LinuxWindows
macOS: Generate a secret key and copy it to the clipboard:
_10python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | pbcopy
Linux: Generate a secret key and copy it to the clipboard:
_10python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | xclip -selection clipboard
Unix: Generate a secret key and print it to the terminal to manually copy it:
_10python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')"
Generate a secret key and copy it to the clipboard:
_10python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')"
Generate a secret key and print it to the terminal to manually copy it:
_10_10# Or just print_10python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')"
2. Paste the value into your .env file:
_10LANGFLOW_SECRET_KEY=dBuu...2kM2_fb
If you're running Langflow on Docker, reference the LANGFLOW_SECRET_KEY from your .env file in the docker-compose.yml file like this:
_10environment:_10  - LANGFLOW_SECRET_KEY=${LANGFLOW_SECRET_KEY}

### LANGFLOW_NEW_USER_IS_ACTIVE​

When LANGFLOW_NEW_USER_IS_ACTIVE=False (default), accounts created by superusers are inactive by default and must be explicitly activated before users can sign in to the visual editor.
The superuser can also deactivate a user's account as needed.

When LANGFLOW_NEW_USER_IS_ACTIVE=True, accounts created by superusers are automatically activated.

`_10LANGFLOW_NEW_USER_IS_ACTIVE=False`Only superusers can manage user accounts for a Langflow server, but user management only matters if your server has authentication enabled.
For more information, see Start a Langflow server with authentication enabled.

### LANGFLOW_API_KEY_SOURCE​

This variable controls how Langflow validates API keys.

ValueDescription`db`(default)Validates API keys againstLangflow API keysstored in the database. This is the standard behavior where users create and manage API keys through the Langflow UI or CLI.`env`Validates API keys against the`LANGFLOW_API_KEY`environment variable. Useful for Kubernetes deployments, CI/CD pipelines, or any environment where you want to inject a pre-defined API key without database configuration.By default, Langflow validates the x-api-key header against the Langflow database with LANGFLOW_API_KEY_SOURCE=db.
When using database-based validation, you can create multiple keys with per-user permissions, track usage, and manage keys through the Langflow UI or CLI.

When LANGFLOW_API_KEY_SOURCE=env, Langflow validates the x-api-key header against the value of the LANGFLOW_API_KEY environment variable.
This means Langflow runs securely in stateless environments, such as with LFX or Kubernetes secrets.

When LANGFLOW_API_KEY_SOURCE=env, only a single API key can be used for the deployment. All authenticated requests use the same API key, and successful authentication grants superuser privileges.
This mode is designed for single-tenant deployments or automated systems, not multi-user environments where different users need different access levels. To rotate your keys, update the environment variable and restart the Langflow server.

To enable environment-based API key validation:

1. In the Langflow .env file, set the API key source to env:
_10LANGFLOW_API_KEY_SOURCE=env
2. In the Langflow .env file, set the API key value:
_10LANGFLOW_API_KEY=your-secure-api-key
3. Use the API key in your requests:
_10curl -X POST \_10  "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false" \_10  -H "Content-Type: application/json" \_10  -H "x-api-key: LANGFLOW_API_KEY" \_10  -d '{"inputs": {"text":""}, "tweaks": {}}'
Replace LANGFLOW_SERVER_ADDRESS, FLOW_ID, and LANGFLOW_API_KEY with the values from your deployment.

Kubernetes deployment exampleTo configure an environment-based API key in a Kubernetes Secret, do the following:

1. Create a Kubernetes Secret with your API key:
_10apiVersion: v1_10kind: Secret_10metadata:_10  name: langflow-api-key_10type: Opaque_10stringData:_10  api-key: "YOUR_API_KEY"
Replace YOUR_API_KEY with the LANGFLOW_API_KEY value from the Langflow .env file.
2. Reference the langflow-api-key Secret in your Kubernetes deployment:
_18apiVersion: apps/v1_18kind: Deployment_18metadata:_18  name: langflow_18spec:_18  template:_18    spec:_18      containers:_18      - name: langflow_18        image: langflowai/langflow:latest_18        env:_18        - name: LANGFLOW_API_KEY_SOURCE_18          value: "env"_18        - name: LANGFLOW_API_KEY_18          valueFrom:_18            secretKeyRef:_18              name: langflow-api-key_18              key: api-key

Docker Compose exampleTo configure an environment-based API key in Docker Compose, do the following:

1. Set the API key in your Langflow .env file.
_10LANGFLOW_API_KEY=your-secure-api-key
Replace YOUR_API_KEY with your actual Langflow API key value.
2. Create or update your docker-compose.yml file to set LANGFLOW_API_KEY_SOURCE=env and reference the LANGFLOW_API_KEY.
_10services:_10  langflow:_10    image: langflowai/langflow:latest_10    environment:_10      - LANGFLOW_API_KEY_SOURCE=env_10      - LANGFLOW_API_KEY=${LANGFLOW_API_KEY}_10    ports:_10      - "7860:7860"

### LANGFLOW_CORS_*​

Cross-Origin Resource Sharing (CORS) configuration controls how authentication credentials are handled when your Langflow frontend and backend are served from different origins.
The following LANGFLOW_CORS_* environment variables are available:

VariableFormatDefaultDescription`LANGFLOW_CORS_ALLOW_CREDENTIALS`Boolean`True`Whether to allow credentials, such as cookies and authorization headers, in CORS requests.`LANGFLOW_CORS_ALLOW_HEADERS`List[String] or String`*`The allowed headers for CORS requests. Provide a comma-separated list of headers or use`*`to allow all headers.`LANGFLOW_CORS_ALLOW_METHODS`List[String] or String`*`The allowed HTTP methods for CORS requests. Provide a comma-separated list of methods or use`*`to allow all methods.`LANGFLOW_CORS_ORIGINS`String`*`The allowed CORS origins. Provide a comma-separated list of origins or use`*`for all origins.The default configuration enables CORS credentials and uses wildcards (*) to allow all origins, headers, and methods:

`_10LANGFLOW_CORS_ORIGINS=*_10LANGFLOW_CORS_ALLOW_CREDENTIALS=True_10LANGFLOW_CORS_ALLOW_HEADERS=*_10LANGFLOW_CORS_ALLOW_METHODS=*`dangerLangflow's default CORS settings can be a security risk in production environments because any website can make requests to your Langflow API, and any website can include credentials in cross-origin requests, including authentication cookies and authorization headers.

In production deployments, specify exact origins in LANGFLOW_CORS_ORIGINS.
You can also specify allowed headers and methods, if needed.
For example:

`_10LANGFLOW_CORS_ORIGINS=["https://yourdomain.com","https://app.yourdomain.com"]_10LANGFLOW_CORS_ALLOW_CREDENTIALS=True_10LANGFLOW_CORS_ALLOW_HEADERS=["Content-Type","Authorization"]_10LANGFLOW_CORS_ALLOW_METHODS=["GET","POST","PUT"]`### SSRF protection​

The following environment variables configure Server-Side Request Forgery (SSRF) protection for the API Request component.
SSRF protection prevents requests to internal or private network resources, such as private IP ranges, loopback addresses, and cloud metadata endpoints.

VariableFormatDefaultDescription`LANGFLOW_SSRF_PROTECTION_ENABLED`Boolean`False`Enable SSRF protection for the**API Request**component. When enabled, the component blocks requests to private IP addresses. When disabled, requests are not blocked.`LANGFLOW_SSRF_ALLOWED_HOSTS`List[String]Not setA comma-separated list of allowed hosts, IP addresses, or CIDR ranges that can bypass SSRF protection checks. For example:`192.168.1.0/24,10.0.0.5,*.internal.company.local`.### LANGFLOW_WEBHOOK_AUTH_ENABLE​

This variable controls whether API key authentication is required for webhook endpoints.

VariableFormatDefaultDescription`LANGFLOW_WEBHOOK_AUTH_ENABLE`Boolean`False`When`True`, webhook endpoints require API key authentication and validate that the authenticated user owns the flow being executed. When`False`, no Langflow API key is required and all requests to the webhook endpoint are treated as being sent by the flow owner.By default, webhooks run as the flow owner without authentication with LANGFLOW_WEBHOOK_AUTH_ENABLE=False.

To require API key authentication for webhooks, in your Langflow .env file, set LANGFLOW_WEBHOOK_AUTH_ENABLE=True.

When webhook authentication is enabled, you must provide a Langflow API key with each webhook request as an HTTP header or query parameter. For more information, see Require authentication for webhooks.

## Start a Langflow server with authentication enabled​

This section shows you how to use the authentication environment variables to deploy a Langflow server with authentication enabled.
This involves disabling automatic login, setting superuser credentials, generating a secret encryption key, and enabling user management.

This configuration is recommended for any deployment where Langflow is exposed to a shared or public network, or where multiple users access the same Langflow server.

With authentication enabled, all users must sign in to the visual editor with valid credentials, and API requests require authentication with a Langflow API key.
Additionally, you must sign in as a superuser to manage users and create a Langflow API key with superuser privileges.

### Start the Langflow server​

1. Create a .env file with the following variables:
_10LANGFLOW_AUTO_LOGIN=False_10LANGFLOW_SUPERUSER=_10LANGFLOW_SUPERUSER_PASSWORD=_10LANGFLOW_SECRET_KEY=_10LANGFLOW_NEW_USER_IS_ACTIVE=False_10LANGFLOW_ENABLE_SUPERUSER_CLI=False
Your .env file can have other environment variables.
This example focuses on authentication variables.
2. Set LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD to your desired superuser credentials.
For a one-time test, you can use basic credentials like administrator and password.
Strong, securely-stored credentials are recommended in genuine development and production environments.
3. Recommended: Generate and set a LANGFLOW_SECRET_KEY for encrypting sensitive data.
If you don't set a secret key, Langflow generates one automatically, but this isn't recommended for production environments.
For instructions on generating and setting a secret key, see LANGFLOW_SECRET_KEY.
4. Save your .env file with the populated variables. For example:
_10LANGFLOW_AUTO_LOGIN=False_10LANGFLOW_SUPERUSER=administrator_10LANGFLOW_SUPERUSER_PASSWORD=securepassword_10LANGFLOW_SECRET_KEY=dBuu...2kM2_fb_10LANGFLOW_NEW_USER_IS_ACTIVE=False_10LANGFLOW_ENABLE_SUPERUSER_CLI=False
5. Start Langflow with the configuration from your .env file:
_10uv run langflow run --env-file .env
Starting Langflow with a .env file automatically authenticates you as the superuser set in LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD.
If you don't explicitly set these variables, the default values are langflow and langflow for system auto-login.
6. Verify the server is running. The default location is http://localhost:7860.

Next, you can add users to your Langflow server to collaborate with others on flows.

### Manage users as an administrator​

1. To complete your first-time login as a superuser, go to http://localhost:7860/login.
If you aren't using the default location, replace localhost:7860 with your server's address.
2. Log in with the superuser credentials you set in your .env (LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD).
3. To manage users on your server, navigate to /admin, such as http://localhost:7860/admin, click your profile icon, and then click Admin Page.
As a superuser, you can add users, set permissions, reset passwords, and delete accounts.
4. To add a user, click New User, and then complete the user account form:
Enter a username and password.
To activate the account immediately, select Active. Inactive users cannot sign in or access flows they created before becoming inactive.
Deselect Superuser if you don't want the user to have full administrative privileges.
Click Save. The new user appears in the Admin Page.
5. Send the credentials to the user so they can sign in to Langflow. The superuser sets the initial password when creating the account, so users must receive their login credentials from the superuser.
6. To test the new user's access, sign out of Langflow, and then sign in with the new user's credentials.
Try to access the /admin page.
You are redirected to the /flows page if the new user isn't a superuser.

## See also​

- Langflow environment variables
