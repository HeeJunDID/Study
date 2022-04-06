import logging

# # 간단한 예시
# logging.warning("Watch out!")  # will print a message to the console
# logging.info("I told you so")  # will not print anything

# # 기본 수준이 WARNING이므로, INFO 메시지는 나타나지 않는다.
# # 인쇄된 메시지에는 수준 표시와 로깅 호출에 제공된 이벤트의 설명(즉, <Watch out!>)이 포함된다.


# 파일에 로깅하기
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: %s % loglevel")
logging.basicConfig(filename="example.log", encoding="utf-8", level=numeric_level)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Øresund and Malmö")

# 버전 3.9에서부터 encoding 인자가 추가되었다.
