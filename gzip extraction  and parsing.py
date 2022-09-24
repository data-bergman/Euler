import re
import pathlib
import gzip
import os
import math



data_folder = []
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.2.gz"))
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.3.gz"))
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.4.gz"))
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.5.gz"))
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.6.gz"))
data_folder.append(pathlib.Path("C:/Users/erwan/Desktop/Delight/access-gateway-api-production/e0bfbda61cc38366b8bfe990abebba74cde6cb131aab386f49d7779a2011e60e-json.log.7.gz"))

3

dates_logs = {}
error_logs = {}

pattern1=re.compile(r"\d\d\d\d\-\d\d\-\d\d")

pattern2=re.compile(r"\d\d\d\d\-\d\d\-\d\dT\d\d\:\d\d\:\d\d\.\d+Z")

pattern3=re.compile(r"\[[^\]]\]")

for file_name in data_folder:
    with gzip.open(file_name, 'rb') as f:
        for line in f:
            matches= pattern1.finditer(str(line))
            for match in matches:
                date = match.group(0)
                if date not in dates_logs:
                    dates_logs[date] = {}
                matches = pattern2.finditer(str(line))
                for match in matches:
                    time = match.group(0)
                dates_logs[date][time]=(line)
                if "[error]" in str(line):
                    if date not in error_logs:
                        error_logs[date] = {}

                    matches = pattern2.finditer(str(line))
                    for match in matches:
                        time = match.group(0)
                    matches = pattern3.finditer(str(line))


                    error_logs[date][time]=line
                    print((str(line))[30:len(str(line))-(len(time)+39)])
                    print(line)

# os.makedirs(pathlib.Path(f"C:/Users/erwan/Desktop/Delight/logs/all_logs"))
#
# for date , times in dates_logs.items():
#     wlogs = gzip.open(pathlib.Path(f"C:/Users/erwan/Desktop/Delight/logs/all_logs/{date}.logs.gz"), "a+")
#     for time in times:
#         wlogs.write(times[time])
#     wlogs.close
#
# os.makedirs(pathlib.Path(f"C:/Users/erwan/Desktop/Delight/logs/error_logs"))
#
# for date , times in error_logs.items():
#     wlogs = gzip.open(pathlib.Path(f"C:/Users/erwan/Desktop/Delight/logs/error_logs/{date}.errorlogs.gz"), "a+")
#     for time in times:
#         wlogs.write(times[time])
#     wlogs.close