---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: python3
  language: python
  name: python3
---
(visualise)=
# 시각화

책의 첫 부분을 읽은 후 데이터 과학 수행에 가장 중요한 도구의 기본 사항을 이해했습니다. 이제 세부 정보로 자세히 들어갈 차례입니다. 이 책의 이 부분에서는 데이터 시각화에 대해 더 자세히 배우고({ref}`vis-layers` 참조) 다양한 종류의 데이터 시각화({ref}`exploratory-data-analysis` 및 {ref}`communicate-plots` 참조)의 세부 정보에 대해 더 자세히 알아봅니다. 이 짧은 장에서는 시각화를 만드는 다양한 방법과 시각화의 다양한 목적에 대해 설명합니다.

## 데이터 시각화 철학

코드를 사용하여 데이터 시각화를 만드는 접근 방식에는 크게 두 가지 범주가 있습니다. *명령형*(개별 요소에서 원하는 것을 구축)과 *선언형*(미리 존재하는 옵션 목록에서 원하는 것을 말함)입니다. 어떤 것을 사용할지 선택하는 데는 장단점이 있습니다. 명령형 라이브러리는 유연성을 제공하지만 다소 장황한 단점이 있습니다. 선언형 라이브러리는 데이터를 플로팅하는 빠른 방법을 제공하지만 처음부터 올바른 형식인 경우에만 가능하며 특수 차트 유형에 대한 사용자 지정은 더 어렵습니다.

파이썬에는 아마도 가장 강력한 명령형 플로팅 패키지인 **matplotlib**과 이미 살펴본 놀라운 선언형 라이브러리인 **lets-plot**을 포함하여 많은 훌륭한 플로팅 패키지가 있습니다. 이 두 라이브러리는 많은 것을 할 수 있으며 각각 전체 책의 가치가 있을 수 있습니다. 그러나 다행스럽게도 우리는 둘 중 하나의 몇 가지 명령으로 필요한 것의 95%를 수행할 수 있습니다. 일반적으로 이 책을 가능한 한 가볍게 유지하기 위해 가능한 한 **lets-plot**을 사용하기로 결정했으며 {ref}`vis-layers`에서는 이를 직접 사용하는 방법에 대한 심층적인 둘러보기를 제공합니다.

## 데이터 시각화의 목적

데이터 시각화에는 모든 종류의 다양한 목적이 있습니다. 시각화에는 세 가지 광범위한 범주가 있다는 점을 염두에 두는 것이 유용합니다.

- 탐색적
- 과학적
- 서사적

각각을 좀 더 자세히 살펴보겠습니다.

### 탐색적 데이터 시각화

세 가지 종류 중 첫 번째는 *탐색적 데이터 시각화*이며, 데이터를 보고 이해하려고 할 때 수행하는 종류입니다. 데이터를 플로팅하는 것만으로도 발생할 수 있는 모든 문제에 대한 느낌을 얻는 데 정말 좋은 전략입니다. 이것은 아마도 앤스컴의 콰르텟에서 가장 유명하게 시연되었습니다. 동일한 평균, 표준 편차 및 상관 관계를 갖지만 데이터 분포가 매우 다른 네 가지 다른 데이터 세트입니다.

```{code-cell} ipython3
---
tags: [remove-input]
---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline

# 플롯 설정
plt.style.use("https://github.com/aeturrell/python4DS/raw/main/plot_style.txt")
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# 가독성을 위해 표시되는 최대 행 설정
pd.set_option("display.max_rows", 6)

x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

datasets = {"I": (x, y1), "II": (x, y2), "III": (x, y3), "IV": (x4, y4)}

fig, axs = plt.subplots(
    2,
    2,
    sharex=True,
    sharey=True,
    figsize=(10, 6),
    gridspec_kw={"wspace": 0.08, "hspace": 0.08},
)
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))

for ax, (label, (x, y)) in zip(axs.flat, datasets.items()):
    ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va="top")
    ax.tick_params(direction="in", top=True, right=True)
    ax.plot(x, y, "o")

    # 선형 회귀
    p1, p0 = np.polyfit(x, y, deg=1)  # 기울기, 절편
    ax.axline(xy1=(0, p0), slope=p1, color="r", lw=2)

    # 통계용 텍스트 상자 추가
    stats = (
        f"$\\mu$ = {np.mean(y):.2f}\n"
        f"$\\sigma$ = {np.std(y):.2f}\n"
        f"$r$ = {np.corrcoef(x, y)[0][1]:.2f}"
    )
    bbox = dict(boxstyle="round", fc="blanchedalmond", ec="orange", alpha=0.5)
    ax.text(
        0.95,
        0.07,
        stats,
        fontsize=9,
        bbox=bbox,
        transform=ax.transAxes,
        horizontalalignment="right",
    )

plt.suptitle("앤스컴의 콰르텟")
plt.show()
```

탐색적 시각화는 일반적으로 빠르고 지저분하며 유연합니다. 일부 탐색적 데이터 시각화는 자동화될 수 있으며 [**skimpy**](https://aeturrell.github.io/skimpy/)를 포함하여 이를 지원하는 다양한 패키지가 있습니다.

그러나 당신과 아마도 당신의 공동 저자/협력자를 제외하고는 다른 많은 사람들이 당신의 탐색적 시각화를 보아서는 안 됩니다! 일반적으로 빠르게 작업되고, 수가 많으며, 일회용입니다. 이에 대해서는 {ref}`exploratory-data-analysis`에서 더 자세히 살펴보겠습니다.

### 과학적 데이터 시각화

두 번째 종류인 과학적 데이터 시각화는 탐색적 시각화의 정수입니다. 더 기술적인 논문에 포함할 수 있는 종류의 플롯이며, 천 마디 말을 하는 그림입니다. 저는 종종 블랙홀의 첫 번째 이미지 {cite:t}`akiyama2019first`를 이것의 대표적인 예로 생각합니다. 과학적 플롯에는 많은 정보를 담을 수 있으며, 짧은 형식의 저널에서는 필요할 수 있습니다. 8페이지 제한이 있는 저널 Physical Review Letters는 거의 모든 호에 이 장르의 고전을 게재합니다. 이러한 종류의 차트에서는 중요한 값을 플롯에서 정확하게 읽을 수 있도록 하는 것이 특히 중요합니다. 그러나 연구에서 결정적인 결과를 제시하는 종류의 플롯일 수도 있습니다. 생계를 위해 차트를 보지 않는 사람들에게는 흥미롭지 않을 수 있지만 동료들에게는 흥미롭고, 마찬가지로 중요하게도 이해할 수 있을 수 있습니다.

이러한 유형의 시각화는 공간이 부족한 *Nature* 및 *Science*와 같은 주요 과학 저널에서 특히 인기가 있습니다. 이 책에서는 이러한 유형의 플롯을 다루지 않을 것입니다. 왜냐하면 매우 맞춤형인 경향이 있기 때문입니다.

### 서사적 데이터 시각화

세 번째이자 마지막 종류는 서사적 데이터 시각화입니다. 이것은 첫 번째 보기에서 최종 제품으로 넘어가는 단계에서 가장 많은 생각이 필요한 것입니다. 단순히 그림을 보여주는 것이 아니라 통찰력을 제공하는 시각화입니다. 이러한 종류의 시각화는 *Financial Times*, *The Economist* 또는 *BBC News* 웹사이트에서 볼 수 있습니다. 시청자가 제작자가 의도한 측면에 집중하도록 돕는 보조 도구가 함께 제공됩니다(이러한 보조 도구 또는 초점은 굵은 글꼴이 텍스트에 하는 것과 동일한 역할을 시각화에 한다고 생각할 수 있습니다). 특히 특정 서사를 전달하려고 하거나 소통하는 사람들이 주제에 대한 깊은 지식이 없는 경우 작업에 사용하는 것이 좋습니다. 폭넓은 독자층을 기대하는 논문, 작업을 요약하는 블로그 게시물 또는 정책 입안자를 위한 보고서에 사용할 수 있습니다.

데이터 시각화를 통한 의사소통 주제에 대한 자세한 내용은 {ref}`communicate-plots` 장에서 확인할 수 있습니다.
