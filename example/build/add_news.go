package build

type AddNewsParams struct {
  Active bool
  Article *Article
  Id int
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
      "properties": {
        "content": {
          "type": "string"
        },
        "preview": {
          "type": "string"
        }
      },
      "type": "object",
      "result": {
        "type": "object",
        "properties": {}
      },
      "id": "article"
    },
    "id": {
      "type": "integer"
    }
  }
}`
