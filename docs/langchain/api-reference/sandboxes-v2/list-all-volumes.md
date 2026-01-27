> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all Volumes

> List all persistent volumes in the tenant's sandbox namespace.

This endpoint queries the database for fast performance.



## OpenAPI

````yaml https://api.host.langchain.com/openapi.json get /v2/sandboxes/volumes
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
  /v2/sandboxes/volumes:
    get:
      tags:
        - Sandboxes (v2)
      summary: List all Volumes
      description: |-
        List all persistent volumes in the tenant's sandbox namespace.

        This endpoint queries the database for fast performance.
      operationId: list_volumes_v2_sandboxes_volumes_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VolumeListResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    VolumeListResponse:
      properties:
        volumes:
          items:
            $ref: '#/components/schemas/VolumeResponse'
          type: array
          title: Volumes
      type: object
      required:
        - volumes
      title: VolumeListResponse
      description: Response model for listing Volumes.
    VolumeResponse:
      properties:
        id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Id
          description: Unique volume identifier
        name:
          type: string
          title: Name
        size:
          type: string
          title: Size
        storage_class:
          type: string
          title: Storage Class
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
        - size
        - storage_class
      title: VolumeResponse
      description: Response model for a Volume.

````