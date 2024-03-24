import sys

sys.path.append('utils')
from utils import (ai_producer, rythm_generator)

if __name__ == "__main__":
    description = 'Michael Jackson - Billie Jean'

    ai_producer = ai_producer.AIProducer('openai', 'gpt-3.5-turbo')
    abc_notes = ai_producer.generator(description=description, params={})

    hg = rythm_generator.HummingGenerator(abc_notes)
    try:
        hg.generator()
    except Exception as e:
        raise(e)
