> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all Sandboxes

> List all Sandboxes in the tenant's namespace.

This endpoint queries the database for fast performance.



## OpenAPI

````yaml https://api.host.langchain.com/openapi.json get /v2/sandboxes/boxes
openapi: 3.1.0
info:
  title: LangSmith Deployment Control Plane API
  description: >
    The LangSmith Deployment Control Plane API is used to programmatically
    create and manage

    Agent Server deployments. For example, the APIs can be orchestrated to

    create custom CI/CD workflows.


    ## Host

    https://api.host.langchain.com


    ## Authentication

    To authenticate with the LangSmith Deployment Control Plane API, set the
    `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).


    ## Versioning

    Each endpoint path is prefixed with a version (e.g. `v1`, `v2`).


    ## Quick Start

    1. Call `POST /v2/deployments` to create a new Deployment. The response body
    contains the Deployment ID (`id`) and the ID of the latest (and first)
    revision (`latest_revision_id`).

    1. Call `GET /v2/deployments/{deployment_id}` to retrieve the Deployment.
    Set `deployment_id` in the URL to the value of Deployment ID (`id`).

    1. Poll for revision `status` until `status` is `DEPLOYED` by calling `GET
    /v2/deployments/{deployment_id}/revisions/{latest_revision_id}`.

    1. Call `PATCH /v2/deployments/{deployment_id}` to update the deployment.
  version: 0.1.0
servers: []
security: []
paths:
  /v2/sandboxes/boxes:
    get:
      tags:
        - Sandboxes (v2)
      summary: List all Sandboxes
      description: |-
        List all Sandboxes in the tenant's namespace.

        This endpoint queries the database for fast performance.
      operationId: list_claims_v2_sandboxes_boxes_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SandboxClaimListResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    SandboxClaimListResponse:
      properties:
        sandboxes:
          items:
            $ref: '#/components/schemas/SandboxClaimResponse'
          type: array
          title: Sandboxes
      type: object
      required:
        - sandboxes
      title: SandboxClaimListResponse
      description: Response model for listing Sandboxes.
    SandboxClaimResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        template_name:
          type: string
          title: Template Name
        dataplane_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Dataplane Url
          description: Direct URL for data plane operations (execute, files, terminal)
        created_at:
          anyOf:
            - type: string
            - type: 'null'
          title: Created At
        updated_at:
          anyOf:
            - type: string
            - type: 'null'
          title: Updated At
      type: object
      required:
        - id
        - name
        - template_name
      title: SandboxClaimResponse
      description: Response model for a SandboxClaim.

````