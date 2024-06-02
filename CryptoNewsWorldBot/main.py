from bot import bot
from loguru import logger


@logger.catch
def main() -> None:
    bot.polling(none_stop=True, interval=0, timeout=0)


if __name__ == '__main__':
    main()
