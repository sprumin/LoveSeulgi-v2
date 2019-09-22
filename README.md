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

<br/>

### LoveSeulgi v2

- `Frontend` 와 `Backend` 구분
  - 기존 jinja2 + Django ( 순수 Django 기능 )
  - `Frontend` : Vue.js
  - `Backend` :  django-rest-framework api server
- Database 변경
  - 기존 sqlite3
  - Postgresql / Mysql 로 변경예정
  - DB Relation 도 다시 짤 예정
- Website Renual
  - 기존에 있던 기능은 삭제되지 않으나 신규 기능이 추가될듯함
  - 웹 사이트 돌아다니면서 참고하기
  - 기존 UI 전부 수정할 계획
  - ↑ 현재 디자인이 너무 안좋기때문
- Crawler
  - 기존 django custom command 로 수동으로 실행해
  - python 프로젝트로 따로 분리하여 cron 으로 실행할예정
  - v1 에서 오류때문에 사용중지한 Multiprocessing 적용예정

<br/>



- Todo List 는 github Issue 기능으로 관리할 예정
- Develop by sprumin@gmail.com 
