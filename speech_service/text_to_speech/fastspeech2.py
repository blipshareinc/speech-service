from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor
from datetime import datetime
from os import path, makedirs

import tensorflow as tf
import numpy as np
import soundfile as sf
import yaml
import argparse

def process(text: str, output_dir: str):
    '''
    Description: Function to process input text and convert to audio (.wav) using FastSpeech2
    @param: text -- str. Text to be converted.
    @param: output_dir -- str. Absolute path of the output directory where audio file to be generated
    @return: output_file -- str. Absolute path to the output audio (.wav) file
    '''

    # if the output directory does not exist, create one
    if not path.exists(output_dir):
        makedirs(output_dir)

    # initialize fastspeech2 model.
    fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")

    # initialize mb_melgan model
    mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")

    # inference
    processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")

    input_ids = processor.text_to_sequence(text)

    # fastspeech inference

    _, mel_after, _, _, _ = fastspeech2.inference(
        input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
        energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # melgan inference
    audio_after = mb_melgan.inference(mel_after)[0, :, 0]

    # save to file
    datetime_str = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    output_file = path.join(output_dir, 'audio_%s.wav' % datetime_str)
    sf.write(output_file, audio_after, 22050, "PCM_16")

    # return path of the audio file
    return output_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Text to speech")
    parser.add_argument("-t", "--TEXT", dest="text", help="Text to be translated to audio", required=True)
    parser.add_argument("-o", "--OUTPUT_DIR", dest="output_dir", help="Absolute path to output directory", required=True)

    # parse arguments
    args = parser.parse_args()

    # process
    process(args.text, args.output_dir)
