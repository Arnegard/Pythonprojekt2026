class LogAnalyzer:
    def __init__(self, lines):
        self.lines = lines

    def count_levels(self):
        levels = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

        for line in self.lines:
            for level in levels:
                if level in line:
                    levels[level] += 1

        return levels
