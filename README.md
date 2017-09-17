# THE iDOLM@STER Crawler Bot

## 만듦

아이마스 소식을 즐겨보는 페이지에서 새소식이 올라왔나 죽치고 있기도 하고
새로고침 하느라 시간을 허비하는 것이 아까워서 크롤링을 하게 해왔습니다.

## 설명

`Crawler` class의 원형은 이렇습니다.

    Crawler(crawl_method, period, queue, maximum, chan)

다음은 parameter의 명세입니다.

 * `crawl_method`
   * 필수, 타입은 method
   * 아래에서 설명합니다.
 * `period`
   * 크롤링 주기 입니다.
   * 단위는 초입니다.
   * 기본값은 60입니다.
 * `queue`
   * 크롤러가 정보를 담을 큐입니다.
   * 파이썬의 `Queue`를 참고해주세요.
   * 밑에 설명 나옵니다.
   * 기본값은 `None`입니다.
 * `maximum`
   * 새 글을 얼마나 기억하고 있을지 여부입니다.
   * 기본값은 40입니다.
 * `chan`
   * 모릅니다.
   * `None`입니다.

다음은 간단한 `Crawler`의 로직입니다.

 * `crawl_method`는 `list((prefix, title, link, date))`를 리턴해야 합니다.
 * `Crawler` instance (thread)에서 정해진 주기로 새 글이 나타났는지 가져오며
 * 받아온 정보를 바탕으로 `[prefix]| [title] [link] ([date])`를 만듭니다.
 * crawler에 queue 객체를 설정하면 해당 queue에 위 정보를 넣습니다.
 * 아닐 경우 stdout에 출력합니다.

저는 이 정보를 irc bot을 통해 가져오도록 했습니다

## 간단한 실행

    a = Crawler(selected_crawl_method)
    a.start()

## 크롤링 하는 곳

가져오는 곳이 아이마스를 위한 뿐만 게시판이 아닌 곳도 있고
글이 너무 자주 올라와 로그가 오염될 문제가 있는 곳도 있어서
아이마스 관련 글만 가져오도록 크롤러에 설정해두었습니다.
irc 채널에 있는 다른 분들을 위해서 자극적인 내용은 제외하고

 * 디시인사이드 아이돌 마스터 갤러리
   * 글이 많이 올라올 뿐더러 필터링이 되어야 하기 때문에 개념글만 봅니다.
   * 개념글도 이상한 것이 올라올 수 있기에 `만화`, `핫산`, `그림` 키워드로 필터링을 합니다.
 * 디시인사이드 765 프로 마이너 갤러리
   * 위와 동일합니다
 * 루리웹 팬픽 패러디 게시판
   * 아이마스 이외에도 많은 글이 올라오는 곳입니다.
   * 다행히 말머리를 제목에 달아주셔서 키워드로 필터링을 하고 있습니다.
   * 키워드: `@`, `아이마스`, `신데마스`, `밀리마스`, `밀리`, `신데`, `마스`, `푸치`, `765`, `346`, `876`, `315`, `961`
 * 아이돌 마스터 inven 공지사항 게시판
   * 데레스테에 관한 정보를 가져옵니다.
   * 아쉽게도 자유게시판 등은 글이 많이 올라오고 필터링 할 수 있는 기준도 없어서 가져올 수 없었습니다.
   * 아무래도 제 서버가 차단 당한 것 같습니다.
 * shunei 님 이글루스 블로그
   * 각종 아이마스 소식, 만화 번역, 게임 커뮤니케이션 번역, 가사 번역 등이 올라오는 곳입니다.
   * RSS를 이용합니다.
   * 잘 보고 있습니다.
   * 아이돌 마스터 태그가 붙은 것 중 잡담은 제외합니다.
 * yayo 님 이글루스 블로그
   * 각종 아이마스 동인지, 만화 번역물이 올라오던 곳입니다.

## 기타

자동으로 올라오는 것 뿐만 아니라,
직접 사이트에 찾아가서 미쳐 긁어오지 못 하거나,
필터되어 안 올라온 것도 읽습니다!

그 외에 추가할 사이트가 있다면 이슈로 알려주시면 감사하겠습니다.

`crawler` 코드는 출처(이 레포)만 표기한다면 가져가서 개조하셔도 상관없습니다.
기재를 안 한다면 어쩔 수 없지요...

감사합니다.

## 사족

본 리모트 저장소의 이름은 `idol`입니다.

    git push idol master

이게 리드미를 만든 이유

야호
