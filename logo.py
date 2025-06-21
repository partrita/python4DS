import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patheffects import Stroke

text = "Python4DS"

cmap = plt.cm.cividis
font = FontProperties()
font.set_name("Fira Code Bold")


def get_logo():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_facecolor("w")
    for x in np.linspace(0, 1, 100):
        lw, color = x * 225, cmap(1 - x)
        for i, letter in enumerate([x for x in text]):
            t = ax.annotate(
                letter,
                (i * 50, 0),
                va="center",
                size=40,
                ha="center",
                zorder=-lw + 1,
                color="#6b5496",
            )
            t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
    ax.set_ylim(-60, 60)
    ax.set_xlim(-60, 450)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("logo.png")


get_logo()
# 이 파이썬 스크립트는 Matplotlib를 사용하여 "Python4DS" 텍스트 로고를 생성하고 "logo.png" 파일로 저장합니다.
# 스크립트에는 사용자 정의 글꼴, 색상맵 및 경로 효과를 사용하여 시각적으로 흥미로운 로고를 만듭니다.
# 주석이 거의 없는 비교적 간단한 스크립트이므로, 번역할 주석이 없습니다.
# 코드 자체는 이미 명확하며, 추가 설명이 필요한 경우 함수나 변수 이름 위에 주석을 추가할 수 있습니다.
