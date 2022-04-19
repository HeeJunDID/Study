import logging

# # 간단한 예시
# logging.warning("Watch out!")  # will print a message to the console
# logging.info("I told you so")  # will not print anything

# # 기본 수준이 WARNING이므로, INFO 메시지는 나타나지 않는다.
# # 인쇄된 메시지에는 수준 표시와 로깅 호출에 제공된 이벤트의 설명(즉, <Watch out!>)이 포함된다.


# 파일에 로깅하기
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError("Invalid log level: %s % loglevel")
# logging.basicConfig(filename="example.log", encoding="utf-8", level=numeric_level)
# logging.debug("This message should go to the log file")
# logging.info("So should this")
# logging.warning("And this, too")
# logging.error("And non-ASCII stuff, too, like Øresund and Malmö")

# 버전 3.9에서부터 encoding 인자가 추가되었다.


# 변수 데이터 로깅

# logging.warning("%s before you %s", "Look", "leap!")

# 표시된 메시지의 포맷 변경

# 메시지를 표시하는 데 사용되는 포맷을 변경하려면 사용할 format을 지정해야한다.
# logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
# logging.debug("This message should appear on the console")
# logging.info("So should this")
# logging.warning("And this, too")

# 메시지에 날짜/ 시간 표시


# logging.basicConfig(format="%(asctime)s %(message)s")
# logging.warning("is when this event was logged")

# 날짜/ 시간 표시의 기본 포맷은 ISO8601 또는 RFC 3339와 같다. 날짜/ 시간의 포맷을 좀 더 제어해야 하는 경우, basicConfig에 datefmt인자를 활용하면 된다.

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
logging.warning("is when this event was logged.")

# datefmt 인자의 형식은 time.strftime()에 의해 지원되는 것과 같다.
