def card_contructor(message):
    return {
      "cards": [
        {
          "header": {
            "title": "<b>Sendy</b>",
            "imageUrl": "https://pbs.twimg.com/profile_images/945830499695714304/uW-wtFiB.jpg",
            "imageStyle": "IMAGE"
          },
          "sections": [
            {
              "widgets": [
                {
                  "textParagraph": {
                    "text": f"{message}"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
