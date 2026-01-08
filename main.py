from config.settings import LOG_FILE, REPORT_FILE
from utils.logger import setup_logger
from app.reader import read_log_file
from app.analyzer import LogAnalyzer
from app.writer import write_report

logger = setup_logger("LogAnalyzer")

def main():
    logger.info("Startar logganalys")

    lines = read_log_file(LOG_FILE)
    analyzer = LogAnalyzer(lines)
    summary = analyzer.count_levels()

    write_report(REPORT_FILE, summary)

    logger.info("Analys klar")

if __name__ == "__main__":
    main()
