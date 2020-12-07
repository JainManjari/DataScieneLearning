import os
import dialogflow_v2 as dialogflow
from gnewsclient import gnewsclient


client=gnewsclient.NewsClient()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_newbot.json"

dialogflow_session_client=dialogflow.SessionsClient()
PROJECT_ID="newsbot-yc9r"

def detect_intent_from_text(text,session_id,language_code="en"):
    session=dialogflow_session_client.session_path(PROJECT_ID,session_id)
    text_input=dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input=dialogflow.types.QueryInput(text=text_input)
    response=dialogflow_session_client.detect_intent(session=session,query_input=query_input)
    return response.query_result


# response=detect_intent_from_text("football major break through",12345)

# print(response)

# intent=response.intent.display_name

# print(intent)

# params=dict(response.parameters)

# print(params)


def fetch_news(params):
    client.location=params['geo-country']
    client.language=params['language']
    client.topic=params['topic']
    news=client.get_news()
    return news[:5]


def get_reply(query,chat_id):
    response=detect_intent_from_text(query,chat_id)
    if response.intent.display_name=="get_news":
        return "get_news",dict(response.parameters)
    else:
        return "small_talk",response.fulfillment_text


topics_keyboards=[
    ['Top Stories','World','Nation'],
    ['Business','Technology','Entertainment'],
    ['Sports','Science','Health']
]