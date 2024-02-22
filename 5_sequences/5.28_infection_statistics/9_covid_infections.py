import statistics

infections = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,
              1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# print minimum, maximum, range, mean, median, variance and standard deviation
print("\nStatistics:\n"
      f"minimum: {min(infections)}\n"
      f"maximum: {max(infections)}\n"
      f"range: {max(infections)-min(infections)}\n"
      f"mean: {statistics.mean(infections)}\n"
      f"median: {statistics.median(infections)}\n"
      f"variance: {statistics.variance(infections)}\n"
      f"standard deviation: {statistics.stdev(infections)}" )