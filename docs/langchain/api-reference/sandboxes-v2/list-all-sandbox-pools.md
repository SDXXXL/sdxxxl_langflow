> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all Sandbox Pools

> List all Sandbox Pools in the tenant's namespace.

This endpoint queries the database for fast performance.



## OpenAPI

````yaml https://api.host.langchain.com/openapi.json get /v2/sandboxes/pools
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
  /v2/sandboxes/pools:
    get:
      tags:
        - Sandboxes (v2)
      summary: List all Sandbox Pools
      description: |-
        List all Sandbox Pools in the tenant's namespace.

        This endpoint queries the database for fast performance.
      operationId: list_warmpools_v2_sandboxes_pools_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WarmPoolListResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    WarmPoolListResponse:
      properties:
        pools:
          items:
            $ref: '#/components/schemas/WarmPoolResponse'
          type: array
          title: Pools
      type: object
      required:
        - pools
      title: WarmPoolListResponse
      description: Response model for listing Sandbox Pools.
    WarmPoolResponse:
      properties:
        id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Id
          description: Unique pool identifier
        name:
          type: string
          title: Name
        template_name:
          type: string
          title: Template Name
        replicas:
          type: integer
          title: Replicas
          description: Desired number of replicas
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
        - name
        - template_name
        - replicas
      title: WarmPoolResponse
      description: Response model for a Sandbox Pool.

````