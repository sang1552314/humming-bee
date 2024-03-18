import os
import time
import music21
from music21 import *
from midi2audio import FluidSynth

class HummingGenerator:
    def __init__(self, abc_notes) -> None:
        super().__init__()
        self.abc_notes = abc_notes

    def generator(self):
        ts =  time.time()
        # Parse ABC notation to music21 stream
        try:
            s = converter.parse(self.abc_notes)
        except music21.converter.ConverterException as e:
            raise(e)

        # Check if directory exists, else make directory
        output_dir = './storage'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Write stream to MIDI file
        mf = midi.translate.streamToMidiFile(s)
        midi_path = f'{output_dir}/output.mid'
        mf.open(midi_path, 'wb')
        mf.write()
        mf.close()

        # Convert MIDI to MP3
        fs = FluidSynth()
        fs.midi_to_audio(midi_path, f'{output_dir}/output.wav')