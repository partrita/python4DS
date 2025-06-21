# 데이터 과학을 위한 파이썬

[![DOI](https://zenodo.org/badge/496994611.svg)](https://zenodo.org/doi/10.5281/zenodo.10518241)  ![GitHub 릴리스](https://img.shields.io/github/v/release/aeturrell/python4DS)

이것은 **데이터 과학을 위한 파이썬**의 저장소입니다.

이 README는 개발자와 기여자를 위한 것입니다. 책을 읽으려면 [https://aeturrell.github.io/python4DS](https://aeturrell.github.io/python4DS)로 이동하십시오.

## 기여하기

저희는 기여자들을 적극적으로 환영합니다! 책에 대한 문제를 제기하거나 직접 풀 리퀘스트를 생성하여 기여할 수 있습니다. 풀 리퀘스트를 생성하는 경우 로컬에 개발 환경을 설치하고 변경 사항을 적용한 후 책이 빌드되는지 확인해야 합니다.

저희는 [**데이터 과학을 위한 R (2e)**](https://r4ds.hadley.nz/)의 내용을 밀접하게 따르는 것을 목표로 합니다.

풀 리퀘스트를 만들기 전에 사전 커밋 검사가 통과하는지, 출력이 포함되어 있지 않은지, 책이 빌드되는지 테스트해야 합니다. 로컬에서 이러한 작업을 수행하는 방법에 대한 지침은 아래를 참조하십시오.

풀 리퀘스트를 만들면 사전 커밋 및 빌드가 자동으로 실행되며 오류가 있으면 실패합니다. 이는 `.github/workflows/tests.yml`에 있습니다.

## 로컬에 개발 환경 설치하기

파이썬 3.10과 [**uv**](https://docs.astral.sh/uv/) 설치가 필요합니다. **uv**는 `uv python install 3.10` 명령을 통해 특정 파이썬 배포판을 설치하는 데 사용할 수 있지만 다른 파이썬 설치를 사용할 수도 있습니다.

이 저장소를 복제하십시오.

개발 환경을 설치하려면 프로젝트 루트에서 `uv sync`를 실행하십시오. 이렇게 하면 Python4DS 환경이 포함된 `.venv/` 디렉터리가 생성됩니다. 프로젝트 루트 디렉터리에서 `uv run python -V`를 실행하여 환경이 설치되었는지 확인할 수 있습니다.

## 책 빌드하기

이 책은 소스 마크다운 및 주피터 노트북 파일에서 [**jupyter-book**](https://jupyterbook.org/en/stable/) 패키지를 사용하여 컴파일됩니다.

책을 빌드하려면 다음을 실행하십시오.

```bash
uv run playwright install --with-deps chromium
uv run jupyter-book build . --builder pdfhtml
```

이 명령을 실행하면 컴퓨터에서 로컬로 책의 PDF 파일을 볼 수 있습니다. 오류가 발생하면 빌드를 중지하도록 구성되어 있습니다. 이는 자주 발생하는 일입니다! 무엇이 잘못되었는지 확인하려면 로그를 살펴봐야 합니다.

## 책 업로드하기

### 책 자동 업로드

이 저장소는 새 버전이 자동으로 책을 빌드하고 웹사이트에 업로드하도록 구성되어 있습니다. 이 작업을 수행하는 GitHub Action은 `.github/workflows/release.yml`에 있습니다.

### 빌드된 책 수동 업로드

일반적인 기여자라면 책을 업로드할 필요가 없습니다. 관리자로서 필요할 때가 있을 수 있지만 일반적으로 새 버전이 릴리스되면 책이 자동으로 업데이트됩니다.

수정된 HTML 파일을 업로드하는 방법에 대해서는 [여기](https://jupyterbook.org/publish/gh-pages.html)를 참조하십시오. 주요 명령은 다음과 같습니다.

```bash
uv run ghp-import -n -p -f _build/html
```

## 코드 위생

이 책은 사전 커밋을 사용하여 노트북에서 출력을 제거하고, 린트하고, 형식을 지정하고, 실수로 추가된 큰 파일을 확인합니다.

사전 커밋 검사를 수행하려면 다음을 사용하십시오.

```bash
uv run pre-commit run --all-files
```

스테이징된 파일에 대해. 커밋하기 전에 사전 커밋이 모든 테스트를 통과했다고 보고하는지 확인하십시오.

## 새 버전 게시하기

1. 버전 이름(예: `v1.0.4`)으로 새 브랜치를 엽니다.

2. `pyproject.toml`에서 버전을 변경합니다(스크립트 수준 종속성이 있는 `uv run version_bumper.py`를 실행할 수 있음).

3. 커밋 메시지로 새 버전 레이블(예: `v1.0.4`)을 사용하여 변경 사항을 커밋합니다.

4. GitHub로 이동합니다. 테스트가 통과하면 기본 브랜치에 병합합니다.

5. 책은 GitHub 작업에서 자동으로 빌드되어 웹사이트에 푸시되어야 합니다. 새 릴리스도 자동으로 생성됩니다. 새 Zenodo 항목도 자동으로 생성됩니다.

## Docker 컨테이너에서 실행 및 개발하기

이 프로젝트와 관련된 Dockerfile이 있습니다. 사전 요구 사항:

1. 사전 요구 사항: Docker 설치, VS Code 설치, VS Code Docker 및 원격 탐색기 확장 프로그램 설치.
2. 파일에서 이미지를 빌드합니다. VS Code에서 파일을 마우스 오른쪽 버튼으로 클릭하고 "이미지 빌드"를 선택합니다.
3. VS Code의 Docker 탭에서 `python4DS:latest` 이미지를 마우스 오른쪽 버튼으로 클릭하고 '대화형으로 실행'을 선택합니다.
4. Docker 탭에서 실행 중인 `python4DS:latest` 컨테이너를 다시 마우스 오른쪽 버튼으로 클릭하고 "Visual Studio Code 연결"을 클릭합니다.
5. 필요에 따라 개발을 수행합니다(위 지침 참조).

빌드된 HTML 파일과 같은 파일을 로컬 시스템에 다시 복사하여 확인하려면 다음을 사용하십시오.

```bash
docker cp CONTAINER:app/_build/html/ temp_dir/
```
