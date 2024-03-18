import os 
from abc import ABC, abstractmethod
from openai import OpenAI
import together

class AIBot(ABC):
    def __init__(self, key=None, base_url=None) -> None:
        super().__init__()
        self.key = key
        self.base_url = base_url

    @abstractmethod
    def init_client(self):
        pass

    @abstractmethod
    def get_available_models(self) -> list:
        pass

class OpenAIChatBot(AIBot):
    def __init__(self, key=None, base_url=None) -> None:
        super().__init__(key, base_url)

    def init_client(self):
        return OpenAI(api_key=self.key, base_url=self.base_url)
    
    def get_available_models(self) -> list:
        return [
            'gpt-3.5-turbo',
            'gpt-3.5-turbo-instruct',
            'gpt-4',
        ]

class TogetherAIChatBot(OpenAIChatBot):
    def __init__(self, key=None, base_url=None) -> None:
        super().__init__(key, base_url)

    def get_available_models(self) -> list:
        together.api_key = self.key
        model_list = together.Models.list()
        model_names = [model_dict['name'] for model_dict in model_list]
        return model_names
    
class AnyscaleChatBot(OpenAIChatBot):
    def __init__(self, key=None, base_url=None) -> None:
        super().__init__(key, base_url)

    def get_available_models(self) -> list:
        return [
            'mistralai/Mixtral-8x7B-Instruct-v0.1'
        ]
    
# class LlamaCppLocalChatBot(OpenAIChatBot):
#     def __init__(self, key=None, base_url=None) -> None:
#         super().__init__(key, base_url)

#     def get_available_models(self) -> str | list | None:
#         return [
#             'mistral-7b-openorca.Q4_0'
#         ]


class BotStation(ABC):
    def __init__(self, agent) -> None:
        super().__init__()
        self.agent = agent

    def get_client(self) -> AIBot:
        if 'openai' in self.agent:
            chatbot = OpenAIChatBot(key=os.getenv("OPENAI_API_KEY"), base_url=None)
        
        if 'togetherai' in self.agent:
            chatbot = TogetherAIChatBot(key=os.getenv('TOGETHERAI_API_KEY'), base_url='https://api.together.xyz')

        if 'anyscale' in self.agent:
            chatbot = AnyscaleChatBot(key=os.getenv('ANYSCALE_API_KEY'), base_url='https://api.endpoints.anyscale.com/v1')

        # if 'local' in self.agent:
        #     chatbot = LlamaCppLocalChatBot(key=None, base_url='http://localhost:8000/v1')
            
        client = chatbot.init_client()

        return client

    def get_available_models(self) -> list:
        if 'openai' in self.agent:
            chatbot = OpenAIChatBot(key=os.getenv("OPENAI_API_KEY"), base_url=None)
        
        if 'togetherai' in self.agent:
            chatbot = TogetherAIChatBot(key=os.getenv('TOGETHERAI_API_KEY'), base_url='https://api.together.xyz')

        if 'anyscale' in self.agent:
            chatbot = AnyscaleChatBot(key=os.getenv('ANYSCALE_API_KEY'), base_url='https://api.endpoints.anyscale.com/v1')

        # if 'local' in self.agent:
        #     chatbot = LlamaCppLocalChatBot(key=None, base_url='http://localhost:8000/v1')
            
        models = chatbot.get_available_models()

        return models