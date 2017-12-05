package build

const buildAddNewsName = `add_news`
const buildAddNewsParamsSchema string = `{
  "type": "object",
  "properties": {
    "active": {
      "type": "boolean"
    },
    "article": {
      "id": "article",
      "type": [
        "object",
        "null"
      ],
      "properties": {
        "content": {
          "type": "string"
        },
        "preview": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "result": {
        "type": "object",
        "properties": {}
      }
    },
    "id": {
      "type": "integer"
    },
    "language": {
      "enum": [
        "ru",
        "en"
      ]
    },
    "tags": {
      "type": [
        "array",
        "null",
        "string"
      ]
    }
  }
}`
