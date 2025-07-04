---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: py4ds2e
  language: python
  name: python3
---
(workflow-help)=
# 추신: 추가 도움 받기

이 책은 외딴 섬이 아닙니다. 데이터 과학을 위한 파이썬을 마스터하는 데 도움이 되는 단일 자료는 없습니다. 이 책에서 설명하는 기술을 자신의 데이터에 적용하기 시작하면 곧 우리가 답변하지 않는 질문을 발견하게 될 것입니다. 이 섹션에서는 도움을 받고 계속 학습하는 데 도움이 되는 몇 가지 팁을 설명합니다.

## 자료

학습을 위한 다른 자료는 다음과 같습니다.

- [파이썬 데이터 과학 핸드북](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [리얼 파이썬](https://realpython.com/), 파이썬을 더 광범위하게 다루는 훌륭한 짧은 튜토리얼(데이터 과학뿐만 아니라)
- [freeCodeCamp의 파이썬 과정](https://www.freecodecamp.org/news/search?query=data%20science%20python), 자신에게 맞는 수준의 과정을 선택하도록 주의하십시오.
- [경제학자를 위한 코딩](https://aeturrell.github.io/coding-for-economists), 이 책과 유사한 내용을 담고 있지만 더 심층적이며 분석가(특히 경제학)를 대상으로 합니다.

## 구글은 당신의 친구입니다

막히면 구글부터 시작하십시오. 일반적으로 쿼리에 "Python" 또는 "Python Data Science"(파이썬 생태계는 데이터 과학을 *훨씬* 넘어섭니다)를 추가하면 관련 결과로 제한하기에 충분합니다. 구글은 특히 오류 메시지에 유용합니다. 오류 메시지가 표시되고 무슨 의미인지 전혀 모르는 경우 구글링해 보십시오! 과거에 다른 사람이 혼란스러워했을 가능성이 높으며 웹 어딘가에 도움이 있을 것입니다.

구글이 도움이 되지 않으면 [스택 오버플로](http://stackoverflow.com)를 시도해 보십시오. 파이썬을 사용하는 질문과 답변으로 검색을 제한하려면 `[Python]`을 포함하여 기존 답변을 찾는 데 약간의 시간을 할애하십시오.

## 최신 정보 확인

데이터 과학의 최신 개발 동향을 주시하는 것도 도움이 됩니다. 수많은 데이터 과학 뉴스레터가 있으며 트위터에서 (#pydata), (#datascience) 및 (#python) 해시태그를 팔로우하여 파이썬 데이터 과학 커뮤니티의 최신 정보를 확인하는 것이 좋습니다.

## 재현 가능한 예제(reprex) 만들기

구글링으로 유용한 정보를 찾지 못했다면 최소한의 재현 가능한 예제 또는 **reprex**를 준비하는 것이 매우 좋습니다.

좋은 reprex는 다른 사람들이 당신을 돕기 쉽게 만들고, 종종 만드는 과정에서 문제를 스스로 파악하게 됩니다. reprex를 만드는 데는 두 가지 부분이 있습니다.

- 첫째, 코드를 재현 가능하게 만들어야 합니다. 즉, 사용한 모든 패키지를 포함하고 필요한 모든 개체를 만드는 등 모든 것을 캡처해야 합니다. 이를 확인하는 가장 쉬운 방법은 다른 작업과 함께 [**watermark**](https://github.com/rasbt/watermark) 패키지를 사용하는 것입니다.

```{code-cell} ipython3
import pandas as pd
import numpy as np
import watermark.watermark as watermark

print(watermark())
print(watermark(iversions=True, globals_=globals()))
```

- 둘째, 최소화해야 합니다. 문제와 직접 관련이 없는 모든 것을 제거하십시오. 여기에는 일반적으로 실제 생활에서 직면하는 것보다 훨씬 작고 간단한 파이썬 개체를 만들거나 내장 데이터를 사용하는 것이 포함됩니다.

일이 많은 것처럼 들립니다! 그리고 그럴 수도 있지만 큰 성과가 있습니다.

- 훌륭한 reprex를 만드는 시간의 80%는 문제의 원인을 드러냅니다. 독립적이고 최소한의 예제를 작성하는 과정이 자신의 질문에 답할 수 있게 해주는 경우가 놀랍도록 많습니다.

- 나머지 20%의 시간에는 다른 사람들이 쉽게 가지고 놀 수 있는 방식으로 문제의 본질을 포착하게 됩니다. 이렇게 하면 도움을 받을 가능성이 크게 향상됩니다.

예제를 재현 가능하게 만들기 위해 포함해야 할 몇 가지 사항이 있습니다. 파이썬 환경, 필수 패키지, 데이터 및 코드입니다.

- **파이썬 환경**--실제로는 파이썬 버전입니다. 이것은 **watermark** 패키지에 대한 첫 번째 호출에서 다룹니다.

- **패키지** 및 해당 버전. 스크립트 상단에 로드하여 예제에 필요한 패키지를 쉽게 확인할 수 있도록 해야 합니다. 위 구성으로 **watermark**를 사용하면 패키지 버전도 인쇄됩니다. 각 패키지의 최신 버전을 사용하고 있는지 확인하기에 좋은 시기입니다. 패키지를 설치하거나 마지막으로 업데이트한 이후 수정된 버그를 발견했을 수 있습니다.

- **데이터**: 다른 사람들이 작업 중인 데이터를 쉽게 다운로드할 수 없으므로 실제 데이터에서 발견하는 것과 동일한 문제가 여전히 있는 코드에서 소량의 데이터를 만드는 것이 가장 좋습니다. **numpy**와 **pandas** 사이에서는 코드에서 데이터를 생성하기가 매우 쉽습니다. 다음은 예입니다.

```{code-cell} ipython3
df = pd.DataFrame(
    data=np.reshape(range(36), (6, 6)),
    index=["a", "b", "c", "d", "e", "f"],
    columns=["col" + str(i) for i in range(6)],
    dtype=float,
)
df["random_normal"] = np.random.normal(size=6)
df
```

- **코드**: 최소한의 재현 가능한 예제 코드(위에 언급된 패키지 포함)를 복사하여 붙여넣습니다. 공백을 사용하고 변수 이름이 간결하면서도 정보를 제공하는지 확인하십시오. 주석을 사용하여 문제가 있는 위치를 나타냅니다. 문제와 관련 없는 모든 것을 제거하기 위해 최선을 다하십시오. 마지막으로 코드가 짧을수록 이해하기 쉽고 수정하기 쉽습니다.

새 파이썬 세션을 시작하고 reprex를 복사하여 붙여넣어 실제로 재현 가능한 예제를 만들었는지 확인하여 마무리합니다.
