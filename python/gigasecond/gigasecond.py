from datetime import timedelta

def add(moment):
    secdelta = 1_000_000_000
    d = timedelta(seconds=secdelta)
    return moment + d
