package build

type AddNewsParams struct {
    Active   bool        `json:"active"`
    Article  *Article    `json:"article"`
    Id       int         `json:"id"`
    Language string      `json:"language"`
    Tags     interface{} `json:"tags"`
}

type AddNewsResult struct {
}

var AddNewsParamsSchema string = `{
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
        "text"
      ]
    }
  }
}`
