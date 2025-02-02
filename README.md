# 파이썬 데이터 분석 프로젝트: 자전거 공유 시스템 탐구

## 프로젝트 설명

이 프로젝트는 미국의 주요 도시인 시카고, 뉴욕, 워싱턴의 자전거 공유 시스템 데이터를 분석하는 것을 목표로 합니다.
 데이터 분석을 통해 각 도시의 자전거 이용 패턴, 사용자 행동, 그리고 통계적 인사이트를 도출할 수 있습니다. 
 이 프로젝트는 NanoDegree 프로그램의 일환으로 진행되며, 데이터 과학 및 분석 기술을 실습할 수 있는 좋은 기회를 제공합니다.

### 작성일

최종 업데이트: 2025년 1월 23일

### 프로젝트 제목

미국 자전거 공유 데이터 분석

### 프로젝트 목표

- **데이터 수집**: 각 도시의 자전거 공유 데이터셋을 수집하고 정리합니다.
- **데이터 분석**: 통계적 방법을 사용하여 자전거 이용 패턴을 분석합니다.
- **시각화**: 분석 결과를 시각적으로 표현하여 인사이트를 도출합니다.
- **결과 보고**: 분석 결과를 정리하여 보고서를 작성합니다.

### 설명

이 프로젝트는 시카고, 뉴욕, 워싱턴 세 도시의 자전거 공유 시스템 데이터를 분석합니다. 
통계 분석은 터미널 기반의 인터랙티브 프로그램을 통해 수행되며, 사용자는 다양한 필터를 적용하여 데이터를 탐색할 수 있습니다.
이 프로그램은 자전거 공유 시스템의 이용 현황을 탐색하고, 사용자 행동을 분석하는 데 도움을 줍니다.

### 사용된 파일

프로젝트는 각 도시의 데이터셋을 포함하는 세 개의 CSV 파일로 구성됩니다

- **Chicago.csv**: 시카고의 자전거 공유 데이터
- **New York City.csv**: 뉴욕의 자전거 공유 데이터
- **Washington.csv**: 워싱턴의 자전거 공유 데이터

대용량 CSV 파일은 `.gitignore`를 통해 버전 관리에서 제외됩니다. 이는 데이터 파일이 GitHub와 같은 버전 관리 시스템에 포함되지 않도록 하기 위함입니다.

또한, `bikeshare.py` 스크립트 파일이 프로그램 실행에 사용됩니다. 이 스크립트는 데이터 분석 및 통계 계산을 수행하고고, 사용자와의 인터랙션을 통해 결과를 출력합니다.

### 기술 스택

- **프로그래밍 언어**: Python
- **라이브러리**: Pandas, NumPy
- **데이터 포맷**: CSV