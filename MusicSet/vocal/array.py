import pretty_midi
import random

def retArr():
    arr = [
        'A4', 'B4', 'C#5', 'D5', 'C#5', 'B4', 'A4', 'E4', 'F#4', 'A4', 'F#4', 'E4', 'D4', 'C#4', 'A4', 'E4', 'F#4', 'A4', 'D5', 'C#5', 'B4', 'A4', 'B4', 'C#5', 'D5'
    ]
    return arr

def create_random_array(quo):
    pitch_range=('A4', 'C6')
    # pitch_rangeで指定された範囲内でランダムな音程を生成する
    min_pitch = pretty_midi.note_name_to_number(pitch_range[0])
    max_pitch = pretty_midi.note_name_to_number(pitch_range[1])
    
    # ランダムな音程を持つ配列を生成する
    random_array = []
    for _ in range(quo):
        random_pitch_number = random.randint(min_pitch, max_pitch)
        print(random_pitch_number)
        random_note_name = pretty_midi.note_number_to_name(random_pitch_number)
        length = random.randint(int(0.125 * 8), int(1 * 8)) / 8  # 0.125の倍数でランダムな長さを生成

        random_array.append({
            'note_name': random_note_name,
            'length': length
        })
    
    return random_array
