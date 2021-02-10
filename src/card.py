def card_contructor(subs_count, invalid_subs_count):
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
                    "text": f"Subscribers list has been updated:<br>New Subscribers: <b>{subs_count}</b><br>Invalid Emails: <b>{invalid_subs_count}</b>"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
