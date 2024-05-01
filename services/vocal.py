import pretty_midi
from MusicSet.vocal.array import *
from Common.ChordTheory import *

def vocalCreate():
    # Create a PrettyMIDI object
    cello_c_chord = pretty_midi.PrettyMIDI()
    # Create an Instrument instance for a cello instrument
    cello_program = pretty_midi.instrument_name_to_program('Cello')
    cello = pretty_midi.Instrument(program=cello_program)

    # 配列の用意
    random_notes = get_ramdom_melody(["C", "Cm", "C", "Cm"])
    print(random_notes)

    # スタート時間
    start_time = 0
    # 音符をMIDIに追加
    for note_info in random_notes:
        # 音符の情報を取得
        note_name = note_info['note']
        length = note_info['length']
        
        # MIDIノートナンバーを取得
        note_number = pretty_midi.note_name_to_number(note_name)
        
        # Noteインスタンスを作成してInstrumentに追加
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=start_time + length)
        cello.notes.append(note)
    
        # 次の音符のスタート時間を更新
        start_time += length
    
    cello_c_chord.instruments.append(cello)
    cello_c_chord.tempo = 150
    cello_c_chord.write('vocal-demo.mid')