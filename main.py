from utils import (ai_producer, rythm_generator)

if __name__ == "__main__":
    description = 'Japanese samurai battle, fantansy, dramatic, honor, god'

    ai_producer = ai_producer.AIProducer('togetherai', 'mistralai/Mixtral-8x7B-Instruct-v0.1')
    abc_notes = ai_producer.generator(description=description)

    hg = rythm_generator.HummingGenerator(abc_notes)
    hg.generator()
