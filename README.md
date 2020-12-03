# RedVelvet Seulgi Fan Page

**[레드벨벳 슬기 팬 페이지](http://loveseulgi.kro.kr)**

위 링크는 현재 `LoveSeulgi v1` 이 서비스중이며 `LoveSeulgi v2 .Dev` 서버로 사용됩니다.

<br/>

|     날짜     | 작성자  |          비고           |
| :--------: | :--: | :-------------------: |
| 2019-02-12 | 이성필  |  LoveSeulgi 프로젝트 생성   |
| 2019-08-09 | 이성필  |  LoveSeulgi 프로젝트 배포   |
| 2019-09-20 | 이성필  | LoveSeulgi 프로젝트 v2 구상 |
| 2019-09-21 | 이성필  |  LoveSeulgi v2 개발 시작  |
| 2019-10-20 | 이성필  | 구직 활동으로 프로젝트 잠시 정지 |
| 2020-12-03 | 이성필  | 프로젝트 스택 재구성 예정 |

<br/>

### LoveSeulgi v2

- `Frontend` 와 `Backend` 구분
  - 기존 jinja2 + Django ( 순수 Django 기능 )
  - `Frontend` : Vue.js
  - `Backend` :  <del>django-rest-framework api server</del> Django
                 API Server를 운영하는데 DRF를 굳이 사용할 필요가 없을것같아 편한 개발 방식을 선택
- Database 변경
  - 기존 sqlite3
  - Postgresql / Mysql 로 변경예정
  - DB Relation 도 다시 짤 예정
  - AWS RDS 사용 예정 ( 이거 요금관리 잘해야할듯 )
- Website Renual
  - 기존에 있던 기능은 삭제되지 않으나 신규 기능이 추가될듯함
  - 웹 사이트 돌아다니면서 참고하기
  - 기존 UI 전부 수정할 계획
  - ↑ 현재 디자인이 너무 안좋기때문
- Crawler
  - 일정 시간 마다 실행되도록 container 올릴 예정
  - v1 에서 오류때문에 사용중지한 Multiprocessing 적용예정
  - AWS S3 사용 예정
  - 비 정상적인 페이지의 Url과 Content를 수집해야하기에 Blacklist 테이블 생성
  - dev. Chromedriver
  - prod. PhantomJS

<br/>



- Todo List 는 github Issue 기능으로 관리할 예정
- 프론트엔드 개발시간이 좀 걸릴예정
- Develop by sprumin@gmail.com 
