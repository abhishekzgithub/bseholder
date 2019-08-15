LOG_FORMAT = "[%(asctime)s]-{%(pathname)s:%(lineno)d}-{%(levelname)s}-{In file ->%(module)s " \
             "In function ->%(funcName)s}-{%(message)s}"
q="""select (BSETicker) from TblCompany where Ticker != '' and BSETicker != '' and BSETicker is not Null;"""