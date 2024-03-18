from abc import ABC
import utils.ai_bot as ai_bot

class AIProducer(ABC):
    def __init__(self, agent, model) -> None:
        self.bot_statation = ai_bot.BotStation(agent)
        self.client = self.bot_statation.get_client()
        self.model = model

    def generator(self, description):
        augmented_description = f'''
        Your task is recreating the given description delimited by triple backticks as a musical score by using ABC notation
        Description: ```{description}```

        #Notes:
        - return only ABC notation. Do not giving any explaination 
        - using the given chord progression: 'Dm', 'C', 'Dm', 'Dm', 'C', 'Dm', 'C', 'Dm'
        '''
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful MUSIC COMPOSER."
                },
                {
                    "role": "user",
                    "content": augmented_description,
                }
            ],
            model=self.model,
        )
        text_response =  chat_completion.choices[0].message.content
        print(text_response)

        return self.post_process_response(text=text_response)
    
    def post_process_response(self, text):
        text = text.replace('`', '').\
                    replace('abc', '')
        return text

