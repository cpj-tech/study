import tkinter as tk
import tkinter.messagebox as messagebox


# カゴの移動方向を設定する関数
def direction_control():
    pass


# 扉を開く関数
def door_control():
    pass


# カゴを移動する関数
def cage_control():
    pass


# 「次の動作」ボタンがクリックされたときに呼び出される関数
def next_motion():
    # カゴの移動方向を設定する
    direction_control()

    # 扉を開く
    if door_control():
        # 扉を開いたらカゴの移動は次の動作にする
        return

    # カゴを移動する
    cage_control()


# カゴの移動方向を示すボタンがクリックされたときに呼び出される関数
def change_direction():
    # 「未定」「上昇」「下降」を順番に切り替える
    cd = cage_direction.get()
    if cd == "未定":
        cage_direction.set("上昇")
    elif cd == "上昇":
        cage_direction.set("下降")
    else:
        cage_direction.set("未定")


# 以下はグローバル変数およびGUI
# 最上階を5Fとする
TOP_FLOOR = 5

# Tkのルートを作成する
root = tk.Tk()
root.title("エレベータ")

# 現在のカゴの位置を1~5で表す。
cage_position = tk.IntVar()
cage_position.set(1)

# カゴの動作（"未定"、"上昇"、"下降"）
cage_direction = tk.StringVar()
cage_direction.set("未定")

# カゴ内のボタンの選択状態をtrue/falseで表す。
cage_buttons = []
for n in range(TOP_FLOOR + 1):
    bv = tk.BooleanVar()
    bv.set(False)
    cage_buttons.append(bv)

# 各階の[↑]ボタンの選択状態
floor_up_buttons = []
for n in range(TOP_FLOOR + 1):
    bv = tk.BooleanVar()
    bv.set(False)
    floor_up_buttons.append(bv)

# 各階の[↓]ボタンの選択状態
floor_down_buttons = []
for n in range(TOP_FLOOR + 1):
    bv = tk.BooleanVar()
    bv.set(False)
    floor_down_buttons.append(bv)

# ラベル付きフレームを作成する
flame1 = tk.LabelFrame(root, text="カゴの現在位置", labelanchor=tk.N)
flame1.grid(row=0, column=0, padx=5, pady=5)
flame2 = tk.LabelFrame(root, text="カゴ内のボタン", labelanchor=tk.N)
flame2.grid(row=0, column=1, padx=5, pady=5)
flame3 = tk.LabelFrame(root, text="各階のボタン", labelanchor=tk.N)
flame3.grid(row=0, column=2, padx=5, pady=5)

# カゴの現在位置を示すラジオボタンを作成する
cp_list = [
    ("5F", 5, 0),
    ("4F", 4, 1),
    ("3F", 3, 2),
    ("2F", 2, 3),
    ("1F", 1, 4),
]
for c_text, c_val, c_row in cp_list:
    rdo = tk.Radiobutton(
        flame1,
        text=c_text,
        value=c_val,
        variable=cage_position,
        indicatoron=0,
        width=4,
        font=("", "20", ""),
        bg="white",
        selectcolor="cyan",
    )
    rdo.grid(row=c_row, column=0, padx=5, pady=5)

# カゴ内のボタンを表すチェックボタンを作成する
cb_list = [("5", 0), ("4", 1), ("3", 2), ("2", 3), ("1", 4)]
for c_text, c_row in cb_list:
    chk = tk.Checkbutton(
        flame2,
        text=c_text,
        variable=cage_buttons[int(c_text)],
        indicatoron=0,
        width=4,
        font=("", "20", ""),
        bg="white",
        selectcolor="yellow",
    )
    chk.grid(row=c_row, column=0, padx=5, pady=5)

# 各階のボタンを表すチェックボタンを作成する
fb_list = [("5", 0), ("4", 1), ("3", 2), ("2", 3), ("1", 4)]
for f_text, f_row in fb_list:
    # 上昇ボタン
    if f_text != "5":
        chk1 = tk.Checkbutton(
            flame3,
            text="↑",
            variable=floor_up_buttons[int(f_text)],
            indicatoron=0,
            width=4,
            font=("", "20", ""),
            bg="white",
            selectcolor="yellow",
        )
        chk1.grid(row=f_row, column=0, padx=5, pady=5)
    # 下降ボタン
    if f_text != "1":
        chk2 = tk.Checkbutton(
            flame3,
            text="↓",
            variable=floor_down_buttons[int(f_text)],
            indicatoron=0,
            width=4,
            font=("", "20", ""),
            bg="white",
            selectcolor="yellow",
        )
        chk2.grid(row=f_row, column=1, padx=5, pady=5)

# カゴの移動方向を示すボタンを作成する
btn_change = tk.Button(
    root, textvariable=cage_direction, command=change_direction
)
btn_change.grid(
    row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S
)

# 「次の動作」ボタンを作成する
btn_next = tk.Button(root, text="次の動作", command=next_motion)
btn_next.grid(
    row=1,
    column=1,
    padx=5,
    pady=5,
    columnspan=2,
    sticky=tk.W + tk.E + tk.N + tk.S,
)

# イベント待ちの無限ループ
root.mainloop()
