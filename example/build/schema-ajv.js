ajv.addSchema({
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
}, "default.add_news")
