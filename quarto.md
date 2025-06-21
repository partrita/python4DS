(quarto)=
# 쿼토

이 장에서는 {ref}`workflow-writing-code`에서 간략하게 소개한 [**쿼토(Quarto)**](https://quarto.org/)에 대해 더 자세히 알아봅니다. **쿼토**는 코드와 텍스트(마크다운 형식, {ref}`markdown`에서 다룸)를 결합하여 보고서 및 프레젠테이션과 같은 풍부한 결과물을 만들 수 있는 도구입니다.

## 소개

쿼토는 데이터 과학을 위한 통합 저작 프레임워크로, 코드, 결과 및 산문 해설을 결합합니다. 쿼토는 완전히 재현 가능한 결과물을 허용하며 PDF, Microsoft Word 파일, 슬라이드쇼 등 수십 가지 출력 형식을 지원합니다.

쿼토 마크다운은 세 가지 방식으로 사용하도록 설계되었습니다.

1.  분석 이면의 코드가 아닌 결론에 집중하기를 원하는 의사 결정권자와 소통하기 위해.

2.  결론과 결론에 도달한 방법(즉, 코드) 모두에 관심이 있는 다른 데이터 과학자(미래의 자신 포함!)와 협업하기 위해.

3.  무엇을 했는지뿐만 아니라 무엇을 생각했는지도 기록할 수 있는 현대적인 실험실 노트로서 데이터 과학을 *수행*하는 환경으로.

예를 들어, 사용 사례는 최신 데이터를 가져와 플로팅하는 코드 부분이 포함된 최근 무역 통계를 탐색하는 기술 보고서일 수 있습니다. 또는 동일한 분석을 수행하지만 웹사이트에 게시할 수도 있습니다. 무엇보다도 최종 결과물에서 코드 부분을 숨기거나 표시할지 여부를 결정할 수 있습니다(또는 html 결과물의 경우 사용자가 코드를 볼지 여부를 선택하도록 허용). 더 자세히 살펴보면 사용 사례는 다음과 같습니다.

- 데이터 및/또는 차트를 사용하고 실행될 때마다 유사한 보고서(예: 데이터만 업데이트됨)

- 기존 코드베이스의 기능을 보여주거나 사용하는 기술 보고서

- 최신 데이터를 요약하고 정기적으로 생성되는 슬라이드 덱

- 공동 저자 또는 공동 작업자에게 탐색적 또는 프로토타입 분석 전송

- `.md` 파일을 허용하는 블로깅 서비스용 블로그 작성(마크다운으로 내보내기 확인)

- 비교적 쉽게 자동으로 업데이트되는 웹사이트 만들기——이 장에서는 다루지 않지만 [여기](https://quarto.org/docs/websites/)에서 이에 대한 정보를 찾을 수 있습니다.

**쿼토**는 자동화된 보고서를 편리하게 생성할 수 있도록 하는 여러 다른 도구에 대한 정말 편리한 래퍼입니다. 최신 사용 가이드는 최신 [설명서](https://quarto.org/docs/getting-started/quarto-basics.html)를 확인해야 합니다. 여기서는 기본 사항을 살펴보고 유용하게 사용할 수 있는 몇 가지 템플릿을 소개합니다.

### 전제 조건

먼저 [**쿼토** 웹사이트](https://quarto.org/)로 이동하여 [설치 지침](https://quarto.org/docs/getting-started/installation.html)을 따라야 합니다. 명령줄에서 `quarto check install`을 사용하여 올바르게 설치되었는지 확인할 수 있습니다.

Visual Studio Code [쿼토 확장](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)도 유용하며 이 책에서는 권장합니다. 이렇게 하면 Visual Studio Code 내에 "렌더링"이라는 특수 버튼이 만들어져 입력과 함께 출력이 어떻게 보일지 나란히 보여줍니다.

## **쿼토**를 사용한 자동화된 보고서

쿼토는 HTML, PDF, Microsoft Office(docx 및 pptx), OpenOffice 등 다양한 형식의 *출력* 문서 및 슬라이드를 만드는 데 사용할 수 있습니다.

다음 두 가지 방법으로 *입력* 문서(코드 조각 포함)를 작성할 수 있습니다.

1. 파일 확장자가 `.qmd`인 특수한 종류의 마크다운 파일. 마크다운에 대한 자세한 내용은 {ref}`markdown`을 참조하십시오. 특수 구문이 있는 코드 블록이 실행되고 그 결과가 모든 출력에 포함됩니다.

2. 파일 확장자가 `.ipynb`인 Jupyter Notebook. 코드 셀이 실행되고 그 결과가 모든 출력에 포함됩니다.

선택적으로 문서에 코드(예: Python, R, JavaScript 등)를 추가하여 동적으로 그림, 표 등을 만들고 쿼토를 사용하여 문서를 최종 형식으로 렌더링할 수 있습니다.

### 마크다운 콘텐츠로 작성된 보고서의 최소 예

이제 코드와 출력을 포함하는 `.qmd` 파일인 첫 번째 접근 방식의 가장 최소한의 예를 시도해 보겠습니다.

보고서를 `.qmd` 형식으로 작성하는 데는 장단점이 있습니다. 장점은 일반 텍스트 파일이므로 누구나 텍스트 편집기로 열고 보고 변경할 수 있다는 것입니다(이러한 방식으로 버전 관리에도 더 편리합니다). 가장 큰 단점은 코드를 작성하는 동안 코드가 어떻게 진행되는지 볼 수 없다는 것입니다(코드 출력을 보려면 렌더링해야 하며 잠시 후에 보게 될 것입니다). 다음 하위 섹션에서는 더 나은 워크플로를 달성하는 방법을 살펴보겠습니다.

최소 예제 설정을 해봅시다. 아래 코드와 마크다운은 `report.qmd`라는 파일의 내용을 구성합니다.

````markdown
---
title: "예제 보고서"
author: "조앤 로빈슨"
format: pdf
toc: true
number-sections: true
jupyter: python3
---

## 극좌표

극좌표에서의 선 그림 데모는 @fig-polar를 참조하십시오.

```{python}
#| label: fig-polar
#| fig-cap: "극좌표에서의 선 그림"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

이 예에는 세 가지 중요한 콘텐츠 유형이 포함되어 있습니다.

1.  `---`로 둘러싸인 **YAML 헤더**.
2.  ```` ``` ````로 둘러싸인 파이썬 코드 **청크**.
3.  `# 제목` 및 `_기울임꼴_`과 같은 간단한 텍스트 서식이 혼합된 마크다운.

이 '원시' 입력 쿼토 마크다운 `.qmd` 파일에서 `{python}`은 **쿼토**에게 코드 청크가 파이썬으로 되어 있고 실행되어야 함을 알려주고, `jupyter: python3`은 **쿼토**에게 사용할 Jupyter Notebook 설치를 알려줍니다. Jupyter 설치 이름이 확실하지 않은 경우 명령줄에서 `jupyter kernelspec list`를 실행하여 목록을 볼 수 있습니다.

### 출력 문서로 렌더링하기

위 보고서를 출력 PDF로 변환하려면 `report.qmd`로 저장한 다음 명령줄에서 파일과 동일한 디렉터리에서 다음을 실행합니다.

```bash
quarto render report.qmd
```

Visual Studio Code [쿼토 확장](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)(권장)을 사용하는 경우 대신 렌더링 버튼을 누를 수 있습니다(단, PDF를 출력으로 선택해야 함).

```{admonition} 연습

위 마크다운을 `report.qmd`라는 파일에 저장하여 PDF를 성공적으로 만듭니다.

Jupyter 커널을 찾을 수 없다는 오류가 발생하면 먼저 Jupyter Lab이 설치되어 있는지 확인한 다음 명령줄에서 `jupyter kernelspec list`를 사용하여 Jupyter 커널 이름을 확인합니다. 헤더 문서에서 Jupyter 커널 이름을 올바르게 지정해야 합니다(위 예에서는 기본값인 'python3'으로 지정됨).

```

이제 파일의 '헤더'에 `pdf`를 지정했으므로 자동으로 pdf를 얻었습니다. 그러나 다양한 출력 형식을 사용할 수 있습니다. 예를 들어 HTML은 다음과 같습니다.

```bash
quarto render report.qmd --to html
```

그리고 Microsoft Word는 다음과 같습니다.

```bash
quarto render report.qmd --to docx
```

Word 문서로 변환할 때 약간의 불편함은 코드의 표(데이터 프레임)가 Word 문서의 표로 렌더링되지 않는다는 것입니다.

기본 구문은 렌더링 명령 끝에 `--to 출력형식`을 작성하는 것입니다.

```{admonition} 연습

위 마크다운을 `report.qmd`라는 파일에 저장한 다음 html 옵션으로 쿼토 렌더링 명령을 실행하여 HTML 보고서를 성공적으로 만듭니다.

`##` 마크다운 구문을 사용하여 추가 제목을 추가하면 오른쪽 메뉴가 어떻게 됩니까?

```

### 코드 블록 실행 옵션

코드 블록 실행 방법에 대한 다양한 옵션이 있습니다. 실행되지 않는 코드 블록을 포함하려면 일반 마크다운 구문을 사용합니다(즉, ```` ```python ````으로 시작하는 블록). 그렇지 않으면 입력 코드를 표시할지, 결과만 표시할지, 둘 다 표시할지, 아니면 둘 다 표시하지 않을지(코드는 계속 실행하면서)에 대한 다양한 옵션이 있습니다.

입력이 표시되지 않는 코드 출력의 예로, 아래 코드는 `echo: false` 옵션을 사용하여 출력 테이블*만* 표시합니다.

````
```{python}
#| echo: false
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
pd.crosstab(df["species"], [df["island"], df["sex"]], margins=True)
```
````

아래 표는 코드 블록에 대한 모든 옵션을 제공합니다.

| 옵션 | 설명 |
|---|---|
| `eval` | 코드 청크 평가 (false인 경우 코드만 출력에 에코). |
| `echo` | 출력에 소스 코드 포함 |
| `output` | 코드 실행 결과를 출력에 포함 (true, false 또는 출력이 원시 마크다운이고 쿼토의 표준 포함 마크다운이 없어야 함을 나타내는 asis). |
| `warning` | 출력에 경고 포함. |
| `error` | 출력에 오류 포함 (이는 코드 실행 오류가 문서 처리를 중단하지 않음을 의미함). |
| `include` | 모든 출력(코드 또는 결과)이 포함되지 않도록 하는 포괄적인 기능 (예: include: false는 코드 블록의 모든 출력을 억제함). |
| `true` | 참 |
| `false` | 거짓 |

**텍스트와 함께 코드 결과를 인라인으로 삽입하는 것도 가능합니다.** 다음은 그 최소한의 예입니다.

````markdown
---
title: "코딩된 인라인 숫자가 포함된 예제 보고서"
author: "조앤 로빈슨"
format: pdf
toc: true
number-sections: true
jupyter: python3
---

## 보고서

극좌표에서의 선 그림 데모는 @fig-polar를 참조하십시오.

입력이 표시되지 않는 코드 출력의 예로, 아래 코드는 `echo: false` 옵션을 사용하여 출력 테이블*만* 표시합니다.

```{python}
#| echo: false
from IPython.display import display, Markdown
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
big_pen = df["body_mass_g"].max()
number = len(df)
```

### 가장 무거운 펭귄

총 `python f"{number}"` 마리의 펭귄 중 가장 무거운 펭귄의 질량은 `python f"{big_pen:.2f}"` 킬로그램인 것으로 나타났습니다.

````

이 예에서 `{big_pen:.2f}`의 `:2f` 부분은 지정된 숫자를 소수점 이하 2자리까지 보고하라는 지침입니다.

```{admonition} 연습

위 예제를 사용하여 인라인 숫자가 포함된 HTML 보고서를 만들되 가장 무거운 펭귄의 서식을 소수점 이하 자릿수를 표시하지 않도록 변경합니다.

```

물론 이 예제를 넘어서는 많은 추가 기능이 있습니다.

### Jupyter Notebook으로 작성된 보고서의 최소 예

Jupyter Notebook으로 보고서를 작성할 수도 있습니다. 다시 말하지만, 이러한 셀은 텍스트(마크다운 형식) 또는 코드(다양한 언어 지원)일 수 있으며 파일 형식은 `.ipynb`입니다. 이 책에서는 Visual Studio Code에서 작업하는 것을 권장합니다. Google Colab 노트북은 Jupyter 노트북의 한 유형이며(`.ipynb` 파일로 다운로드 가능)입니다.

Jupyter Notebook에서 자동화된 보고서를 작성하는 것은 `.qmd` 마크다운 파일을 사용하는 것보다 한 가지 주요 이점이 있습니다. 코드를 실행하면서 진행 상황을 알 수 있으므로 무엇을 얻고 있는지 알 수 있고 버그를 제거하기가 더 쉽습니다. 이 책에서는 자동화된 보고서를 작성하는 이 방법을 권장합니다.

그렇다면 위에서 본 것과 다른 점은 무엇일까요? 실제로는 거의 없습니다. 콘텐츠는 여전히 정확히 동일한 헤더로 시작하지만 이번에는 노트북 상단의 *마크다운 셀*에 있게 됩니다. 명시적으로 노트북의 첫 번째 셀에는 다음이 포함됩니다.

```markdown
---
title: "예제 보고서"
author: "조앤 로빈슨"
format: pdf
toc: true
number-sections: true
jupyter: python3
---
```

후속 셀은 풍부한 출력(그림 및 표)이 필요한지 텍스트가 필요한지에 따라 코드 또는 마크다운이 됩니다. 따라서 `.qmd` 접근 방식처럼 ```` ```{python} ````으로 시작하는 코드 청크 대신 새 코드 셀을 만듭니다.

이 헤더에 `format: pdf`를 넣으면 `render` 명령이 자동으로 pdf를 생성한다는 것을 기억하십시오. 대신 html 파일로 기본 설정하려면 `format: html`로 변경할 수 있으며 두 옵션 모두 `--to format`을 전달하여 덮어쓸 수 있습니다.

이전과 마찬가지로 코드 출력으로 동적으로 업데이트되는 텍스트를 만들 수도 있습니다. 마크다운 셀 대신 코드 셀을 선택하기만 하면 됩니다.

Jupyter Notebook의 주요 차이점은 **쿼토**로 렌더링하기 전에 노트북을 *실행*할지 여부를 결정해야 한다는 것입니다. 노트북을 실행한다는 것은 새 형식으로 내보내기 전에 코드를 실행하는 것을 의미합니다. (참고로 Jupyter Notebook을 사용하는 가장 좋은 방법은 코드 출력 없이 저장하는 것이므로 실행 및 렌더링이 표준적인 방법입니다.) 노트북을 실행하고 렌더링하는 터미널 명령은 다음과 같습니다.

```bash
quarto render jupyter-report.ipynb --execute
```

```{admonition} 연습

위 헤더를 사용하여 `jupyter-report.ipynb`라는 새 Jupyter Notebook을 만듭니다. 이전 섹션의 `qmd` 예제의 코드 및 텍스트 블록을 다시 사용합니다. 위 명령으로 렌더링합니다.

```

출력 유형을 변경하려면 `--to`를 사용하여 명령에 다른 지침을 추가합니다.

```bash
quarto render jupyter-report.ipynb --execute --to html
```

## 자동화된 보고서 작성을 위한 최적의 워크플로

이는 Visual Studio Code **쿼토** 확장을 사용하는 대안입니다.

이제 자동화된 보고서 및 슬라이드 작성을 위한 최적의 워크플로에 대한 중요한 팁으로 넘어갑니다. 코드를 변경함에 따라 최종 보고서가 어떻게 보일지 *실시간*으로 확인하는 데 관심이 있는 경우가 많습니다. 이는 Jupyter Notebook과 **쿼토**를 사용하여 가능합니다. 터미널에서 다음을 실행합니다.

```bash
quarto preview jupyter-report.ipynb
```

브라우저 창이 열리고 pdf의 실시간 미리보기가 표시됩니다(헤더에서 pdf를 기본 출력 옵션으로 설정한 경우). HTML 문서의 실시간 미리보기를 만들려면 다음과 같습니다.

```bash
quarto preview jupyter-report.ipynb --to html
```

아래 이미지는 Visual Studio Code의 Jupyter Notebook과 함께 미리보기를 사용하는 예를 보여줍니다.

![Jupyter 노트북 및 생성된 보고서의 실시간 HTML 미리보기](https://quarto.org/docs/tools/images/vscode-preview.png)

````{admonition} 연습
이전 연습의 Jupyter 예제를 가져와 형식을 HTML로 변경합니다. 그런 다음 위 `quarto preview` 명령을 사용하여 미리보기 모드에서 새 텍스트 셀과 새 그림(코드 셀에서)을 모두 추가합니다. 새 그림에 대한 영감이 필요하면 간단한 산점도가 있습니다.

```python
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(
    [1, 2, 3, 4, 5, 6],
    [1, 4, 2, 3, 1, 7],
    s=np.linspace(300, 2000, 6),
    c=["b", "r", "g", "k", "cyan", "yellow"],
    edgecolors="k",
    alpha=0.5,
)
plt.show()
```

````

## **쿼토**를 사용한 자동화된 슬라이드

만들 수 있는 것은 보고서뿐만이 아닙니다. 슬라이드 덱도 만들 수 있습니다. 슬라이드에 대해 선택할 수 있는 세 가지 주요 출력 형식이 있습니다.

- 'revealjs'라는 것을 통한 html; `format: revealjs` 사용
- LaTeX 비머 패키지를 통한 pdf; `format: beamer` 사용
- pptx 형식을 사용하는 Powerpoint; `format: pptx` 사용

다른 모든 것은 이전에 본 것과 동일합니다. 다음은 코드와 텍스트를 모두 보여주는 최소한의 예입니다. HTML 슬라이드 덱을 만듭니다.

````markdown
---
title: "내 발표"
author: "조앤 로빈슨"
format: revealjs
---

## 소개

- 이것은 약간의 텍스트입니다.
- 이것도 마찬가지입니다.

## 여기에 몇 가지 코드 출력이 있습니다.

```{python}
#| echo: false
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
````

코드 청크에 대해 `#| echo: false`를 설정했으므로 코드가 아닌 그림만 표시됩니다. 헤더에서 전체 덱에 대해 `echo: false`를 설정할 수도 있습니다.

```{admonition} 연습
이 슬라이드 예제를 세 가지 주요 형식으로 모두 렌더링합니다.
```

```{admonition} 연습
이전에 나온 가장 무거운 펭귄 예제를 수정하여 렌더링된 덱에 인라인 코드의 출력을 추가합니다.
```
