Package include paths seem to be ignored when using per-function requirements (and specifying module), 
instead, only module contents are taken.

    18:51:21 -> sls package && unzip -l .serverless/functions/my_function-sls-test-dev-my_function.zip
    Serverless: Adding Python requirements helper to functions/my_function...
    Serverless: Installing requirements of functions/my_function/requirements.txt in .serverless/functions/my_function...
    Serverless: Zipping required Python packages for functions/my_function...
    Serverless: Packaging service...
    Serverless: Excluding development dependencies...
    Serverless: Removing Python requirements helper from functions/my_function...
    Serverless: Injecting required Python packages to package...
    Archive:  .serverless/functions/my_function-sls-test-dev-my_function.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
            0  2098-01-01 00:00   requirements.txt
           22  2098-01-01 00:00   .requirements.zip
          119  2098-01-01 00:00   handler.py
           34  2098-01-01 00:00   other_file.py
          458  2098-01-01 00:00   unzip_requirements.py
    ---------                     -------
          633                     5 files

Then when Commenting out serverless-python-requirements like so:

    #plugins:
    #  - serverless-python-requirements

I get:

    18:53:09 -> unzip -l .serverless/my_function.zip 
    Archive:  .serverless/my_function.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
           40  1980-01-01 00:00   functions/common/utils.py
           22  1980-01-01 00:00   functions/my_function/.requirements.zip
          119  1980-01-01 00:00   functions/my_function/handler.py
           34  1980-01-01 00:00   functions/my_function/other_file.py
            0  1980-01-01 00:00   functions/my_function/requirements.txt
    ---------                     -------
          215                     5 files


When leaving plugin registered, commenting out `module: functions/my_function`, 
and ensuring we have a root level requirements.txt

    18:53:23 -> touch requirements.txt
    18:55:01 -> sls package && unzip -l .serverless/my_function.zip 
    Serverless: Adding Python requirements helper to ....
    Serverless: Installing requirements of requirements.txt in .serverless...
    Serverless: Zipping required Python packages for ....
    Serverless: Packaging service...
    Serverless: Excluding development dependencies...
    Serverless: Removing Python requirements helper from ....
    Serverless: Injecting required Python packages to package...
    Archive:  .serverless/my_function.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
           22  1980-01-01 00:00   ./.requirements.zip
           40  1980-01-01 00:00   functions/common/utils.py
           22  1980-01-01 00:00   functions/my_function/.requirements.zip
          119  1980-01-01 00:00   functions/my_function/handler.py
           34  1980-01-01 00:00   functions/my_function/other_file.py
            0  1980-01-01 00:00   functions/my_function/requirements.txt
          458  1980-01-01 00:00   unzip_requirements.py
    ---------                     -------
          695                     7 files
