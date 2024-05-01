import pretty_midi
from services import vocal

print("0: ボーカル作成")
print("1: ドラム作成")
print("2: ベース作成")
print("3: キーボード作成")
mode = input("モード: ")

match mode:
    case "0":
        vocal.vocalCreate()
    case "1":
        vocal.testtest(["Cm", "Dm", "G"])